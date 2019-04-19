import urllib.request

url = 'https://docs.python.org/3/tutorial/'
htmllist = []
response = urllib.request.urlopen(url)
dictionary = dict()
html = response.readline()
html = html.decode("utf-8")
htmllist.append(html)
while html != '':
    html = response.readline()
    html = html.decode("utf-8")
    if "<a href=" in html:
        htmllist.append(html)
#print(dictionary)
list = []
list2 = []
for i in range(len(htmllist)):
    htmllist[i] = htmllist[i].replace("<a href=", "")
    htmllist[i] = htmllist[i].replace("title=", "")
    htmllist[i] = htmllist[i].replace("          ", "")
    list = htmllist[i].split(' ', 1)
    if len(list) == 2:
        if '' not in list:
            list2.append(list)
    for i in range(len(list2)):
        dictionary[list2[i][0]] = list2[i][1]

print(dictionary)
