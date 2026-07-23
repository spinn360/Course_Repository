exam1_grade = float(input("Enter score on Exam 1 (out of 50): "))
exam2_grade = float(input("Enter score on Exam 2 (out of 50): "))
exam3_grade = float(input("Enter score on Exam 3 (out of 75): "))
exam4_grade = float(input('Enter score on Exam 4 (out of 75): '))
exam1_grade /= 50 * 100
exam2_grade /= 50 * 100
exam3_grade /= 75 * 100
exam4_grade /= 75 * 100

overall_grade = (exam1_grade + exam2_grade + exam3_grade + exam4_grade) / 4 *10000

print(f"Your overall grade is: {overall_grade} percent")