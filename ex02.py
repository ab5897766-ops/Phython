#25
keys = "alpha bravo charlie delta echo foxtrot"
values = "30 40 50 60 70 80"

#26
park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

#27
kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

#28
lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

if 'english' in lee:
    del lee['english']

print(lee)

#29
lim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

for subject, score in lim.items():
    print(subject, score)

#30
choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

high_scores = {subject: score for subject, score in choi.items() if score >= 90}
print(high_scores.keys())

#31
yoo = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

average = sum(yoo.values()) / len(yoo)
print(f"평균 점수는 {average:.2f}점입니다.")