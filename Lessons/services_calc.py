services = { 
            'Air freshener' : 1 ,
            'Rain repellent': 2,
            'Tire shine' : 2,
            'Wax' : 3,
            'Vacuum' : 5 
            }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

cost1 = services.get(service_choice1, 0)
cost2 = services.get(service_choice2, 0)
total = base_wash + cost1 + cost2

print('ZyCar Wash')
print('Base car wash - $10')

if service_choice1 != '-':
    if service_choice1 in services:
        print(f'{service_choice1} - ${cost1}')
if service_choice2 != '-':
    if service_choice2 in services:
        print(f'{service_choice2} - ${cost2}')
print('------')

print(f'Total price: ${total}')
