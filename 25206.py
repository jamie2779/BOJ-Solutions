import sys

lines = sys.stdin.readlines()

total_time = 0
total_score = 0
scores = ['F','','D0','D+','C0','C+','B0','B+','A0','A+']
for line in lines:
    _, time, score = line.split()
    if score != 'P':
        total_time += float(time)
        total_score += 0.5*scores.index(score) * float(time)

print(total_score/total_time)