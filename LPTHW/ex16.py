#coding=utf-8
#import argv function from sys of the python organic lib.
from sys import argv

#set these two varibles as argv
script, filename = argv

#print a format string with the argument of filename
print(f"We are going to erase {filename}")
#print a string
print("If you don't want to hit CTRL+C(^C)")
#print a string
print("If you do want that, hit ENTER.")

#ask users to input something, this is a smart one. it collect user's input
#but doesn't give the value to any varible. so it's kind of "pause".
input("?")

#print a string
print("Opening the file....")
#target means the opened file and its status
#in this open function the file that the user give in the command-line 
#is opened and in a "w" mode.
#w mode means "write", which means the file as the second argument in the command-line 
#is opened and in a write mode and all these things set to target, the varible
target = open(filename, "w")
#print a string
print("Truncating the file....Goodbye!")
#run the truncate function to the file. the default of truncate function to cut 
#the size of the file from the very position (start). that means erase everything.
target.truncate()

#print a format string with a argument
print("Now the file {filename} has been erased.")
#print a string
print("Now I'am gong to ask you for three lines to write in the text.")

#gather input from users and prompt some strings to the users.
line1 = input("line 1 = ")
line2 = input("line 2 = ")
line3 = input("line 3 = ")

#print a string
print("I am going to write these to the file.")

#run a write function to the varible target. this function can only write string. 
#its argument is a string
#and run this function for 6 times 
#and then close the file in the varible to clear the memory? Yes!
#target.write("\n")
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#target.close()

target.write(f"\n, {line1}\n, {line2}\n, {line3}\n")
target.close()

#run the open function to open the file and create a 'file' object for varible txt.
txt = open(filename)

#print the file in the function of read. read the file object in txt
print(txt.read())

#print a string
print("And finally, we close it.OK, please hit ENTER!")
input("ARE YOUR SURE TO CLOSE IT?")

target.close()
print(f"Your {filename} file has been closed, goodbye!")