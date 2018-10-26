#coding=utf-8
from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()
print(f"Does the output file exist?{exists(to_file)}")
open(to_file, 'w').write(indata)
open(to_file).close()

txt=open(to_file)
print(txt.read())
