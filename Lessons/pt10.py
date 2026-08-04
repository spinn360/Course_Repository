purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase

print("Enter the item to purchase:")
item = input()
print("Enter the quantity of that item:")
quantity = int(input())
item_val = purchase[item]

'''If fewer than 10 items are purchased, the price is the full cost per item.
If between 10 and 20 items (inclusive) are purchased, the purchase gets a 5% discount.
If 21 or more items are purchased, the purchase gets a 10% discount.'''
if quantity < 10:
    if item in purchase:
        print(f"{quantity} {item} total cost: ${item_val * quantity:.2f}")
elif 10 <= quantity <= 20:
    if item in purchase:
         print(f"{quantity} {item} total cost: ${(item_val* quantity) * 0.95:.2f}")
elif quantity >= 21:
    if item in purchase:
         print(f"{quantity} {item} total cost: ${(item_val* quantity) * 0.90:.2f}")