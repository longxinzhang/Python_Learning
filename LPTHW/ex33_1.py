#coding=utf-8
def numb(i,m):
	print(f"initial i = {i}, m = {m}")

	while i < 4 :
		print(f"Now the number is {i}")
		numbers.append(i)
		
		i = i + 1
		m = numbers[-1]
		print("We now have : ",numbers," in the list.")
		print(f"The newly-added number is {i}")
		print(f"The last number in the list is {m}\n")
#		numb(i,m)
	return m



i = 1
numbers = []

last_number = numb(i,0)
print(f"Now i is {i}")
print(f"now last_number: {last_number}")
