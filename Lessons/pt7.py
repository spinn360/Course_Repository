frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input

#try-block to determine value
try:
    print("Enter the index of the element that you want to extract from the list:")  
    index = int(input())              #accept integer input
    print(frameworks[index])
except:
    print("Error")
  