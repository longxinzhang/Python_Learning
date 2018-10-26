#coding=utf-8
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslach_cat = "I'm \\ a \\ cat"
a=10
fat_cat = """
I'ill do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\\  cat
\'  cat
\"  cat
\a  cat
\b  cat
\b  cat
\f  cat
\n  cat
\v  cat
"""

print(tabby_cat)
print(persian_cat)
print(backslach_cat)
print(fat_cat)
#put more escape sequence mark in the codes!!!
escape = "\n\t\t\t\t\tAh \n\t\t\t\thow \n\t\t\tmany \n\t\tnew \n\tlines \nin \n\tthis \n\t\tlist:{}"
print(escape.format('\n\t\t\tLoads! \n\t\t\t\tAnd some more!'))

#do more excises by using the !r
print("Didn't you see{!r},that's {!r}".format("Michaels\'s top","crazy"))
print("Didn't you see{!s},that's {!s}".format('Michaels\'s tops','crazy'))