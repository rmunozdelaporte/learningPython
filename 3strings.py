print('Hello', 'world', 'concatenated', 'with', 'spaces')


print('I can\'t ... \n\neven')
'''She said, "I can't ...
...
... even."
 '''
#print(_)


dessert = "Chocolate" + " and marshmallows"
dessert = dessert + " and graham crackers"
dessert += " yum"
dessert += "!"*20
print(dessert)

quote = "A person who never made a mistake never tried anything new"
len(quote)
quote.upper()
quote.lower()
quote.title()

str(42)
#help(str)

template = "Thanks for learning {} with us {}!"
template.format('Python', 'Valentina')
"You just bought {} {}.".format(3, "Fidget cubes")
"ham" in "hamster"

x = 0x0a
y = 0x0f
z = 0x0f
print(f'(hex x is {x:02x}')