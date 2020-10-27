n=int(input("Enter any Number: "))
f= lambda n: n*f(n-1) if n>0 else 1
s=f(n)
print(s)