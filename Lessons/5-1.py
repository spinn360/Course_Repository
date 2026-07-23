c_meters_per_sec = 299792458  # Speed of light (m/s)
joules_per_AA_battery = 4320.5  # Nickel-Cadmium AA batteries
joules_per_TNT_ton = 4.184e9

#Read in a floating-point number from the user
print('Enter Mass in kg:')
mass_kg = float(input())

#Compute E = mc^2.
energy_joules = mass_kg * (c_meters_per_sec**2)  # E = mc^2
print('Total energy released:', energy_joules, 'Joules')

#Calculate equivalent number of AA and tons of TNT.
num_AA_batteries = energy_joules / joules_per_AA_battery
num_TNT_tons = energy_joules / joules_per_TNT_ton

print('Which is as much energy as:')
print('  ', num_AA_batteries, 'AA batteries')
print('  ', num_TNT_tons, 'tons of TNT')



miles = float(input('Enter a distance in miles: '))
hours_to_fly = miles / 500.0
hours_to_drive = miles / 60.0

print(miles, 'miles would take:')
print(hours_to_fly, 'hours to fly')
print(hours_to_drive, 'hours to drive')


u = float(input('Enter polynomial number: '))
t= (4.5*u * u) -(8.5 *u) -9.5

print(f'{t:.3f}')

# Assign wall_area with a float read from input
wall_area = float(input('Enter Wall Area size: '))

# Compute num_gallons
num_gallons = wall_area / 350.0

print(f'{num_gallons:.5f} Gallons of paint required')



object_mass = float(input('Enter object mass: '))
object_velocity = float(input('Enter object velocity: '))
kinetic_energy = 1/2 * object_mass * object_velocity * object_velocity

print(f'Kinetic Energy is {kinetic_energy}')

age_years = float(input('Enter your age: '))
weight_pounds = float(input('Enter your weight: '))
heart_bpm = float(input('Enter heart BPM: '))
time_minutes = float(input('Enter length of time in minutes: '))
sex = input('m for male, f for female: ')

# don't know how to do if sex is 'm' or 'f' yet:
calories_man = ( (age_years * 0.2017) + (weight_pounds * 0.09036) + (heart_bpm * 0.6309) - 55.0969 ) * time_minutes / 4.184

calories_woman = ( (age_years * 0.074) - (weight_pounds * 0.05741) + (heart_bpm * 0.4472) - 20.4022 ) * time_minutes/ 4.184

print(f'A man burns {calories_man}')
print(f'A female burns {calories_woman}')
