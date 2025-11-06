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

    # Task 3: Track Diversity Report
    print("\nTracks offered in this event:")
    unique_tracks = set()
    for p in participants:
        unique_tracks.add(p["track"])

    track_list = list(unique_tracks)
    print(", ".join(track_list))

    if len(unique_tracks) < 2:
        print("Not enough variety in tracks.")

    # Task 4: Duplicate Name Detection
    print()
    seen_names = set()
    duplicate_found = False

    for p in participants:
        if p["name"] in seen_names:
            print(f"Duplicate name found: {p['name']}")
            duplicate_found = True
        seen_names.add(p["name"])

    if not duplicate_found:
        print("No duplicate names.")

    # Task 5: Track Summary Report
    print("\nParticipants per track:")
    track_count = {}

    for p in participants:
        if p["track"] in track_count:
            track_count[p["track"]] += 1
        else:
            track_count[p["track"]] = 1

    for track in track_count:
        print(f"{track}: {track_count[track]}")
