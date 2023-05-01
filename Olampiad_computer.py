num_participants = int(input())

# Create empty lists for male and female participants
male_participants = []
female_participants = []

# Loop over the number of participants
for i in range(num_participants):
    participant_info = input().split('.')
    name = participant_info[1]
    gender = participant_info[0]
    language = participant_info[2]

    # Standardize the name
    name = name.capitalize()

    # Append the participant to the appropriate list
    if gender == 'm':
        male_participants.append((name, language))
    else:
        female_participants.append((name, language))

# Sort the participants by name
male_participants = sorted(male_participants)
female_participants = sorted(female_participants)

# Print the female participants
for participant in female_participants:
    print('f', participant[0], participant[1])

# Print the male participants
for participant in male_participants:
    print('m', participant[0], participant[1])