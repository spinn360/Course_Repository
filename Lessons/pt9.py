stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

#solution accepts an integer input representing the number of stock selections
#solution accepts string inputs equivalent to the integer input identifying the stock selections
#solution outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places

# input 
print("Enter a quantity of stocks followed by stock symbol(s):")
num_items = int(input())
i = 0
stock_value = 0
while i < num_items:
    key = input()
    i +=1
    if key in stocks:
        stock_value += stocks[key]

# loop and calculations
print(f"Total price: ${stock_value:.2f}")