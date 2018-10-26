#coding=utf-8
#import argument function from sys
from sys import argv

#user's input command will be argv.
script, input_file = argv

#define a new function named print_all and its argument is f 
#this function will run a print
#in the print the f object will be read.
def print_all(f):
	print(f.read())
	
#defin a new function named rewin and its argument is f too
#this function has a new function: seek
#this means the python will put the cursor to the very postion to the size of argument
#default 0 means start from the begining of the file.
def rewind(f):
	f.seek(0)

#define a new function named print_a_line with two arguments
#line_count is an input argumen, f should be a object.
#this will print a line_count(int), and use a new function named readline
#readline will read the file line by line.
#default means from the begining
#use end = "" to avoid the \n to separate the sentence.
def print_a_line(line_count, f):
	print(line_count, f.readline(),end = "")

#open function open a file object for the variable current_file
current_file = open(input_file)

#print a sting with a \n to escape
print("首先，让我们来打印这个文件：\n")

#run the cuntion of print_all with the object
print_all(current_file)

#print a string
print("然后，我们从头开始……")

#run the rewind function
rewind(current_file)

#print a string
print("一行一行看内容：")

#set value 1 to variable
#run the print_a_line function with two arguments,
#one is int, one is object
#repeat this 3 times
#readline will read line one by one.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)