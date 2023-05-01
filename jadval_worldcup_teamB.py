# تعریف دیکشنری برای ذخیره نتایج
results = {
    "Iran": [0, 0, 0, 0],  # [برد، باخت، تفاضل گل، امتیاز]
    "Portugal": [0, 0, 0, 0],
    "Spain": [0, 0, 0, 0],
    "Morocco": [0, 0, 0, 0],
}

# تعریف تابع برای به‌روزرسانی نتایج
def update_results(team, goal_diff, points):
    results[team][2] += goal_diff
    results[team][3] += points
    if goal_diff > 0:
        results[team][0] += 1
    elif goal_diff < 0:
        results[team][1] += 1
    else:
        results[team][0] += 1
        results[team][3] += 1

match1_score = input()
match2_score = input()
match3_score = input()
match4_score = input()
match5_score = input()
match6_score = input()

# خواندن نتایج بازی‌ها
matches = [
    {"team1": "Iran", "team2": "Spain", "score": match1_score},
    {"team1": "Iran", "team2": "Portugal", "score": match2_score},
    {"team1": "Iran", "team2": "Morocco", "score": match3_score},
    {"team1": "Spain", "team2": "Portugal", "score": match4_score},
    {"team1": "Spain", "team2": "Morocco", "score": match5_score},
    {"team1": "Portugal", "team2": "Morocco", "score": match6_score},
]

for match in matches:
    team1 = match["team1"]
    team2 = match["team2"]
    score = match["score"].split("-")
    goal1 = int(score[0])
    goal2 = int(score[1])
    goal_diff = goal1 - goal2
    if goal_diff > 0:
        update_results(team1, goal_diff, 3)
        update_results(team2, -goal_diff, 0)
    elif goal_diff < 0:
        update_results(team1, goal_diff, 0)
        update_results(team2, -goal_diff, 3)
    else:
        update_results(team1, goal_diff, 1)
        update_results(team2, -goal_diff, 1)

# چاپ نتایج به ترتیب امتیاز
sorted_results = sorted(results.items(), key=lambda x: (-x[1][3], -x[1][0], x[0]))
for team, stats in sorted_results:
    print(
        f"{team}  wins:{stats[0]} , loses:{stats[1]} , draws:{3-stats[0]-stats[1]} , goal difference:{stats[2]} , points:{stats[3]}"
    )