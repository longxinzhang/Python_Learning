# -*- code: utf-8 -*-
s1=float(input('去年的学习成绩是'))
s2=float(input('今年的学习成绩是'))
if s2<60:
	print('你怎么回事，今年才考了%.1f分，都没及格你知道吗？' % s2)
elif s2==60:
	print('真够幸运的，刚好60分！')
elif s2>60 and s2<75:
	print('%.1f分只能说是及格线啊！' % s2)
elif s2>=75 and s2<85:
	print('%.1f分，这个分数算是良好了！' % s2)
elif s2>=85 and s2<100:
	print('%.1f分，这个分数算是优秀了哦！考得很不错！' % s2)
else:
	print('好厉害啊，这次考了满分，再接再厉哦！')
s=s2-s1
r=(s/s1)*100
if s<0:
	s=-s
	print('%s,学习成绩退步了【%.2f %%】，把你家长叫来！' % ('小明',r))
	n=str(input('你家长的手机号码是多少？'))
	m=int(input('你家长的手机号是%s，对吗，对打1' % n))
	if m>=1:
		print('明天我就%s这个号码打电话，看看他们到底管不管你！' % n)
	else:
		m1=str(input('那你家长的手机号码是多少？'))
else:
	print('%s,学习成绩进步了 %.2f %%' % ('小明',r))
	