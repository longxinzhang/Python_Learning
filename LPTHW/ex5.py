#coding=utf-8
the_name = 'Longxin Zhang'
the_age = 29 #not a lie
the_height = 186 #cm
the_weight = 88.5 #kg
the_eyes = 'Grey'
the_teeth = 'White'
the_hair = 'Black'

print(f"Let's talk about {the_name}.")
print(f"He's {the_height} cm tall.")
print(f"He's {the_weight} KG heavy.")
print("Actually that's a little bit heavy.")
print(f"He's got {the_eyes} eyes and {the_hair} hair.")
print(f"His teeth are usually {the_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = the_age + the_height + the_weight
print(f"If I add{the_age}, {the_height}, {the_weight}, I get {total}.")