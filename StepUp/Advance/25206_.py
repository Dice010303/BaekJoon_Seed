# 너의 평점은
# 전공평점 = 전공과목별 (학점 * 과목평점) / 학점의 총합
# 등급에 따른 과목평점
# A+ 4.5
# A0 4.0
# B+ 3.5
# B0 3
# C+ 2.5
# C0 2.0
# D+ 1.5
# D0 1.0
# F  0.0
# P/F 과목의 경우 등급이 P 또는 F로 표시되는데 , 등급이 P인 과목은 계산에서 제외
# 입력 - 20줄애 걸쳐 수강한 전공과목의 과목명, 학점 , 등급이 공백으로 주어짐
rank_dict ={
    'P': 0,
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}
total = 0
total_score = 0
grade = 0

for i in range(20):
    subject, score, rank = input().split()
    if rank == "P" : # P일 경우에는 계산값에서 제외 -> 반복문 pass
        continue
    total += float(score) * rank_dict[rank]
    total_score += float(score)

grade = round(total / total_score,6)

print(grade)
