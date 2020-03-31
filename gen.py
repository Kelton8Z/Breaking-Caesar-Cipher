import string 
key = "goqibdwxystklmefacpvzurhjn"
base = string.ascii_lowercase
d = {}
for i in range(26):
    d[key[i]] = base[i]
file = open("/Users/keltonz/Desktop/11411/hw01-handout/key.txt","w")
for key,value in d.items():
    file.write("%s %s\n" % (key,value))

file.close()
