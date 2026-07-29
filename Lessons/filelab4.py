file_name = input()

mid1_total = 0
mid2_total = 0
final_total = 0
num_students = 0
# open the file and read each line into a lis
with open(file_name, 'r') as f_in, open('report.txt', 'w') as f_out:
    for line in f_in:
        data = line.strip().split('\t')
        last_name = data[0]
        first_name = data[1]
        midterm1 = int(data[2])
        midterm2 = int(data[3])
        final = int(data[4])

        avg = (midterm1 + midterm2 + final) / 3

        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        else:
            grade = 'F'

        #f_out.write(f'{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{avg}\t{grade}\n')
        f_out.write(f'{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{grade}\n')
        mid1_total += midterm1
        mid2_total += midterm2
        final_total += final
        num_students += 1

    mid1_avg = mid1_total / num_students
    mid2_avg = mid2_total / num_students
    final_avg = final_total / num_students

    f_out.write(f'\nAverages: midterm1 {mid1_avg:.2f}, midterm2 {mid2_avg:.2f}, final {final_avg:.2f}\n')


