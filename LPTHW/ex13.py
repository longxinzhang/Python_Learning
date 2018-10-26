#coding=utf-8
from sys import argv
#read the WYSS section for how to run this
#script, first, second, third = argv
one, two, three, four = argv
#print("This script is called:", script)
#print("Your first variable is:", firt)
#print("Your second variable is:", second)
#print("Your third variable is:", third)

print(argv[0])

print("This script is called:", one)
print("Your first variable is:", two)
print("Your second variable is:", three)
print("Your third variable is:", four)

five=input("what do you want to ear more?")
print("you like to eat: {five}".format(five=five))
