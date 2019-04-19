def unzip(listtuples):
    list1 =[]
    list2 =[]
    for i in range(len(listtuples)):
        x = listtuples[i][0]
        list1.append(x)
    for i in range(len(listtuples)):
        y = listtuples[i][1]
        list2.append(y)
    tuple = (list1, list2)
    return tuple
if __name__ == '__main__':
    print(unzip([(1,4),(2,5),(3,6)]))
