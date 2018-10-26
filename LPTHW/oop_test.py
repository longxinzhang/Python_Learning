#coding=utf-8
import random
from urllib.request import urlopen
import sys
#import random、urlopen和sys

#world url是一个字符串
#words是一个list
WORLD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

#phrase是一个dictionary，结构是“”：“”，其中包含一些关键字，可在后面根据function进行替换
PHRASES = {
	"class %%%(%%%)":
		"Make a class named %%% that is a %%%.",
	"class %%%(object):\n\tdef __init__(self,***):":
		"class %%% has-a __init__ that takes self and *** params.",
	"class %%%(object):\n\tdef ***(self,@@@)":
		"class %%% has-a function *** that takes self and @@@ params.",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, call it with params self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}

#do they want to drill phrases first
#计算输入的arguments的数量，len()，并判断第二个变量是不是等于这个字符串，随后给一个变量赋值
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASES_FIRST = True
else:
	PHRASES_FIRST = False
	
#load up the words from the website
#urpopen读取网络文档，然后readlines后将字符串添加到words list中，编码类型是utf-8
for word in urlopen(WORLD_URL).readlines():
	WORDS.append(str(word.strip(),encoding = "utf-8"))

#定义一个convert函数，这个很复杂，是把输入的第一句和第二句进行&&&和***统计，然后再替换。
def convert(snippet, phrase):
#先根据输入的snippet中的%%%数量来确定sample函数的第二个值，确定完这个值之后，
#sample函数从words list中随机取几个value来，然后for 循环一下，因为list里只有一个value
#循环一次结束，用capitalize来将其变成大写
#other_names 统计snippet里面***的数量，然后words list里随机几个value，传递给other_names
#results是一个list，param_name也是一个list
	class_name = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_name = []

#for循环，次数是（0到snippet里面@@@的数量），1-3次）
#然后param_count获得一个随机的1-3的整数
#然后param_name这个list里加入一个value，这个value先根据param_count的数字来确定sample几个数
#值，然后以“,”为分隔符号将他们添加到param_name list里。
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_name.append(','.join(random.sample(WORDS, param_count)))

#for循环 ，先循环snippet再循环phrase，然后用[:]遍历两个变量的值，然后赋给result
#result这里是一个字符串，它是会变的，因为后面还有一个results.append()会用到它。
#result 这个会在for下的几个for循环里用到，进行内容替换。

	for sentence in snippet, phrase:
		result = sentence[:]
#这个for循环把result list 里的%%% 替换为 class_name 刚才大写的那个字符串，替换1次		
		#fake class names
		for word in class_name:
			result = result.replace("%%%", word, 1)
#这个for循环把result list 里的*** 替换为other_name 里没有大写的那个字符串(随机的，可能和)
#class_name里那个大写的不一样，替换1次			
		#fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
#这个for循环把result list里的 @@@ 替换为param_name 里的那个用“,”作为分隔符的字符串，替换1次			
		#fake parameter lists
		for word in param_name:
			result = result.replace("@@@", word, 1)
#不同的PHRASE的key里包含的%%%、***和@@@ 不一样，所以不一定会替换，for循环不一定执行哦
#注意这个result是字符串哦。
#循环结束之后，将result添加到results 
#然后返回results，退出def
		results.append(result)
	return results

#try except了哦
#while true无线循环
#使用list函数把PHRAESE里的key全部取出并变成list给snippets
#然后对这个snippets 的list shuffle一次，乱序
#keep going until they hit CTRL-D
try:
	while True:
		snippets = list(PHRASES.keys())
		random.shuffle(snippets)
#for 循环，phrase 获得key的value，字符串
#将两个变量的值传递给convert函数进行运算，返回的results
#question 和 answer 获得convert的返回值results这个list里的两个值
#然后if判断上面那个true false，如果是True，就把两者的值互换一下
#这里好像没有什么影响，不知道true 和 false之间的区别是什么……
#如果是true的话，一切正常，如果是false就是反了呗……
#然后打印question
#然后prompt等待回车
#然后打印answer
#如果出现EOFError的话，就退出
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASES_FIRST:
				question, answer = answer, question
			print(question)
			
			input(">")
			print(f"ANSWER: {answer}\n\n")
except EOFError:
	print("\nBYE")