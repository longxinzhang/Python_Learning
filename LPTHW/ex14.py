#coding=utf-8
from sys import argv

robot, user_name, title= argv
prompt = '--> '
#keep rememeber the first argument of sys is the script_name.
print(f"Hi{user_name} {title}, I'm the {robot} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name} {title}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f'''
Alright, so {user_name} {title} said '{likes}' about likeing me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
''')