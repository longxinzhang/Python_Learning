#coding=utf-8
ten_things = "Apple Orange Crows Telephone Light Sugar"
print("there are :", len(ten_things), "things in the list now....")
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: ", next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items in the list now.")
	
print("What we have in the list now:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa ! Fancy!
print(stuff.pop())
print(" ".join(stuff)) #what? cool
print("#".join(stuff[3:5])) #super stellar!