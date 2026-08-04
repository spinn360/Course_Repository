#temperature >= 212, water state is "Boiling"
#temperature (115, 211], water state is "Hot"
#temperature [80, 115], water state is "Warm"
#temperature [33, 80), water state is "Cold"
#temperature < 33, water state is "Frozen"
#temperature = 212, safety comment "Caution: Hot!"
#temperature < 33, safety comment "Watch out for ice!"
#solution accepts integer input representing a water temperature
#solution outputs the water state and potential safety comment based on temperature

print("Enter the water temperature:")
temperature = int(input())
water_state = ''
optional_safety_comment = ''
if temperature >= 212:
    water_state = 'Boiling'
    if temperature == 212:
        optional_safety_comment = 'Caution: Hot!'
elif temperature >= 115:
    water_state = 'Hot'
elif temperature >= 80:
    water_state = 'Warm' 
elif temperature >= 33:
    water_state ='Cold'
elif temperature < 33:
    water_state = 'Frozen'
    optional_safety_comment = 'Watch out for ice!'

print(water_state)
if optional_safety_comment != '':
    print(optional_safety_comment)


#determine water state and safety comment