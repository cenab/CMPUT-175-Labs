def arrangeDictionary(rainfall):
    dictionary = dict()
    for line in range(25):
        rainfallline = rainfall.readline()
        split = rainfallline.split()
        dictionary[split[0]] = float(split[1])
    return dictionary

def capitalize_keys(d):
#https://stackoverflow.com/questions/9700399/how-can-i-change-keys-in-a-dictionary-to-upper-case-and-add-values-of-the-same-k
    result = {}
    for key, value in d.items():
        upper_key = key.upper()
        result[upper_key] = result.get(upper_key, 0) + value
    return result

def writeDictionary(dictionary, rainfallfmt, catagories):
    #rainfallfmt.write("51-60 GROUP\n")
    for key, value in dictionary.items():
        if value > catagories[0] and catagories[1] >= value:
            rainfallfmt.write("%25s %5.1f \n"%(key.center(25), value))
    rainfallfmt.write("\n")
    #rainfallfmt.write("61-70 GROUP\n")
    for key, value in dictionary.items():
        if value > catagories[1] and catagories[2] >= value:
            rainfallfmt.write("%25s %5.1f \n"%(key.center(25), value))
    rainfallfmt.write("\n")
    #rainfallfmt.write("71-80 GROUP\n")
    for key, value in dictionary.items():
        if value > catagories[2] and catagories[3] >= value:
            rainfallfmt.write("%25s %5.1f \n"%(key.center(25), value))
    rainfallfmt.write("\n")
    #rainfallfmt.write("81-90 GROUP\n")
    for key, value in dictionary.items():
        if value > catagories[3] and catagories[4] >= value:
            rainfallfmt.write("%25s %5.1f \n"%(key.center(25), value))
    rainfallfmt.write("\n")
    #rainfallfmt.write("91-100 GROUP\n")
    for key, value in dictionary.items():
        if value > catagories[4] and catagories[5] >= value:
            rainfallfmt.write("%25s %5.1f \n"%(key.center(25), value))

def main():
    catagories =[50.00, 60.00, 70.00, 80.00, 90.00, 100.00]
    rainfall = open("rainfall.txt", "r")
    rainfallfmt = open("rainfallfmt.txt", "w")
    dictionary = arrangeDictionary(rainfall)
    dictionary = capitalize_keys(dictionary)
    writeDictionary(dictionary, rainfallfmt, catagories)
    rainfall.close()
    rainfallfmt.close()

main()
