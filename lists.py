
games = ["Mario Bros 3", "Earthbound", "Pilotwings", "Mario Party"]

print(games)

print(type(games))

print(games[1])

games.insert(0, "Zelda")

print(games)

games[1] = 'Mario Bros 1'

print(games)

del(games[2])
print(games)

games = ["Zelda", "Mario Bros 3", "Earthbound", "Pilotwings", "Zelda", "Mario Party"]

# remove will remove the FIRST element that matches
games.remove("Zelda")
print(games)
print(len(games))

# tuples use parantheses.  both size and values are immutable!
tuple = ("Zelda", "Mario Bros 3", "Earthbound", "Pilotwings", "Zelda", "Mario Party")

print(tuple)


#to create an tuple of one element, you need to include a trailing comma
y = [ "hello" ]   # array
w = ( "hello" ) # value,, not a tuple
z = ( "hello", )  # tuple

shoes = ("Spizikes","Air Force 1","Curry 2","Melo 5")

# + operator does concatination for both arrays and tuples
# * operator replicates
q = ["hello"] + 2*[ "there" ]

def appendtotuple(thetuple, value):
    x = ( value, )
    t =  thetuple + x
    return t

print(appendtotuple(shoes,"loafers"))

# sets: use curly braces {}

myset= { "hello", "there "}
print(myset)
myset.discard("there")
myset.add("hi")
print(myset)


myset = set(games)
print(myset)

