'''
Challenge 3: 
Mathematical FormulasBased on: Accepting three inputs 
to calculate the area of a trapezoid using a specific 
mathematical formula.  Your Task:Write a script that 
accepts three integer values representing the length 
($l$), width ($w$), and height ($h$) of a cave chamber. 
Calculate and output the volume of the chamber in cubic 
meters using the formula $V = l \times w \times h$.
'''
length = int(input('Enter length of cave chamber in meters: '))
width = int(input('Enter width of cave chamber in meters: '))
height = int(input('Enter height of cave chamber in meters: '))

volume = length * width * height
print(f'Volume of the cave chamber: {volume} cubic meters')

