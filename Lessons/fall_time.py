# Find seconds to drop from a height on some planets.
import constants
import math

height = int(input('Height in meters: '))  # Meters from planet

if __name__ == '__main__':
    print(f'Earth time to impact: {math.sqrt(2 * height / constants.earth_g):.2f} seconds')
    print(f'Mars time to impact: {math.sqrt(2 * height / constants.mars_g):.2f} seconds')