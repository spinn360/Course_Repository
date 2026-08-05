'''
Challenge 1: 
Unit ConversionsBased on: Converting 
a total number of ounces into tons, pounds, and 
remaining ounces using floor division (//) and 
modulo (%) operators.  Your Task:Write a script 
that accepts an integer representing a total 
number of inches. Convert that total into miles, 
yards, feet, and remaining inches.There are 12 
inches in a foot.There are 3 feet in a yard.
There are 1760 yards in a mile.
Output the converted miles, yards, feet, and inches.
'''
total_inches = int(input())
mile = total_inches // 12 // 3 // 1760
remaining_inches = total_inches % (12 * 3 * 1760)
yard = remaining_inches // 12 // 3
remaining_inches = remaining_inches % (12 * 3)
foot = remaining_inches // 12
remaining_inches = remaining_inches % 12
inches = remaining_inches
print(f'Miles {mile}\nYards {yard}\nFeet {foot}\nInches {inches}')