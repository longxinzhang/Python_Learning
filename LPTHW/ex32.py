#coding=utf-8
#list use [] to gather its items
#numbers, strings are allowed.
the_count = [1,2,3,4,5]
fruits = ["apples","bananas","pears","appricots","oranges"]
change = [1,"pennies",2,"dimes",3,"quarters"]

#this first kind of for-loop goes through a list
for number in the_count:
	print(f"this is count {number}.")

#the same as above
for fruit in fruits:
	print(f"A fruits of type: {fruit}.")
	
#also we can go through mixed lists too
#notice we have to use{} since we don't know what's in it
for i in change:
	print(f"i got {i}.")

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts.
#for i in range(0,8,2):
#	print(f"Adding {i} to the list.")
#	#append is a function that lists understand.
#	elements.append(i)

#let's define a function to do the repeated work. yes!
def looppp(n):
	if n <= 4:
		n=n+1
		print(f"adding {n} to the list")
		elements.append(n)
		looppp(n)
n = 0
looppp(n)

#now we can print them out too
for i in elements:
	print(f"The elements contains: {i}")