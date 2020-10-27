"""
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. 
Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.
In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to 
ship that package using Sal’s Shippers.
Sal’s Shippers has several different options for a customer to ship their package. 
They have ground shipping, which is a small flat charge plus a rate based on the weight of your package.
Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. 
They recently also implemented drone shipping, which has no flat charge, but the rate based on weight 
is triple the rate of ground shipping.
Write a program that asks the user for the weight of their package and then tells them 
which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.
"""

def cost_ground_shipping(weight):
  if weight<=2:
    return weight*1.50+20.00
  elif weight>2 and weight<=6 :
    return weight*3.00+20
  elif weight>6 and weight<=10:
    return weight*4.00+20.00
  elif weight>10:
    return weight*4.75+20
  
x=cost_ground_shipping(8.4)
print(x)

premium_ground_shipping=125

def cost_drone_shipping(weight):
  if weight<=2:
    return weight*4.50
  elif weight>2 and weight<=6 :
    return weight*9.00
  elif weight>6 and weight<=10:
    return weight*12.00
  elif weight>10:
    return weight*14.25

y=cost_drone_shipping(1.5)
print(y)

def cheapest_shipping_method(weight):
  ground=cost_ground_shipping(weight)
  premium=premium_ground_shipping
  drone=cost_drone_shipping(weight)

  if ground<premium and ground<drone:
    method="Standard Ground"
    cost=ground

  elif premium<ground and premium<drone:
    method="Premium Ground"
    cost=premium

  else:
    method="Drone"
    cost=drone
  
  print(" The cheapest option is %.2f with %s shipping." %(cost,method))

   

cheapest_shipping_method(4.8)
cheapest_shipping_method(41.5)