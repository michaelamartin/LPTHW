def top_bottom(variable, step):

    i = 0
    numbers = [ ]

    while i < variable:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    
    print "The numbers: "

    for num in numbers:
        print num
 
print    "Please enter a positive integer you would like to set as your range: "
variable = int(raw_input("> "))

print "Please enter a positive increment for the numbers in your range: "
step = int(raw_input("> "))
top_bottom(variable, step)
