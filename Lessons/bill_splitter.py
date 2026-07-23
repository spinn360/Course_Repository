running_total = 0

num_of_friends = int(input('Enter number to split bill with: '))

appetizers = float(input('Cost of Appetizers: '))
main_courses = float(input('Cost of Main courses: '))
desserts = float(input('Cost of Desserts: '))
drinks = float(input('Cost of drinks: '))

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)
tip_percent = int(input('Enter tip percentage: '))
tip = running_total * (tip_percent / 100)
print('Tip amount:', round(tip, 2))

running_total += tip
print('Total with tip:', round(running_total, 2))

final_bill = running_total / num_of_friends
#print('Bill per person:', final_bill)

each_pays = round(final_bill,2)
print(f'Each person pays: {each_pays}')