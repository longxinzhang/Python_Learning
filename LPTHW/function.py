#coding=utf-8
a=int(input('please enter your 10-digital number'))
b=hex(a)
#print(b)
print('your hex of the number %d is: %s'% (a,b))
#print('your hex of the number %s is: %x'% (a,b)) 错误原因b是字符串，并非16进制，它是以16进制现实在字符串中。

