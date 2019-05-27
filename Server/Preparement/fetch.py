from http import client
from html.parser import HTMLParser
from html.entities import name2codepoint

class FetchHrefParser(HTMLParser):

	list = []

	def handle_starttag(self, tag, attrs):
		if tag == 'a' :
			for attr in attrs:
				if attr[0] == 'href' :
					s = attr[1]
					if s[0:4] != 'http' and s != 'Poetry/sonnets.html' and s != 'news.html':
							self.list.append(s)
					
	def fetch(self, html):
		self.list = []
		self.feed(html)
		return self.list

parser = FetchHrefParser()

class FetchContentParser(HTMLParser):
	
	res = ""
	
	def handle_data(self, data):
		self.res += data + ' '
	
	def handle_starttag(self, tag, attrs):
		if tag == 'br':
			self.res += '\n'
	
	def fetch(self, html):
		self.res = ""
		self.feed(html)
		return self.res
crawler = FetchContentParser()

cnt = 0;
lp = open('list.txt', 'w+')

conn = client.HTTPConnection("shakespeare.mit.edu")
conn.request("GET", "/")

index = conn.getresponse()
if index.status != 200 :
	print("Returned " + str(index.status) + "(" + index.reason + "), failed when crawling index")
	exit()
	
print("Index fetched.")

html = index.read().decode('utf-8')
list = parser.fetch(html)

# Fetch Normal

for url in list:
	cnt = cnt + 1
	id = str(cnt)
	
	if url[-10:] == 'index.html' :
		url = url[:-10] + 'full.html'
	
	conn = client.HTTPConnection("shakespeare.mit.edu")
	conn.request("GET", '/' + url)
	
	
	print(id + ": " + url)
	lp.write(id + ": " + url + '\n')
	
	content = conn.getresponse()
	if content.status != 200 :
		print("Returned " + str(content.status) + "(" + content.reason + "), failed when crawling index")
		exit()
	
	html2 = content.read().decode('utf-8')
	text = crawler.fetch(html2)
	conn.close()
	
	fp = open('test' + id +".txt", 'w+')
	fp.write(text)
	fp.close()

# Fetch Sonnets

conn = client.HTTPConnection("shakespeare.mit.edu")
conn.request("GET", "/Poetry/sonnets.html")

index = conn.getresponse()
if index.status != 200 :
	print("Returned " + str(index.status) + "(" + index.reason + "), failed when crawling index")
	exit()


print("Sonnets Index fetched.")

html = index.read().decode('utf-8')
list = parser.fetch(html)

for url in list:
	cnt = cnt + 1
	id = str(cnt)
	
	conn = client.HTTPConnection("shakespeare.mit.edu")
	conn.request("GET", '/Poetry/' + url)
	
	print(id + ": " + url)
	lp.write(id + ": " + url + '\n')
	
	content = conn.getresponse()
	if content.status != 200 :
		print("Returned " + str(content.status) + "(" + content.reason + "), failed when crawling index")
		exit()
	
	html2 = content.read().decode('utf-8')
	text = crawler.fetch(html2)
	conn.close()
	
	fp = open('test' + id +".txt", 'w+')
	fp.write(text)
	fp.close()

