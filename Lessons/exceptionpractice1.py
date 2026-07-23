class JustNotCoolError(Exception):
    pass

x =2 
try:
    raise JustNotCoolError("this just isn't cool man")
    #raise Exception('I am a custom exception') #custom exception
    #print(x /0)
    #if not type(x) is str:
    #    raise TypeError('Only strings are allowed')
except NameError:
    print('there is a name error, so something is probably undefined')
except ZeroDivisionError:
    print("You can't divide by zero homie!!")
except Exception as error:
    print(error)
else:
    print('no errors!')
finally:
    print('I am going to print no matter error or not')