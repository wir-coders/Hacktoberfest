def reverse(s): 
  string = "" 
  for i in s: 
    string = i + string
  return string
  
s = "I am Moksha"
  
print ("Original string : ",end="") 
print (s) 
  
print ("Reversed string : ",end="") 
print (reverse(s)) 