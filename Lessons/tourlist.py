num_lines = int(input())
tour_lists = []
for row_index in range(num_lines):
    tour_lists.append(input().split())

for pos, places in enumerate(tour_lists):
    print(f'Places visited in tour {pos +1}:')
    for place in places:
        print(place, end=' ')
    print()
    