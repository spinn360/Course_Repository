
music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

# Get user input

# While user input != 'exit'
    # ....
user_input = input()
while user_input != 'exit':
    if user_input in music:
        
        for album in music[user_input]:
            songs = music[user_input][album]['songs']
            year = music[user_input][album]['year']
            plat = music[user_input][album]['platinum']
            
            print(f'Album: {album}')
            
            for sngs, title in enumerate(songs):
                print(f'Songs {sngs}: {title}')
        
            print(f'Year: {year}')
            print(f'Platinum: {plat}')
    user_input = input()