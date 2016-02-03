import urllib
import urllib2

url = "http://espncricinfo.com/australia-v-india-2015-16/engine/match/895821.html?innings=2;page=1;shdr=none;view=commentary;wrappertype=none";
response = urllib2.urlopen(url)
html = response.read()
lines = html.split('\n')
for line in lines:
	print line
	print 'test'

