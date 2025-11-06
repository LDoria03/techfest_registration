# TechFest Registration System

# Task 1: Registration Setup
print("Welcome to SMIT TechFest!")
print("Event organized by Lorenzo Luis F. Doria of APPDAET BTCS2")
print()

num_participants = int(input("How many participants will register? "))

if num_participants <= 0:
    print("Invalid number of participants.")
else:
    # Task 2: Collect Participant Information
    participants = []

    for i in range(num_participants):
        name = input("Enter participant name: ")
        track = input("Enter chosen track: ")
        participant = {"name": name, "track": track}
        participants.append(participant)

    # Display registered participants
    print("\nRegistered Participants:")
    for i in range(len(participants)):
        print(f"{i + 1}. {participants[i]['name']} - {participants[i]['track']}")

