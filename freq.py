import collections

with open("encoded.txt", "r") as f:
    s = f.read()

c = collections.Counter(s)

for letter, count in c.most_common(26):
    print("%s: %7d" %(letter,count))



