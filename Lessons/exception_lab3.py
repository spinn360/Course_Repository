'''Given a list of 10 names, complete the program that outputs the name specified by the list 
index entered by the user. Use a try block to output the name and an except block to catch 
any IndexError exception as a variable. Output "Exception! " followed by the message from 
the exception variable. Output also the first element in the list if the invalid index is 
negative or the last element if the invalid index is positive.

Note: Python allows using a negative index to access a list, as long as the magnitude of the index is smaller than the size of the list.'''

names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

# Type your code here.
try:
    print('Name:',names[index])
except IndexError as e:
    print("Exception! " + str(e))
    if index < 0:
        print('The closest name is:',names[0])
    else:
        print('The closest name is:',names[-1])
# Type your code here.