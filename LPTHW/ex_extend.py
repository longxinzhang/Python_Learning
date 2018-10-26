#coding=utf-8
def shop_earning(sales1, sales2):
	#一台苹果手机的售价为12799元，一台苹果手机的成本价为2799元
	#一台小米手机的售价为2799元，一台小米手机的成本价为1799元
	earning_iphone = sales1 * 12799 - sales1 * 2799
	earning_xiaomi = sales2 * 2799 - sales2 * 1799
	earning_total = earning_iphone + earning_xiaomi
	print("Well Well Well,\nlet's have a look of today's performance--->\n")
	print(f"You have sold {sales1} iPhone Xs Max today.")
	print(f"You have sole {sales2} Xiaomi 8 today.")
	print(f"Your earning today is {earning_iphone} from Apple.")
	print(f"Your earning today is {earning_xiaomi} from Lei Busi.")
	print(f"So you have earned {earning_total} today!")
	print("Congratulations!\n")
#1 pass arguments
shop_earning(1,1)
print("============#1==============")
#2 do some math
shop_earning(1+2,1+2)
print("============#2==============")
#3 pass variables
a = b = 3
shop_earning(a,b)
print("============#3==============")
#4 variable + math
c = 4
shop_earning(c+1,c+2)
print("============#4==============")
#5 function to function
shop_total = shop_earning
shop_total(10,10)
print("============#5==============")
#6 *vags 
vags = (11,12)
shop_earning(*vags)
print("============#6==============")
#7 one more function
def another_one():
	v1=20
	v2=20
	shop_earning(v1,v2)
another_one()
print("============#7==============")
#8 user input
sale_iphone = int(input("how many iPhone Xs Max have you sold today?"))
sale_xiaomi = int(input("How many Xiaomi 8 have you sold today?"))
shop_earning(sale_iphone,sale_xiaomi) 
print("============#8==============")
#9 function in function 
def another_two(ss1,ss2):
	s_1 = ss1 * 1
	s_2 = ss2 * 1
	shop_earning(s_1,s_2)
another_two(10,11)
print("============#9==============")

#10
#print("============#1==============")
