import math
from decimal import *

getcontext().prec = 26

def factorial(n):
	if n<2:
		return 1
	else:
		return n*factorial(n-1)

def bailey_borwein_plouffe(n):
	sum = Decimal(0)
	for i in range(n):
		sum += (Decimal(1)/(16**i))*((Decimal(4)/(8*i+1))-(Decimal(2)/(8*i+4))-(Decimal(1)/(8*i+5))-(Decimal(1)/(8*i+6)))
	return sum

def bellard(n):
	sum = Decimal(0)
	for i in range(n):
		sum += ((Decimal(-1)**i)/(1024**i)) * ((Decimal(-32)/(4*i+1))-(Decimal(1)/(4*i+3))+(Decimal(256)/(10*i+1))-(Decimal(64)/(10*i+3))-(Decimal(4)/(10*i+5))-(Decimal(4)/(10*i+7))+(Decimal(1)/(10*i+9)))
	sum*= Decimal(1)/64
	return sum


def chudnovsky(n):
	sum = Decimal(0)
	for i in range(n):
		sum +=  (Decimal(-1)**i)*(Decimal(factorial(6*i))/((factorial(i)**3)*(factorial(3*i)))* (13591409+545140134*i)/(640320**(3*i)))
	sum *= Decimal(10005).sqrt()/4270934400
	sum = sum**-1
	return sum
x = Decimal('3.141592653589793238462643')
print('\t\t\t bailey_borwein_plouffe\t\t\tbellard\t\t\t      chudnovsky')
for i in range(1,21):
	print('Iteration number - {:2}  {:26.24f}    {:27.24f}     {:26.24f}'.format(i,bailey_borwein_plouffe(i),bellard(i),chudnovsky(i)))
	print('Inaccuracy -           {:24.24f}     {:26.24f}     {:26.24f}'.format(x - bailey_borwein_plouffe(i), x - bellard(i), x - chudnovsky(i)))