
grade = float(input('Enter your current grade percentage before final: '))
fin_weight = float(input('How much of your grade does the final make up: '))
target_overall = float(input('What is your overall desired goal percentage: '))


max_final_score = 100
final_weight = fin_weight *.01
current_weight = (100 - fin_weight) * .01
percent = (target_overall - (grade * current_weight)) / final_weight



points_from_final = max_final_score * final_weight
points_needed_from_current = target_overall - points_from_final
min_current_grade = points_needed_from_current / current_weight

if percent <= 0:
    print(f'Congratulations! you already have a {target_overall}% locked in, even if you get a 0% on the final')
elif grade >= min_current_grade:
    print(f'You must score at least a {percent:.1f}% on the final\nto get a {target_overall}% in the class')
else:
    print(f'The absolute lowest current grade you can have \nand still get a {target_overall}% overall,\nis {min_current_grade:.2f}%')

