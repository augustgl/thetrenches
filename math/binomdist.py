# 2/2/2021
# stats class

import math

def factorial(n):
	fact = 1
	for i in range(1, n+1):
		fact = fact * i 

	return fact

def findq(p):
	return 1 - p
	
def binomdist(n, p):
	print
	for x in range(1, n + 1):
		numerator = factorial(int(n))
		denominator = factorial(int(x)) * factorial(int(n) - int(x))
		fraction = numerator / denominator

		q = findq(p)

		secondhalf = pow(p, x) * pow(q, (n - x))
		final = fraction * secondhalf

		print str(final)
		print 
		print "[+] MEAN " + str(n * p)
		print
		print "[+] VARIANCE " + str(n * p * q)
		print
		print "[+] STANDARD DEVIATION " + str(math.sqrt((n * p * q)))
		print

def main():
	binomdist(6, .85)

main()
