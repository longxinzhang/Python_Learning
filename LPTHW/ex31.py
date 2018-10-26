#coding=utf-8
print("You enter a dark room with two doors.\n Do you go through door #1 or #2?")

door = input("choose your door:   ")

if door == "1":
	print("There is a giant bear here eating a cheese cake.")
	print("What do you do ?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")
	
	bear = input("what do you choose?   ")
	
	if bear == "1":
		print("the bear eats your face off. good job.")
	elif bear == "2":
		print("the bear eats your legs off. good job.")
	else:
		print(f"welllllll, doing {bear} is probably better.")
		print("See!\n The bear runs away!")
elif door == "2":
	print("you stare into the endless abyss at Cthulhu's retina!")
	print("1. Bluberryies.")
	print("2. Yellow jacket clothespins.")
	print("3. Understaning revolvers yelling molodies.")
	
	insanity = input("what do you choose ?   ")
	if insanity == "1" or insanity == "2":
		print("your body survives powered by a mind of jello.")
		print("good job!")
	else:
		print("the insanity rots your eyes into a pool of muck.")
		print("good job.")
else:
	print("You stumbled around and fall on a knife and die. Good bye.")