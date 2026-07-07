par = int(input('Enter par: '))
strokes = int(input('Enter strokes: '))

if (strokes + 2) == par:
    print(f'Par {par} in {strokes} strokes is Eagle')
if (strokes + 1) == par:
    print(f'Par {par} in {strokes} strokes is Birdie')
if strokes == par:
    print(f'Par {par} in {strokes} strokes is Par')
if (strokes - 1) == par:
    print(f'Par {par} in {strokes} strokes is Bogey')
if (strokes >= (par + 2)):
    print(f'Par {par} in {strokes} strokes is Error')

    # better coding

if par not in (3, 4, 5):
    print(f'Par {par} in {strokes} strokes is Error')
elif strokes == par - 2:
    print(f'Par {par} in {strokes} strokes is Eagle')
elif strokes == par - 1:
    print(f'Par {par} in {strokes} strokes is Birdie')
elif strokes == par:
    print(f'Par {par} in {strokes} strokes is Par')
elif strokes == par + 1:
    print(f'Par {par} in {strokes} strokes is Bogey')
else:
    print(f'Par {par} in {strokes} strokes is Error')