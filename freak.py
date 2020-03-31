import collections
import os

cur = ""
s = ""

with open("encoded.txt", "r", encoding="ISO-8859-1") as f:
    cur = f.read()
s += cur

c = collections.Counter(s)

for letter, count in c.most_common(26):
    print("%s: %7d" %(letter,count))



