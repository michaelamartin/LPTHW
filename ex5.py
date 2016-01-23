name = 'Zed A. Shaw'
age = 35 # not a lie
height_in = 74 # inches
height_cm = 2.54*height_in #cm
weight_lb = 180 # lbs
weight_kg = weight_lb/2.2 #kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height_cm
print "He's %d kilograms heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %f, and %f I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)
