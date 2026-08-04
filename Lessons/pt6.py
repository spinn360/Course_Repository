def is_in_list(a):
    if a in predef_list:
        return True
    else:
        return False



predef_list = [4, -27, 15, 33, -10]

#solution accepts an integer input
#solution outputs Boolean value indicating whether integer input is in predef_list

#accept integer input
print("Enter the number to check for in the list:")

#define function to compare input with list values

    



#output desired statement based on is_in_list() function
if __name__ == '__main__':
    user_input = int(input())
    print(f"Is the input present in the list? {is_in_list(user_input)}")
    