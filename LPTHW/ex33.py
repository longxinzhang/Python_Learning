#coding=utf-8
def numb(i):
	if i < 5 :
		print(f"Now the number is {i}")
		numbers.append(i)
		
		i = i + 1
		m = numbers[-1]
		print("We have: ",numbers)
		print(f"Now the new number is {i}")
		print(f"Now the last number in the list is {m}\n")
		return numb(i)
	else:
		print(i)
		return i


k = 0
numbers = []

n = numb(k)
print(f"Now k is {k}")
print(f"now n: {n}")
