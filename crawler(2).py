import re
import time
import json
import urllib.request
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
totallist = []
blanktrie = {
	'val':"helloworldstudio.org",
	'child':[]
}
def findlinks(link):
	p = re.compile("(href=\"\/[^\/\"][^\"]*\/\")")
	fp = urllib.request.urlopen("https://" + link)
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	m = p.findall(mystr)
	for x in range(len(m)):
		m[x] = "helloworldstudio.org" + m[x][6:len(m[x])-1]
	return m
def graphtriage(triage):
    for item in triage['child']:
        if item['child'] != None:
            G.add_node(item["val"])
            G.add_edge(triage['val'],item['val'])
            graphtriage(item)
            
def createtrie(site, trie):
	print (site)
	checker = True
	totallist.append(site)
	#time.sleep(61)
	try:
		links = findlinks(site)
	except:
		checker = False
		print("error")
	if checker:
		for item in links:
			dic = {
				'val' : item,
				'child' : []
			}
			trie['child'].append(dic)
			if item not in totallist:
				createtrie(item, trie['child'][len(trie['child'])-1])
createtrie("helloworldstudio.org", blanktrie)
with open("dict.json", 'w') as f:
  json.dump(blanktrie, f)


