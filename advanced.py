
print(None)
print(type(None))


def first(s):
    if len(s) > 0: return s[0]
    else: return None

print(first('hello'))
print(first(''))

def square(n):
    t = type(n)
    if t == int or t == float:
        return n**2
    else: return None

