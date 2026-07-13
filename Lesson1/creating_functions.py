def calc_pizza_area():
    pi_val = 3.14159265

    pizza_diameter = 12.0
    pizza_radius = pizza_diameter / 2.0
    pizza_area = pi_val * pizza_radius * pizza_radius
    return pizza_area

print(f'{12:.1f} inch pizza is {calc_pizza_area():.3f} square inches')

def get_face():
   face_char = 'o   o\n  o\nooooo'
   return face_char
	
print('Say cheese!')
	
print(get_face())
	
print('Did it turn out ok?')


def compute_square(num_to_square):
    return num_to_square * num_to_square


num_squared = compute_square(7)

print(f'7 squared is {num_squared}')