parts = ["Battery", "16GB RAM", "512GB SSD", "Keyboard", "Screen Panel"]

try:
    index = int(input())
    print(f'{parts[index]}')
except:
    print('Error')