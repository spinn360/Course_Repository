import math
#calculate savings over years
base = float(input('Enter initial savings: '))
print()

rate = float(input('Enter annual interest % rate: '))
print()

years = int(input('Enter years that pass: '))
print()

total = base * math.pow(1 + (rate / 100), years)

print (f'Savings after {years} years is ${total:.2f}')

# other functions in math
# Number representation and theoretic functions
# ceil(x)	Round-up value		fabs(x)	Absolute value
# factorial(x)	factorial (3! = 3 * 2 * 1)		floor(x)	Round-down value
# fmod(x, y)	Remainder of division		fsum(x)	Floating-point sum of a range, list, or array.
# Power, exponential, and logarithmic functions
# exp(x)	Exponential function ex		log(x, (base))	Natural logarithm; base is optional
# pow(x, y)	Raise x to power y		sqrt(x)	Square root
# Trigonometric functions
# acos(x)	Arc cosine		asin(x)	Arc sine
# atan(x)	Arc tangent		atan2(y, x)	Arc tangent with two parameters
# cos(x)	Cosine		sin(x)	Sine
# hypot(x1, x2, x3, ..., xn)	Length of vector from origin		degrees(x)	Convert from radians to degrees
# radians(x)	Convert degrees to radians		tan(x)	Tangent
# cosh(x)	Hyperbolic cosine		sinh(x)	Hyperbolic sine
# Complex number functions
# gamma(x)	Gamma function		erf(x)	Error function
# Mathematical constants
# pi (constant)	Mathematical constant 3.141592...		e (constant)	Mathematical constant 2.718281...