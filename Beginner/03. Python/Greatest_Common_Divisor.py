# Uses python3
# Greatest Common Divisior
# Enter two numbers to get the Greatest Common Divisior

import sys
def gcd_naive(a, b):
	if  b == 0:
		return a
	else:
		return	gcd_naive(b%a,a)	

if __name__ == "__main__":
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
