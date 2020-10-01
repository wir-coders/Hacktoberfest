from datetime import *
'''to find age of a person'''
try:
	day=int(input("enter day as number "))
	month=int(input("enter month as number (Eg: 1-for Jan 2-for feb) "))
	year=int(input("enter year Eg-2004,2018 "))

	dob=date(year,month,day)
	print(dob)

	today=datetime.now().date()
	age=(today-dob)/timedelta(days=365.24)
	print(round(age,2))
except ValueError as e:
	print("dob issue ",e)