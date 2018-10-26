#coding=utf-8
#set values to the variables
people = 30
cars = 40
trucks = 15

#this is an if-statement with three statements to be decided.
#the elif is used in more than two statments.
#is multi elif block is true, then python will only run the first block that is true
#and run the first one, as the only one.
if cars>people:
	print("We should take the cars.")
elif cars<people:
	print("We should not take the cars.")
else:
	print("We can't decide.")
	
#this is an if-statement with three statments to be decided.
if trucks>cars:
	print("That's too many trucks.")
elif trucks<cars:
	print("Maybe we could take the trucks.")
else:
	print("We still can't decide.")
#thisi s an if-statement with two statements to be decided.
if people>trucks or cars>trucks:
	print("Alright, let's just take the trucks.")
else:
	print("Fine, let's stay home then.")