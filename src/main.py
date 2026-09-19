from viterbi import viterbi, get_probability


def house():

    states = ["Hallway", "Master_Bedroom", "Bathroom", "Toilet",
              "Guest_Bedroom", "Kitchen", "Living_Room", "Basement_Stairs", "Office", "Outside"]

    start_probability = {
        "Hallway": 0.1,
        "Master_Bedroom": 0.02,
        "Bathroom": 0.01,
        "Toilet": 0.01,
        "Guest_Bedroom": 0.02,
        "Kitchen": 0.01,
        "Living_Room": 0.02,
        "Basement_Stairs": 0.1,
        "Office": 0.01,
        "Outside": 0.7
    }

    transition_probability = {
        "Hallway": {
            "Hallway": 0.1,
            "Master_Bedroom": 0.1,
            "Bathroom": 0.1,
            "Toilet": 0.1,
            "Guest_Bedroom": 0.1,
            "Kitchen": 0.1,
            "Living_Room": 0.1,
            "Basement_Stairs": 0.1,
            "Office": 0.1,
            "Outside": 0.1
        },
        "Master_Bedroom": {
            "Hallway": 0.5,
            "Master_Bedroom": 0.5,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0,
            "Living_Room": 0,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0
        },
        "Bathroom": {
            "Hallway": 0.5,
            "Master_Bedroom": 0,
            "Bathroom": 0.5,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0,
            "Living_Room": 0,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0
        },
        "Toilet": {
            "Hallway": 0.5,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0.5,
            "Guest_Bedroom": 0,
            "Kitchen": 0,
            "Living_Room": 0,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0
        },
        "Guest_Bedroom": {
            "Hallway": 0.5,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0.5,
            "Kitchen": 0,
            "Living_Room": 0,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0
        },
        "Kitchen": {
            "Hallway": 0.34,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0.33,
            "Living_Room": 0.33,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0
        },
        "Living_Room": {
            "Hallway": 0.4,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0.2,
            "Living_Room": 0.2,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0.2
        },
        "Basement_Stairs": {
            "Hallway": 0.5,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0,
            "Living_Room": 0,
            "Basement_Stairs": 0.5,
            "Office": 0,
            "Outside": 0
        },
        "Office": {
            "Hallway": 0.5,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0,
            "Living_Room": 0,
            "Basement_Stairs": 0,
            "Office": 0.5,
            "Outside": 0
        },
        "Outside": {
            "Hallway": 0.33,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0.33,
            "Living_Room": 0,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0.34
        }
    }
    sensor_trigger_probability = {
        # Sensors that are 100%
        "Contact_Sensor_Office_Window": {
            "Office": 1
        },
        "Contact_Sensor_Master_Bedroom_Window": {
            "Master_Bedroom": 1
        },
        "Smart_Kettle": {
            "Kitchen": 1
        },
        # Inbetween 50/50
        "Contact_Sensor_Master_Bedroom_Door": {
            "Master_Bedroom": 0.5,
            "Hallway": 0.5
        },
        "Contact_Sensor_Front_Door": {
            "Outside": 0.5,
            "Hallway": 0.5
        },
        # Sensors that may trigger from neighboring rooms
        "Hallway_Motion": {
            "Hallway": 0.55,
            "Master_Bedroom": 0.05,
            "Bathroom": 0.05,
            "Toilet": 0.05,
            "Guest_Bedroom": 0.05,
            "Kitchen": 0.05,
            "Living_Room": 0.05,
            "Basement_Stairs": 0.05,
            "Office": 0.05,
            "Outside": 0.05
        },
        "Master_Bedroom_Motion": {
            "Hallway": 0.05,
            "Master_Bedroom": 0.85,
            "Bathroom": 0.05,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0,
            "Living_Room": 0,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0.05
        },
        "Bathroom_Motion": {
            "Hallway": 0.05,
            "Master_Bedroom": 0.05,
            "Bathroom": 0.8,
            "Toilet": 0.05,
            "Guest_Bedroom": 0,
            "Kitchen": 0,
            "Living_Room": 0,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0.05
        },
        "Toilet_Motion": {
            "Hallway": 0.15,
            "Master_Bedroom": 0,
            "Bathroom": 0.05,
            "Toilet": 0.8,
            "Guest_Bedroom": 0,
            "Kitchen": 0,
            "Living_Room": 0,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0
        },
        "Guest_Bedroom_Motion": {
            "Hallway": 0.1,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0.8,
            "Kitchen": 0,
            "Living_Room": 0.05,
            "Basement_Stairs": 0.05,
            "Office": 0,
            "Outside": 0
        },
        "Kitchen_Motion": {
            "Hallway": 0.1,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0.8,
            "Living_Room": 0.05,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0.05
        },
        "Living_Room_Motion": {
            "Hallway": 0.1,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0.05,
            "Living_Room": 0.8,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0.05
        },
        "Basement_Stairs_Motion": {
            "Hallway": 0.1,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0.05,
            "Kitchen": 0,
            "Living_Room": 0,
            "Basement_Stairs": 0.8,
            "Office": 0,
            "Outside": 0.05
        },
        "Office_Motion": {
            "Hallway": 0.1,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0.05,
            "Living_Room": 0,
            "Basement_Stairs": 0,
            "Office": 0.8,
            "Outside": 0.05
        },
        "Outside_Motion": {
            "Hallway": 0.2,
            "Master_Bedroom": 0,
            "Bathroom": 0,
            "Toilet": 0,
            "Guest_Bedroom": 0,
            "Kitchen": 0,
            "Living_Room": 0,
            "Basement_Stairs": 0,
            "Office": 0,
            "Outside": 0.8
        },
    }

    observation_probabilities = map_sensors(sensor_trigger_probability, states)

    return states, start_probability, transition_probability, observation_probabilities


def map_sensors(sensors, states):
    observation_probabilities = {}
    for state in states:
        observation_probabilities[state] = {}

    for sensor, rooms in sensors.items():
        for room, probability in rooms.items():
            observation_probabilities[room][sensor] = probability

    # Normalize the values for Viterbi
    for room, sensor_probs in observation_probabilities.items():
        total = 0
        for sensor, probability in sensor_probs.items():
            total = total + probability

        if total > 0:
            for sensor, current_probability in sensor_probs.items():
                sensor_probs[sensor] = current_probability / total

    return observation_probabilities


def simulation():
    states, start_probability, transition_probability, observation_probabilities = house()

    # Subjects own records where they where when the sensor events happend
    record = [
        "Outside",
        "Hallway",
        "Kitchen",
        "Kitchen",
        "Living_Room",
        "Living_Room",  # During false sensor reading
        "Living_Room",
        "Hallway"
    ]

    sensor_readings = [
        "Contact_Sensor_Front_Door",
        "Hallway_Motion",
        "Kitchen_Motion",
        "Smart_Kettle",
        "Living_Room_Motion",
        "Toilet_Motion",  # Triggered on its own
        "Living_Room_Motion",
        "Hallway_Motion",
    ]

    viterbi_path = viterbi(sensor_readings, states, start_probability,
                           transition_probability, observation_probabilities)
    # What happends if we just read the sensors and expect them to reprt the most likely room.
    path_by_mostlikely_sensor_room = []

    for reading in sensor_readings:
        room = None
        max_probability = -1
        for state in states:
            probability = get_probability(
                observation_probabilities, state, reading)
            if probability > max_probability:
                max_probability = probability
                room = state
        path_by_mostlikely_sensor_room.append(room)

    print("SIMULATION")
    print("Event order | Sensor | True Room | By Likely Sensor Position | Viterbi")

    for iterator, sensor in enumerate(sensor_readings):
        true_room = record[iterator]
        sensor_room = path_by_mostlikely_sensor_room[iterator]
        viterbi_room = viterbi_path[iterator]
        if viterbi_room != true_room:
            viterbi_room = viterbi_room + " Fail"
        if sensor_room != true_room:
            sensor_room = sensor_room + " Fail"
        print(f"{iterator} | {sensor} | {true_room} | {sensor_room} | {viterbi_room}")


if __name__ == "__main__":
    simulation()
