#coding=utf-8
print("你好，欢迎来到区块律动带飞理财风险自测")
print("在进行投资之前，你需要回答10个问题来了解自己的风险承受能力")
score = 0
blablabla = input("确认测试请回车：")

print("-"*10)
print("您目前的个人以及家庭财务状况属于以下哪一种：")
q_1 = {"1、有较大数额未到期负债":-10,
	"2、收支平衡，无存款无负债":0,
	"3、有一定积蓄":2,
	"4、有丰富的储蓄且有一定的投资":6,
	"5、有非常丰富的出去且有相当大的投资":10}
for i in q_1:
	print(i)
a = input("请选择：————>")
if "1" in a:
	score= score + q_1["1、有较大数额未到期负债"]
elif "2" in a:
	score= score + q_1["2、收支平衡，无存款无负债"]
elif "3" in a:
	score= score + q_1["3、有一定积蓄"]
elif "4" in a:
	score= score + q_1["4、有丰富的储蓄且有一定的投资"]
elif "5" in a:
	score= score + q_1["5、有非常丰富的出去且有相当大的投资"]
else:
	none
print(f"你现在的得分为{score}")