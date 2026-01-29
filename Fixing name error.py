def calculate_sum(a, b):
    total = a + b
    return total

x = 5
y = 10
w = 4 # w was not defined in the original code which made the error occur 
z = calculate_sum(x, w)
print(z)
