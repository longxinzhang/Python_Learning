#coding=utf-8
def test1():
	try:
		print("to do stuff")
#		raise Exception("Hehe")
		print("to return in try")
		return "Try"
	except Exception:
		print("Process except")
		print("To return in except.")
		return "Except"
	finally:
		print("To return in finally.")
		return "Finally"
		
test1Return = test1()

print("Test1Return" + test1Return)
