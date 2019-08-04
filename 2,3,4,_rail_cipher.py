class rail2:
    def two_rails(self, mes): # 2 rails
        rail1 = []
        rail2 = []
        numset = []
        numset[:0] = mes
        wordlen = len(mes)
        r1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        for x in range(0, wordlen):
            if x in r1:
                rail1.append(mes[x])
            else:
                rail2.append(mes[x])

        return rail2, rail1

    def evensimsg(self, mes): # 3 rails
        rail1 = []
        rail2 = []
        rail3 = []
        numsret = []
        numsret[:0] = mes
        wordlen = len(mes)
        r1 = [0, 4, 8, 12, 16, 20, 24]
        r2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
        r3 = [2, 6, 10, 14, 18, 22]
        for x in range(0, wordlen):
            if x in r1:
                rail1.append(mes[x])
            elif x in r2:
                rail2.append(mes[x])
            else:
                rail3.append(mes[x])

        return rail1, rail2, rail3

    def the_rail_5(self, mes): # 5 rails
        rail1 = []
        rail2 = []
        rail3 = []
        rail4 = []
        rail5 = []
        numsret = []
        numsret[:0] = mes
        wordlen = len(mes)
        r1 = [0, 8, 16, 24]
        r2 = [1, 7, 9, 15, 17, 23]
        r3 = [2, 6, 10, 14, 18, 22]
        r4 = [3, 5, 11, 13, 19, 21]
        r5 = [4, 12, 20]
        for x in range(0, wordlen):
            if x in r1:
                rail1.append(mes[x])
            elif x in r2:
                rail2.append(mes[x])
            elif x in r3:
                rail3.append(mes[x])
            elif x in r4:
                rail4.append(mes[x])
            else:
                rail5.append(mes[x])

        return rail1, rail2, rail3, rail4, rail5

    def the_rail_4(self, mes): # 4 rails
        rail1 = []
        rail2 = []
        rail3 = []
        rail4 = []
        numsret = []
        numsret[:0] = mes
        wordlen = len(mes)
        r1 = [0, 6, 12, 18, 24]
        r2 = [1, 5, 7, 11, 13, 17, 19, 23]
        r3 = [2, 4, 8, 10, 14, 16, 20, 22]
        r4 = [3, 9, 15, 21]
        for x in range(0, wordlen):
            if x in r1:
                rail1.append(mes[x])
            elif x in r2:
                rail2.append(mes[x])
            elif x in r3:
                rail3.append(mes[x])
            else:
                rail4.append(mes[x])

        return rail1, rail2, rail3, rail4


    def the_rail_help2(self, entry_input, evod): # 3rails
        list1 = []
        list2 = []
        list3 = []
        fulllist = []
        message = entry_input

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
        return(str1)

    def the_rail_help1(self, entry_input, evod):
        list1 = []
        list2 = []
        fulllist = []
        message = entry_input

        for x in evod[0]:
            list1.append(x)

        for x in evod[1]:
            list2.append(x)

        for x in list1:
            fulllist.append(x)

        for x in list2:
            fulllist.append(x)


        str1 = ''.join(str(e) for e in fulllist)
        return (str1)

    def the_rail_help3(self, entry_input, evod):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        fulllist = []
        message = entry_input

        for x in evod[0]:
            list1.append(x)

        for x in evod[1]:
            list2.append(x)

        for x in evod[2]:
            list3.append(x)

        for x in evod[3]:
            list4.append(x)


        for x in list1:
            fulllist.append(x)

        for x in list2:
            fulllist.append(x)

        for x in list3:
            fulllist.append(x)

        for x in list4:
            fulllist.append(x)


        str1 = ''.join(str(e) for e in fulllist)
        return (str1)

    def the_rail_help4(self, entry_input, evod):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        fulllist = []
        message = entry_input

        for x in evod[0]:
            list1.append(x)

        for x in evod[1]:
            list2.append(x)

        for x in evod[2]:
            list3.append(x)

        for x in evod[3]:
            list4.append(x)

        for x in evod[4]:
            list4.append(x)


        for x in list1:
            fulllist.append(x)

        for x in list2:
            fulllist.append(x)

        for x in list3:
            fulllist.append(x)

        for x in list4:
            fulllist.append(x)

        for x in list5:
            fulllist.append(x)

        str1 = ''.join(str(e) for e in fulllist)
        return (str1)
