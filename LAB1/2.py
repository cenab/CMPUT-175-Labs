def arrangeLists(text):
    newlist = []
    names =[]
    infoList = []
    for line in range(13):
        list = []
        list2 = []
        info = []
        earthquakeline = text.readline()
#    split = earthquakeline.split(' ', 6)
#    split[6] = split[6].replace("\n", "")
        split = earthquakeline.split()
        name = split.pop()
        info.append(split[1]) ; info.append(split[0]) ; list.append(name) ; list2.append(info) ; list.append(list2)
        newlist.append(list)
        names.append(name)
        infoList.append(list2)
    return newlist, names, infoList

def arrangeDictionary(newlist, names, infoList):
    dictionary = dict()
    for num in range(len(newlist)):
        if names[num] in dictionary:
            dictionary[names[num]].append(infoList[num][0])
        else:
            dictionary[names[num]] = infoList[num]
    return dictionary

def dictionary2list(dictionary):
    for key, value in dictionary.items():
        lastlist = []
        lastlist.append(key)
        for date in value:
            lastlist.append(date)
        print(lastlist)
        print("\n")
    return
#print(dict)
def main():
    earthquake = open("earthquake.txt", "r")
    newlist, names, infoList = arrangeLists(earthquake)
    dictionary = arrangeDictionary(newlist, names, infoList)
    dictionary2list(dictionary)
#    print(dictionary2list(dictionary))
    earthquake.close()

main()
