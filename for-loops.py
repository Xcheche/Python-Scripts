# for i in range(1,20,2):
#     print('i',i)

student_score = [10,14,15,16,17,18,19,20,45,60,70,80,90,100]
scores_above_40 = []


for scores in student_score:
    if scores>=40:
        scores_above_40.append(scores)
        print('Scores above 40',scores_above_40)