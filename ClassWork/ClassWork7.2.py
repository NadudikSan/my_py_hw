#Demonstration chr()
from re import A


x = "a"
x1 = 97

print(type(x))
print(type(ord(x)))
print (type(chr(x1)))

print(chr(ord(x)), x)
print(chr(ord(x)) == x)

print(ord(chr(x1)), x1)
print(ord(chr(x1)) == x1)

#indexing string

the_string = "silly walks"

for ix in range(len(the_string)):
    print(the_string[ix])
print()
#indexing string Negative indices bahave
for ix in range(len(the_string), -1, -1, -1):
    print(the_string[ix])
print()
