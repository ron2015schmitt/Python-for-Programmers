
import operator
import sys

fname = sys.argv[1]
file = open(fname, "r")
text = file.read()
file.close()

split = text.split()
words = {}
for word in split:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

swords = sorted(words.items(), key=operator.itemgetter(1), reverse=True)  # 1 -> sort on value

ofname = fname[:-4] + "-counted" + fname[-4:]
file = open(ofname, "w")
file.write("Total Words = {}, Unique Words = {}\n".format(len(split), len(swords)) )
for item in swords:
    file.write("{} - {}\n".format(item[0], item[1]) )
file.close()


