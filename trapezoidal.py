# Trapezoidal Rule of Integration #

def f(x):
	return 10 - x ** 2
	
a = float(input("Enter the starting point of the interval: "))
b = float(input("Enter the ending point of the interval: "))
n = int(input("Enter the number of points at which you want to calculate: "))

h=(b-a)/n

A = (f(a)+f(b))*h/2

for i in range(n):
	A += h*f(a+i*h)

print(A)
