# Uses python3
# Greatest Common Divisior
# Enter two numbers to get the Greatest Common Divisior

import sys
def gcd_naive(a, b):
	if a==0:
		return b
	elif  b == 0:
		return a
	else:
		return	gcd_naive(b%a,a)	

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
