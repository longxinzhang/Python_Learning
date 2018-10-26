#coding=utf-8
from sys import exit

def store(aa):
	print("欢迎来到商店，请问你想买什么？")
	print("A柜台卖水果，B柜台卖饮料")
	
	toward = input("请问你去那个柜台？")
	while True:
		if "a" or "A" in toward:
			counter_a(aa)
		elif "b" or "B" in toward:
			counter_b(aa)
		else:
			print("请告诉我你要去哪个柜台")


def counter_a(money):
	print(f"现在钱包里还有{money}块钱了。")
	print("你想买什么东西呢？")
	print("我这里有香蕉和苹果")


	cart = input("想买什么呢？")
	while True:

		money_enough(money)
			
		if "apple" or "苹果" in cart:
			print("苹果一个2块钱")
			apple_pay = int(input("要多少个？"))
			payment = apple_pay * 2
			money_deduct(money, payment)
		elif "banana" or "香蕉" in cart:
			print("香蕉一个3块钱")
			banana_pay = int(input("要多少个？"))
			money -= (banana_pay * 3)
		else:
			print("你说啥，那你去B柜台转转吧")
			exit()
	return a
	
def money_enough(bb):
	if bb <= 1:
		print("兄dei，你钱不够了，走吧！")
		exit()
	
def money_deduct(wallet, payment):
	wallet = wallet - payment
	print(f"花费了{payment}钱，钱包里还剩{}钱")
	return wallet

wallet = int(input("你身上有多少钱？"))
shopping_cart = []
print(f"{wallet}这么多钱呢！走去shopping！")
store(wallet)

print()
