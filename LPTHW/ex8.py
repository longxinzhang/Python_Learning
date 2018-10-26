#coding=utf-8
#set a string for formatter but in this string, there are four variables waiting for the function to work

formatter = "{}{}{}{}"

# arguments of 1234 will be put in the variables in the formatter and make the 1234 a string
print(formatter.format(1,2,3,4))
#four strings in the string variables
print(formatter.format("one", "two", "three", "four"))
#four bool values in the string variables
print(formatter.format(True,False,True,False))
#four formatters in the formatter string variables
print(formatter.format(formatter,formatter,formatter,formatter))
#four long string in the formatter string variables, but the pause break won't influence the print result
print(formatter.format(
	"My love",
	"is like a red red rose",
	"It's my love."
))