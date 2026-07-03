exam1_grade = float(input("Enter score on Exam 1 (out of 100): "))
exam2_grade = float(input("Enter score on Exam 2 (out of 100): "))
exam3_grade = float(input("Enter score on Exam 3 (out of 100): "))
exam4_grade = float(input('Enter score on Exam 4 (out of 50): '))
exam5_grade = float(input('Enter score on Exam 4 (out of 50): '))
exam6_grade = float(input('Enter score on Exam 4 (out of 50): '))
exam7_grade = float(input('Enter score on Exam 4 (out of 50): '))



per60Grade = (exam1_grade + exam2_grade + exam3_grade) / 3
per40Grade = (exam4_grade + exam5_grade + exam6_grade + exam7_grade) /2
# print(f' 60: {per60Grade}')
# print(f' 60: {per40Grade}')
# print(f'60 math = {0.6 * per60Grade}')
# print(f'40 math = {0.4 * per40Grade}')
overall_grade = ((0.6 * per60Grade) + (0.4 * per40Grade))

print(f"Your overall grade is: {overall_grade} percent")