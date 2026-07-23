word = input()
password = ''

for passw in word:
    if passw == 'i':
        password += '1'
    elif passw == 'a':
        password += '@'
    elif passw == 'm':
        password += 'M'
    elif passw == 'B':
        password += '8'
    elif passw == 's':
        password += '$'
    else:
        # If it doesn't match any of the above, add the normal character
        password += passw 

# Add the exclamation point to the very end of the completed string
password += '!'

print(password)