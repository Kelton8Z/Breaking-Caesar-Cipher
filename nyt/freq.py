import collections
import os

cur = ""
s = ""
for filename in os.listdir("/Users/keltonz/Desktop/11411/hw01-handout/nyt"):
    with open(filename, "r", encoding="ISO-8859-1") as f:
        print(filename+"\n")
        cur = f.read()
    s += cur

c = collections.Counter(s)

for letter, count in c.most_common(26):
    print("%s: %7d" %(letter,count))



