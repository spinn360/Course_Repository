#solution accepts a 9-digit integer representing an unformatted student identification number (e.g.,"5417543010")
#solution outputs formatted student identification number as a string (e.g.,"541-75-3010")
#accept integer input
print("Enter Student Identification Number:")
identification_number = int(input())
strid = str(identification_number)
stridM = strid[0:3] +'-'+strid[3:5] +'-'+ strid[-4:]
print(stridM)