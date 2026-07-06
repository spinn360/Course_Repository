# is and is not are for evaluating if objects are the same object
# it does not compare values so much as if both variables are pointing
# to the same object not same value


w = 500
x = 500 + 500  # Create a new object with value 1000
y = w + w      # Create a second object with value 1000
z = x          # Bind z to the same object as x

if z is x:
    print('z and x are bound to the same object')
if z is not y:
    print('z and y are NOT bound to the same object')