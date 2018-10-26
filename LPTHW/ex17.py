#coding = utf-8
#import the argv function from sys
from sys import argv
#import exists function from os.path
#exists
from os.path import exists

#give three arguments to the script.
script, from_file, to_file = argv

#print a format string with two arguments in
print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

#print a format string with one argument and one new length function #
#to count the size of the variable
print(f"The input file 【{from_file}】 is {len(indata)} bytes long")

#print a format string with a new exists function 
#this will need to put the string path argument to it
#if the file exist in the path, it will return truth.
#or, it will return a false.
print(f"Does the output file exist?{exists(to_file)}")
print("Ready, hit ENTER to continue. CTRL+C to abort.")
#ask user to input something
input()

#open the file in a write mode, this is a object and this object is to 
#the out_file variable
out_file = open(to_file, "w")
#run the write function to variable. it will write the argument value to 
#the variable out_file
out_file.write(indata)
out_file.close()


print("Alright, all done.")
print(f"Your new file {to_file} is:")


#txt = open(from_file)
#print(txt.read())
txt = open(to_file)
print(txt.read())


in_file.close()
