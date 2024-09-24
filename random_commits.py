import os
import random
import subprocess
from datetime import datetime, timedelta

REPO_PATH = os.getcwd()
FILE_NAME = "activity.txt"
TOTAL_DAYS = 111  # кількість унікальних дат
MAX_COMMITS_PER_DAY = 5  # максимум комітів на один день
START_DATE = datetime(2024, 9, 22)
END_DATE = datetime.now()

os.chdir(REPO_PATH)

dates = set()
while len(dates) < TOTAL_DAYS:
    delta = END_DATE - START_DATE
    rand_day = random.randrange(delta.days)
    date = START_DATE + timedelta(days=rand_day)
    dates.add(date)

for date in sorted(dates):
    commits_count = random.randint(1, MAX_COMMITS_PER_DAY)
    date_str = date.strftime('%Y-%m-%dT%H:%M:%S')
    for i in range(commits_count):
        with open(FILE_NAME, "a") as f:
            f.write(f"Commit {i+1} on {date_str}\n")
        subprocess.run(['git', 'add', FILE_NAME])
        subprocess.run(['git', 'commit', '-m', f'Commit {i+1} on {date_str}', '--date', date_str])

print("Коміти створено, виконай git push.")
