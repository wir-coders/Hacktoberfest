def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s = "I am Moksha"
  
print ("Original string : ",end="") 
print (s) 
  
print ("Reversed string : ",end="") 
print (reverse(s)) 