#coding=utf-8
#define a function named cheese_and_cracker
#this function has two arguments: cheese_count and boxes_of_crackers
#then 4 prints, and two of them are format string.
def cheese_and_cracker(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

#give the function two arguments
#both of the arguments are numbers(integer)
print("We can just give the function numbers directly:")
cheese_and_cracker(20,30)

#give the function two variables
#both of the two variables are integers
print("Or...we can use variables from our script:")
amount_of_cheese = 10
amount_of_crakcer = 50
#then we put the two variables in the function as its arguments
cheese_and_cracker(amount_of_cheese,amount_of_crakcer)

#the two arguments can be math result
print("Also, we can even do math inside too:")
cheese_and_cracker(10+20,5+6)

#the two arguments can be mixed variables and math, 
#because basically, it's still math problem. 10+10
print("And we can combine the two, variables and math:")
cheese_and_cracker(amount_of_cheese + 10,amount_of_crakcer + 1000)