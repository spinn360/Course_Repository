tours_data = []
for token in input().split():
	tours_data.append(int(token))

''' Your code goes here '''
slice_size = len(tours_data) // 4
spring_tours = tours_data[0:slice_size]
summer_tours = tours_data[slice_size:2 * slice_size]
fall_tours = tours_data[2 * slice_size:3 * slice_size]
winter_tours = tours_data[(3 * slice_size):]

print(f'Number of tour dates in each season: {slice_size}')
print(f'All year tours: {tours_data}')
print(f'Spring tours: {spring_tours}')
print(f'Summer tours: {summer_tours}')
print(f'Fall tours: {fall_tours}')
print(f'Winter tours: {winter_tours}')