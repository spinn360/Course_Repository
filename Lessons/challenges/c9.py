#solution accepts an integer input representing the number of stock selections
#solution accepts string inputs equivalent to the integer input identifying the stock selections
#solution outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places

models = {'Suno v3': 10.50, 'Suno v3.5': 15.00, 'MusicGen': 5.25, 'Udio': 12.00}
num = int(input('Enter number of stocks to choose: '))
total_price = 0
i = 0
while i < num:
    print("Enter the name of stock model you want to buy")
    item = input()
    i += 1
    if item in models:
        total_price = total_price + models[item]
print(f"Final price: ${total_price:.2f}")
