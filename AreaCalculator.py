# Calculator that can compute the area of the circle and the triangle

from math import pi

print "Let's start!"
option = raw_input("What figure do you want to calculate? Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == "C" :
	radius = float(raw_input("Enter the radius of the circle: "))
	area = pi * radius**2
	print "The radius of the circle is: %s" % (area)

elif option == "T" :
	base = float(raw_input("Enter the base of the triangle: "))
	height = float(raw_input("Enter the height of the triangle: "))
	area = 0.5 * base * height
	print "The area of the triangle is: %s" % (area)
  
else:
	print "Your input is invalid. Try again"

print "FIN"
