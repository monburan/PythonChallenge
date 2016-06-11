import urllib2
import re
string = []
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
page = urllib2.urlopen(url).read()
info = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]',re.S)
key = info.findall(page)
for i in range(0,(len(key))):
    string.append(key[i][4:5])
print ''.join(string)

