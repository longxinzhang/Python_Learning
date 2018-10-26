#normal import and set argument values...
import sys
script, encoding_way, error = sys.argv
#script, error = sys.argv

#defin a main function with three arguments
#call readline function to the file object and read one line
def main(language_file, encoding_way, errors):
	line = language_file.readline()

#build a if_statement 
#this function will test if the variable line is empty or not(ture or false)
#if not empty, it will run the left codes.
#if empty, it will stop run the left code and stop it.
#tricky here: if the object file is filled with endless lines,
#this loop will never end because it re-call the main function .....
#in this if_statement, it called another function print_line with three arguments.

	if line:
		print_line(line, encoding_way, errors)
		return main(language_file, encoding_way, errors)
	
#define a new function with three arguments.
#.strip is to remove some character from the beginning and the end of the line
#default of .strip is to remove space key
#when removed, it will give string value to next_lang
#.encode means to encode the string to some string using encoding "utf-8"
#the raw_bytes will be \xe4\xb8\x80\xe4\xba\x8c\xe4\xb8\x89\xe5\x9b\x9b this like
#that's because this is the code that computer understand, so it's raw byte.
#用utf-8编码，再用utf-8解码，ok的 \xba这样的ascii是可以被机器读的
#机器读的01010101010这样的，这些二进制的数如何翻译呢？将ascii码解码成010101010
#ascii就是\xba这样的码，而encode做的事情就是把将你想使用的编码格式
#将其翻译成ascii的码格式，不同的utf-8 -16 -32之间翻译成的ascii是不一样的
#所以如果要翻译成ascii又翻译回来，需要使用同一个编码格式，让encode function
#知道具体的编码格式是什么，这个function不给默认，必须填
#同理cooked_string 就是把ascii翻译成utf-8
def print_line(line, encoding_way, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding_way, errors=errors)
	cooked_string = raw_bytes.decode(encoding_way, errors=errors)
	
	print(raw_bytes, "====",cooked_string)
	print(cooked_string == next_lang)

#in this line, we open a file to the variable.
#something interesting here: when you want the file to be encoded in some coded format
#you need to fill the third argument(the 'r' is default as the second argument) with 
#encoding = "some encode" 
#this is different from the variable encoding. it's an argument.
languages = open("test2.txt", encoding = "utf-8")
#encoding = "utf-8"
#甘霖娘！为什么要在variable里使用argument的name
main(languages, encoding_way, error)
#main(languages, encoding, error)