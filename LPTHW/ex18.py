#coding=utf-8
#this one is like your scripts with argv
#define a function named print_two,
#notice the * mark in the parenthesis, and the gogo .
#*means don't know the number so you can type as much argument as you can.
#gogo is just a variable, it can change to anyname.
#only when you run the function, you need to give the arguments to the function.
#then the arguments goes to gogo variable
#when we get enough arguments, let's print it with a format string.
def print_two(*args):
	arg1, arg2, arg3 = args
	print(f"arg1:{arg1},arg2:{arg2},{arg3}")

#ok, that *args is actually pointeless, we can just do this
#in this function define, in the parenthesis, there are two variables
#so the two exact variables don't need to go the "argument = variable" process,
#it can be used in the function directly#
#then we print the format argument.
def print_two_again(arg1, arg2):
	print(f"arg1:{arg1},arg2:{arg2}")
	
#this just take one argument
#in this function define, only one argument is allowed.
def print_one(arg1):
	print(f"arg1:{arg1}")
	
#this one takes no arguments
#in this function definition, no argument is allowed. i don't know why do this.
#or maybe in some cases, there will be no result to the argument, 
#so the script will return no result? maybe.
def print_none():
	print("I got nothing.")	

#let's run the functions.
print_two("Longxin","Zhang","OKAY!")
print_two_again("Longxin","Zhang")
print_one("GOGOGO!")
print_none()
