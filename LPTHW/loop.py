#coding=utf-8
#循环的学习测试

#错误的自以为是的联系
#n=1
#n=int
#for n<10:
#	n=n+1
#	print ('现在N的值为：',n)
#else:
#	print('现在N的值为：',n)

#names = ['aa','bb','cc']
#for name in names:
#	print (name)

#sum = int(0)
#count = int(0)
#group=[1,2,3,4,5,6,7,8,9,10]
#for x in group:
#	sum=sum+x
#	count=count+1
#	print('当前计算结果为', sum,' \n---当前已经计算了%d次' % count)#要把\n放在引号里面啊朋友！
#print('最终的计算结果为： ',sum)

#range序列的测试
#sum=0
#for x in range(101):
#	sum=sum+x
#	print(sum, x)
#print(sum)

#while循环
#sum = 0
#n = 0
#while n<=50:
#	sum=sum+n
#	n=n+1
#	print(sum, n)
#print(sum)

#list循环打印
#L = ['aa','bb','cc']
#for x in L:
#	print ('hello，%s!' % x)

#break a loop
#n = 1
#while n<=100:
#	print(n)
#	n=n+1
#	if n==78:
#		break
#print ('the end')

#continue a loop
n=0
while n>=0:
	n=n+1
	if n%2==1:
		continue
	print(n)