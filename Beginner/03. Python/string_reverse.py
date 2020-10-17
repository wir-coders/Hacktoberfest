def strreverse(s): 
	if len(s) == 0: 
		return s 
	else: 
		return strreverse(s[1:]) + s[0] 

s = "Mustafa"

print ("original: ",end="") 
print (s) 

print ("reversed: ",end="") 
print (strreverse(s)) 
