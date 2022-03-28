
age=input("What is your age?: \n")

print("Your age is "+age+" years old!")

# input always returns a string

print( type(14) )
print( type(14.5) )
print( type("14") )
print( type(None) )

# exception handlimg

try:
    age = int(input("enter age:"))
    print("Valid age!")
except Exception:
    print("You need to provide a valid number")
