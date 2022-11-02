#concatenation of the sentence variables
course = 'Python for "beginners" and the courses are "python" and "django"'
print(course)

#square bracket syntax
print(course[0])
print("Prints from the end: "+course[-2])

#slicing
print(course[0:3])
print(course[:]) # prints the whole string

#application of formatted strings
first = 'Manzi'
last= 'Cedro'

#The Example: You are by the names of [Manzi][Cedrick]
msg = f'You are by the names of [{first}][{last}]'
print(msg)