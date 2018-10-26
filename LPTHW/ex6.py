#coding=utf-8
#set the valuse to types_of_people
types_of_people = 10.0
#set the value of x to a format string which contain a viable in the string
x = f"There are {types_of_people} types of people."

#set a string value to binary
binary = "binary"
#set a sring value to do_not
do_not = "don't"
#set a format string to y which contains two viables
y = f"Those who know {binary} and those who {do_not}."

#print the value of x
print(x)
#print the value of y
print(y)

#print the value of the format string with a x viable in it
print(f"I said: {x}")
#print the value of the format string with a y viable in it
print(f"I also said: {y}")

#set a bool value to viable hilarious
hilarious = False
#set a format string value to joke_evaluation with a default {0} viable in it.
joke_evaluation = "Isn't that joke so funny?!{}"

#print the format string of joke_evaluation and put the bool value of hilarious in this f.string.
print(joke_evaluation.format(hilarious))

#set the string value of the w
w = "This is the left side of..."
#set the string value of the e
e = "a sring with a right side."

#print the two values together if 
print(w+e)
