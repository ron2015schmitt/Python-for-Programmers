
#give age sfor each dog
from itertools import count


dogs = { "Fido": 8, "Sean": 17, "One Woof Sam": 19 }

print(dogs)
print(dogs["Fido"])

# any object can be key and can mix object types in keys
cats = { 
    "Felix": 8, 
    "Boots": 8,
    13: 2
    }

print(cats)    

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"] 

cooldictionary = { 
    words[0]: definitions[0],
    words[1]: definitions[1],
    words[2]: definitions[2],
    }

print(cooldictionary.keys())
print(cooldictionary.values())

print(" ")
for key in dogs:
    print(key)
for key in dogs.keys():
    print(key)
for value in dogs.values():
    print(value)
for item in dogs.items():
    print(item)


dabools = [False, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, True, True, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, False, True, True, True, True, True, False, True, True, False, True, False, False, True, False, False, False, False, True, True, False, False, True, True, True, False, True, True, False, False, False, False, True, True, False, True, True, False, True, True, True, False, False, False, True, True, False, True, False, True, False, True, True, True, False, True, False, False, True, True, False, True, False, False, True, False, True, False, True, False, True, True, True, True, False, False, True, True, False, False, False, False, True, True, True, False, False, True, True, True, True, True, False, True, True, False, False, True, True, False, False, True, True, True, True, True, False, False, True, True, False, False, True, True, False, False, False, False, False, True, True, True, True, True, False, True, True, False, False, True, True, True, True, True, False, False, True, True, True, True, True, False, True, True, True, True, True, False, False, True, False, False, False, True, True, True, False, True, False, False, True, False, False, True, True, False, False, False, False, True, False, False, True, True, False, True, True, False, False, True, False, True, True, False, True, False, True, False, True, False, False, True, False, True, False, False, False, True, True, False, False, False, True, True, False, False, True, True, True, True, True, False, True, True, True, True, False, False, True, False, True, True, True, True, True, False, False, False, True, True, False, True, True, True, False, False, True, True, False, True, True, True, True, False, True, True, False, False, False, True, True, True, True, True, False, False, False, True, False, False, False, True, False, True, True, True, True, False, False, False, True, False, False, False, False, True, True, False, True, False, False, True, False, False, False, True, True, True, False, False, True, True, False, False, True, True, False, False, True, False, True, False, True, True, True, False, True, True, True, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False, True, False, True, False, False, True, True, False, True, False, False, True, True, True, False, True, True, True, False, False, False, True, False, True, True, False, True, False, True, True, False, True, True, False, False, True, False, False, False, True, True, False, True, True, False, False, True, True, True, False, False, True, False, True, True, True, True, False, False, True, True, False, False, True, True, False, True, False, True, True, True, True, True, False, False, False, True, False, False, True, False, False, True, True, False, False, False, False, False, False, True, False, True, False, False, True, True, False, True, True, True, False, True, True, False, False, True, False, False, True, True, False, True, False, True, False, False, True, False, True, True, False, False, True, True, False, False, True, False, False, False, False, True, False]
counter = {
    True: 0,
    False: 0
}

for bool in dabools:
    counter[bool] += 1

print(counter)