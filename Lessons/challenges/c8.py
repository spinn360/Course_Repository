def is_in_list(a, b):
    if a in b:
        return True
    else:
        return False
def check_anime(a):
    if a in anime:  
        return True
    else:
        return False


anime = ['Akira', 'Boku no Hero Academia', 'Cowboy Bebop', 'Dragon Ball Z', 'Eyeshield 21']


if __name__ == "__main__":
    print('Enter the name of an anime:')
    name = input()
    #print(f"{is_in_list(name, anime)}")
    print(f"{check_anime(name)}")
