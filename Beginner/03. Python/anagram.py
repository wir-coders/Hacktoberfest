def check(s1, s2): 
      
    # the sorted strings are checked  
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")          
          
s1 =input("enter first string eg listen \n")
s2 =input("enter second string eg silent \n")
check(s1, s2) 