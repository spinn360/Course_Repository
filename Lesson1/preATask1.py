empa = 15.62
empb = 41.85
empc = 32.67

inp1 = 3
inp2 = 10
inp3 = 5

def miles_per_employee(a,b):
    return a * b

def total_miles_all_emp(a,b,c):
    return a + b + c
emp1_total = miles_per_employee(empa, inp1)
emp2_total = miles_per_employee(empb, inp2)
emp3_total = miles_per_employee(empc, inp3)

total = total_miles_all_emp(emp1_total, emp2_total, emp3_total)
print(f'Distance: {total} miles')