# Program to ask for temperature in F and output in C

ftemp = input("What is the temperature? ")

ctemp = (int(ftemp) - 32) * 5/9

print ("Temperature is ",ctemp, "C")
