#coding=utf-8
print("Input stop no.")
stop = int(input("> "))
print("Input increment.")
inc = int(input("> "))
i = 0

def number_roll(x, stop_no, increment, numbers):

	#i = 0
	#numbers = []

	while x < stop_no:
		print(f"At the top i is {x}")
		numbers.append(x)

		x += increment
		print("Numbers row: ", numbers)
		print(f"At the bottom i is {x}")

	print("The numbers:")

	for num in numbers:
		print(num)
number_roll(i, stop, inc, [])
