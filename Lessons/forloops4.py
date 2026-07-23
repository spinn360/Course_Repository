student_dict = {
    'Van': 'V1',
    'Nia': 'K17',
    'Jeb': 'G20',
    'Pam': 'Q14'
}

student_name = input()
seat_code = input()
student_dict[student_name] = seat_code

for student in student_dict:
    print(f'{student} is in seat {student_dict[student]}')