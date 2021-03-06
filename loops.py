
# rang(10) -> class of type range. iterates over 0 to 9

for x in range(10):
    print(x)

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]
odds = set([])
for n in numbers:
    if n % 2 == 1:
        odds.add(n)

print(odds)

# while loop
age = 27
while age <= 30:
    print(age)
    age += 1

n=0
y=1
while y <= 1000000000:
    n += 1
    y = 2**n

print("n={}",n)

# break
for x in range(10): 
    print(x) 
    if (x == 5): 
        break
# continue
for x in range(10): 
    if (x == 5): 
        continue
    print(x) 

# else runs after loop finishes, but not if break eneded it
for x in range(10): 
    if (x == 5): 
        continue
    print(x) 
else: 
    print("All done")

# else won't run here
for x in range(10): 
    if (x == 5): 
        break
    print(x) 
else: 
    print("All done")


nums = [99, 20, 30, 35, 16, 49, 39, 11, 69, 48, 85, 32, 10, 47, 24, 80, 37, 21, 3, 99, 13, 11, 23, 12, 40, 50, 24, 14, 10, 62, 21, 24, 55, 57, 38, 55, 83, 63, 34, 31, 15, 26, 82, 47, 37, 14, 64, 72, 90, 39, 70, 50, 67, 61, 23, 28, 30, 13, 87, 58, 80, 62, 15, 49, 33, 7, 38, 2, 92, 76, 80, 18, 6, 25, 22, 25, 91, 9, 37, 83, 46, 98, 69, 3, 40, 6, 48, 1, 63, 51, 32, 19, 77, 74, 22, 75, 41, 19, 27, 82, 60, 6, 1, 55, 5, 71, 18, 84, 47, 16, 1, 8, 41, 6, 17, 100, 62, 36, 45, 32, 4, 33, 68, 15, 2, 92, 50, 54, 34, 12, 17, 16, 74, 95, 2, 61, 75, 12, 6, 39, 28, 18, 30, 39, 8, 34, 62, 31, 57, 8, 69, 19, 71, 70, 40, 79, 76, 96, 84, 76, 85, 4, 40, 64, 45, 11, 46, 100, 56, 9, 86, 5, 78, 81, 18, 70, 76, 46, 85, 69, 64, 88, 17, 91, 49, 93, 18, 29, 38, 42, 77, 63, 46, 32, 83, 88, 48, 68, 89, 80]

n = 0
for x in nums:
    if (x == 68): break
    n += 1
print(n)