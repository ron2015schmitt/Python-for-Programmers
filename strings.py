# can use single or double quotes

'hello'
"hello"

# use 3 quotes of either type for multi-line strings

'''hello
world'''

"""hello
world"""

# can use strings as comments


# + is the concatination operator
print("hello"+" "+'world!')

# * is used for repition of a string
print(9*"9")

# printing variables
age = 30
print("My age is {}".format(age))
print("My age is {} and pi is {}".format(age, 3.1415))


"Hello".upper()
"Hello".lower()
"Hello world".title()
len("hello")
s="Hi my name is Bob".replace("Bob","Jim")
print(s)

s[0]
s[-1]
s[-17]   # gives same as s[0]
s[16]   # gives same as s[-1]


s[-18]    # gives an error
s[17]    # gives an error


# slices. s[n:m] goes from s[n] to s[m-1]  !
s[0:2]
s[6:10]

s[3:-4]

s[:10]  # same as 0:9
s[3:]   # same as 0:len

s[3:0]  # gives "" empty string

s[-1:]  # final character

