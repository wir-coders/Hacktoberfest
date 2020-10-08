"""
 Function to print Fibonnaci series of a number
 [Language used] - Python
 Author: Carolini28
"""

previous_ = 0
next_ = 0 

n =int( input(" How many terms do you want? :"))

while(next_ < n):
  print(next_)
  next_ = next_ + previous_
  previous_ = next_ - previous_
  if(next_ == 0):
    next_ = next_ + 1