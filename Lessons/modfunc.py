import modtst as mod

user_input = input()
if type(user_input) != int:
    try:
        print(mod.getstr(user_input))
    except:
        print('some bug occured')
try:
    user_input = int(user_input)
except:
    print("couldn't make a number default of 7 instead")
if type(user_input) != int:
    user_input = 7
try:
    print(mod.getsub(user_input))
    print(mod.getadd(user_input))
    print(mod.getmult(user_input))
    
except ValueError as e:
    print('incorrect value',e)
except SyntaxError:
    print('syntax error')   
except ZeroDivisionError:
    print("one cannot divide by nothing")
except:
    print('some error')