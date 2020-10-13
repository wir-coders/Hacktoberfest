"""
	Algorithm to check Prime number
	[Language used] - Python 
	Author: Phanatagama
"""

number = int(input('Input a Number: '))  
# If given number is greater than 1 
if number > 1: 
   # Iterate from 2 to n / 2  
   for i in range(2, number): 
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (number % i) == 0: 
           print(f"{number} is not a prime number") 
           break
   else: 
       print(f"{number} is a prime number") 
else: 
   print(f"{number} is not a prime number") 