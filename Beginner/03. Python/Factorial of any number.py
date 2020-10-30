f=1
ui=int(input("enter the number to get factorial : "))
for x in range(1,ui+1):
    f= f*x
print("factoral of ",ui ," is ",f)


//adding another method of finding factorial using recursion//
def factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  
# take input from the user  
n = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(n)) 
#end of code.
