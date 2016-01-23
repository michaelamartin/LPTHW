def top_bottom(upper_bound, step):

    numbers = [ ]
    
    for i in range(0,upper_bound,step):
        print "At the top i is %d" % i
        numbers.append(i)
    
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    
    print "The numbers: "

    for num in numbers:
        print num
        
        
print    "Please enter a positive integer you would like to set as your upper bound: "
upper_bound= int(raw_input("> "))

print "Please enter a positive increment: "
step = int(raw_input("> "))

top_bottom(upper_bound, step)
