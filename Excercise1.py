# Excercise 1
print ("Welcome!")
print ("Welcome!")
print ("Three times three plus six is", 3*3+6)
print ("What is 8 times 8?\n", 8*8)

# Exercise 2
s="My favorite number is:"
n=8
print (s,n);

t="My favorite squre number is:"
o=8**2
print (t,o);

# Excercise 3
print ("\n\n\n")
items = {'1':'bill','2':'cows'}
print (items)
Choose_Item = input("Select your Item: ")
try:
    print( items[Choose_Item] )
except KeyError:
    print ('Item %s not found' % Choose_Item )
    name = input("What is your name? ")
color = input("What is your favorite color? ")
num = input("What is your favorite number? ")

print (name, "likes", color, "and", num)
