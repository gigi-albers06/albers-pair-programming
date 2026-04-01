# FEET TO METERS HOORAY
feet = int(input("Please enter a number (feet): "))
inches = int(input("Please enter a number (inches): "))/12 #converts inches to feet

feetinch = feet + inches #combining the feet and inches values
meter = feetinch/3.281  #converting to meters

print("Height in feet:", feetinch) #prints values
print("Meter value:", meter)