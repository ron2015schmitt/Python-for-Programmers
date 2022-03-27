
pointspossible = 100
score = 84
percentage = score / pointspossible
studentname = "Bill"


print("Percentage is {}".format(percentage))


if 0 <= percentage < .60:
    lettergrade="F"
elif .60 <= percentage < .70:
    lettergrade="D"
elif .70 <= percentage < .80:
    lettergrade="C"
elif .80 <= percentage < .90:
    lettergrade="B"
else:
    lettergrade="A"

print("{} {}".format(studentname, lettergrade))

