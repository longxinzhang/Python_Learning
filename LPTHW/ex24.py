#coding=utf-8
#print three strings: one is normal, one have escape \ in 
#the last one has \n and \t escape 
print("Let's practice everything.")
print("You'd need to know 'bout escapes with \\ that do.")
print("\n newlines and \t tabs.")

#this string with ''' irqiy12984eyasidhak;j sfhpwyr 0923r9i3rhi '''
poem = '''
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere ther is none.
'''
#print strings and variable
print("------------")
print(poem)
print("------------")

#variable of result of a math calculation
five = 10 - 2 + 3 - 6
#print a formated string.
print(f"This should be five: {five}")

#define a function.
#in this function we have three calculation
#at the ending of the function it will return three arguments
#seems like it's a list? no. they are seperate variables
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
#set value to variable
#three variables combine a list 
#there values are the result of the function
#it will pass result argument to each variables one by one like a list.
#but not a list.
start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
#yes i remember and almost forget.
print("With a starting point of {}".format(start_point))
#it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

#set a value.
start_point = start_point / 10
#print a string
print("We can also do that this way:")
#now, as one variable to get three result argument, the formular is a list
#this list contains three arguments.
#as i printed in the end, you will see it.
formular = secret_formula(start_point)
#this is an easy way to apply a list to a format string.
#still remember the *? it means you can put a lot of argument to variables
#if you have no idea of how much argument you will give.
print("We'd have {} beans,{} jars, and {} crates.".format(*formular))
#print the list.
print(formular)