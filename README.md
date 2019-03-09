# HelloWorld-Web-Crawler
A Web Crawler to crawl the Hello World Website

#Scraping the Wepage
For any web crawler, the first step is accesing the webpage. I used urllib in order to get the webpage HTML code. Then, I had to get the links off that webpage. I did that using regular expression to look for links that were internal, and not to outside webpages  

#Mapping the Webpage
I chose to use a trie to store the map of the webpage. Each trie node contained the pages it liked to as its children; however, in order to eliminate repeates, I did not build children for webpages that already had children somewhere else in the trie. After creating the trie, I saved it as a dictionary in a JSON File

#Visualizing the Webpage
The final step was to visualize the Webpage, which I did using NetworkX. I first loaded my previously saved JSON file with the trie. I then used recursion to create a NetworkX graph by creating a node for every parent, adding edges between the parent and its children, then calling the same function on the children. Finally, after creating the graph, I displayed it using settings I liked

Made while working with Hello World Studio
