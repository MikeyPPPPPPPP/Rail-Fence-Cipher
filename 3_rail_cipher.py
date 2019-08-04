"""
0     4       8      12      16       20       24
 1  3   5   7  9  11  13  15    17  19  21   23
  2       6     10      14        18      22

3 rails
"""

list1 = []
list2 = []
list3 = []
fulllist = []

message = (input("Enter: "))

def evensimsg(mes):
    rail1 = []
    rail2 = []
    rail3 = []
    numsret = []
    numsret[:0] = mes
    wordlen = len(mes)
    r1 = [0, 4, 8, 12, 16, 20, 24]
    r2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    r3 = [2, 6, 10, 14, 18, 22]
    for x in range(0,wordlen):
        if x in r1:
            rail1.append(mes[x])
        elif x in r2:
            rail2.append(mes[x])
        else:
            rail3.append(mes[x])


    return rail1, rail2, rail3


evod = evensimsg(message)

for x in evod[0]:
    list1.append(x)

for x in evod[1]:
    list2.append(x)

for x in evod[2]:
    list3.append(x)


for x in list1:
    fulllist.append(x)

for x in list2:
    fulllist.append(x)

for x in list3:
    fulllist.append(x)

str1 = ''.join(str(e) for e in fulllist)
print(str1)
