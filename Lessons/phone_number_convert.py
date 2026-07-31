number = int(input())
prefix = number // 10000000
if prefix < 100:
    prefix = '0'+str(prefix)
#print(prefix)
first3 = number % 10000000 // 10000
#print(first3)
last4 = number % 10000
#print(last4)
print(f'({prefix}) {first3}-{last4}')

# or easier and better way

phone_number = input()
print(f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}")