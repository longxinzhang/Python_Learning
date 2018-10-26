#coding=utf-8
#def a(*params):
#	a[0],a[1],a[2],a[3] = params
#	print(params)
#	print(type(params))
#
#a={'params',1,2,3}
#b = (1,2,3,4,5)
#print(b)
def test_var_args(f_arg, *argv):
	print(f"First normal arg: {f_arg}")
	for arg in argv:
		print(f"Another arg through *argv: {arg}")
		
test_var_args("Yasoob","Python","Eggs","Test")