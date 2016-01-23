#Defining variables x and y
x = "There are %d types of people." %10

#Defining the binary and do_not variables
binary = "binary"
do_not = "don't"

#Defining the y variable with binary and do_not as string inputs
y = "Those who know %s and those who %s." % (binary, do_not)

#Printing variables x and y
print x
print y

#Printing strings referencing formatted variables x and y
print "I said: %r." % x
print "I also said: '%s'." % y

#Defining the hilarious and joke_evaluation varibles
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Printing joke_evaluation with formated variable hilarious
print joke_evaluation % hilarious

#Defining w and e variables
w = "This is the left side of..."
e = "a string with a right side."

#Concatenating strings w and e
print w + e
