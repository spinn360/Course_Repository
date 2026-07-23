patients_list = input().split()

''' Your code goes here '''
backup_data = patients_list[:]
selected_patients = patients_list[1::3]
patients_list.clear()
print(f'Backup list of patients: {backup_data}')
print(f'Selected list of patients: {selected_patients}')