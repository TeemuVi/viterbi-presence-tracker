import math


def viterbi(observations, states, start_probability, transition_probability, emission_probability):
    """
    "The Viterbi algorithm is a dynamic programming algorithm that finds the most likely sequence of hidden events that would explain a sequence of observed events.
    The result of the algorithm is often called the Viterbi path. It is most commonly used with hidden Markov models (HMMs). "
    - source wikipedia

    Returns a list of the most probable states of the path. If no observations return empty list.
    """
    if not observations:
        return []

    # Highest log-probability of being at that state at that time [time][state]
    viterbi_table = [{}]

    # The bread crums back [time][state]
    backpointers = [{}]

    first_observation = observations[0]

    for state in states:
        start = start_probability.get(state, 0)
        sensor_probabilities_for_state = emission_probability.get(state, {})
        emission = sensor_probabilities_for_state.get(first_observation, 0)
        viterbi_table[0][state] = to_log(start) + to_log(emission)
        backpointers[0][state] = None
    for time in range(1, len(observations)):
        viterbi_table.append({})
        backpointers.append({})
        current_observation = observations[time]

        for new_state in states:
            max_score_transition = -math.inf
            best_state = None

            for old_state in states:
                transition = get_probability(
                    transition_probability, old_state, new_state)
                score = viterbi_table[time - 1][old_state] + to_log(transition)
                if score > max_score_transition:
                    max_score_transition = score
                    best_state = old_state

            sensor_probability = emission_probability.get(new_state, {})
            emission = sensor_probability.get(current_observation, 0)

            viterbi_table[time][new_state] = max_score_transition + \
                to_log(emission)
            backpointers[time][new_state] = best_state

    last_time = len(observations)-1
    max_score_final = -math.inf
    best_last_state = None

    for state in states:
        if viterbi_table[last_time][state] > max_score_final:
            max_score_final = viterbi_table[last_time][state]
            best_last_state = state

    path = [best_last_state]
    now_state = best_last_state

    for time in range(last_time, 0, -1):
        now_state = backpointers[time][now_state]
        path.append(now_state)

    path.reverse()
    return path


def get_probability(table, row, column):
    # returns 0 if missing
    return table.get(row, {}).get(column, 0)


def to_log(probability):
    if probability <= 0:
        return -math.inf
    return math.log(probability)
