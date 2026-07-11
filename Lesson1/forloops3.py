num_input = int(input())
customer_list = []
for i in range(num_input):
    customer_list.append(input())

print(f'List has {num_input} elements:')

for cust in reversed(customer_list):
    print(f'({cust}) and ', end="")