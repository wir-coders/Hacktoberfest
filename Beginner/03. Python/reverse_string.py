def reverse(s): 
  s1 = "" 
  for i in s: 
    s1 = i + s1
  return s1
  
s = "I am Moksha"
  
print ("Original string : ",end="") 
print (s) 
  
print ("Reversed string : ",end="") 
print (reverse(s)) 
