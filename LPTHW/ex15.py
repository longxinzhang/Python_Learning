#coding=utf-8
#import sys and the fuction of argv as the we will use it later because when 
#you type the python + script + argument values + argvs
#you will use the argvs as we has already set it there.
from sys import argv

#set the two variables as the arguments.
script, filename = argv

#set a new variable named txt and give it the fuction of open
#this fuction will run the filename as the user put in the cmd, the second argv.
txt = open(filename)

#print a format string with filename arguments in
print(f"Here's your file {filename}:")
#print the variable named txt which has a command READ () default is read-only mode.
print(txt.read())
#close() 方法用于关闭一个已打开的文件。
#关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。
#当 file 对象，被引用到操作另外一个文件时，Python 会自动关闭之前的 file 对象。 
#使用 close() 方法关闭文件是一个好的习惯。
txt.close()

#print a string
print("Type the filename again:")
#ask the users to input something to the variable file_again and the prompt is >
file_again = input(">")

#give the variable txt_again a function open and file a command open the file named file_again 
#the file_again variable has been given by the users in the last step.
txt_again = open(file_again)

#print the txt_again variable with the command of opening it.
print(txt_again.read())
