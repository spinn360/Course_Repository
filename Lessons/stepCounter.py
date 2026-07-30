# Define your method here
def steps_to_miles(steps):
    if steps < 0:
        raise ValueError('Exception: Negative step count entered')
    return steps / 2000

if __name__ == '__main__':
    try:
        steps = int(input())
        print(f'{steps_to_miles(steps):.2f}')
    except ValueError as ve:
        print(ve)

    # Type your code here.