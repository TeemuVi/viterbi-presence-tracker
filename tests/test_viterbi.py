from viterbi import viterbi


def test_pytest():
    assert True


def test_empty_observations():
    assert viterbi([], ["Room_1", "Room_2"], {}, {}, {}) == []


def test_move_2_rooms():
    states = ["Room_1", "Room_2"]
    start_state_probability = {
        "Room_1": 0.6,
        "Room_2": 0.4
    }
    move_probability = {
        "Room_1": {"Room_1": 0.2, "Room_2": 0.8},
        "Room_2": {"Room_2": 0.3, "Room_1": 0.7}
    }

    emission_probability = {
        "Room_1": {"sensor_in_room_1": 0.95, "sensor_in_room_2": 0.05},
        "Room_2": {"sensor_in_room_2": 0.95, "sensor_in_room_1": 0.05}
    }

    observations = ["sensor_in_room_1", "sensor_in_room_2"]

    expected_path = ["Room_1", "Room_2"]
    prediction = viterbi(observations, states, start_state_probability,
                         move_probability, emission_probability)

    assert prediction == expected_path


def test_impossible_movement():
    # can't move from room A to C without going to room B first
    states = ["Room_A", "Room_B", "Room_C"]
    start_probability = {"Room_A": 1, "Room_B": 0, "Room_C": 0}
    transition_probability = {
        "Room_A": {"Room_A": 0.5, "Room_B": 0.5, "Room_C": 0},
        "Room_B": {"Room_A": 0.3, "Room_B": 0.4, "Room_C": 0.3},
        "Room_C": {"Room_A": 0, "Room_B": 0.5, "Room_C": 0.5}
    }
    # Sensors
    emission_probability = {
        "Room_A": {"Sensor_room_A": 0.9, "Sensor_room_B": 0.05, "Sensor_room_C": 0.05},
        "Room_B": {"Sensor_room_A": 0.05, "Sensor_room_B": 0.9, "Sensor_room_C": 0.05},
        "Room_C": {"Sensor_room_A": 0.05, "Sensor_room_B": 0.05, "Sensor_room_C": 0.9}
    }
    # Hallusinating sensor fires
    observations = ["Sensor_room_A", "Sensor_room_C"]
    predicted_path = viterbi(observations, states,
                             start_probability, transition_probability, emission_probability)
    # Since Room_A -> Room_C is impossible (0), it should NOT pick Room_C at step 2!
    assert predicted_path[1] != "Room_C"
