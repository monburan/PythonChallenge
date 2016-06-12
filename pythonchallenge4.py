import urllib2
import re
bingo = True
num = "12345"
i = 1
while bingo:       
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + num
    page = urllib2.urlopen(url).read()
    if page == 'Yes. Divide by two and keep going.':
        num = str(int(num)/2)
        print 'running:%d,num:%s'%(i,num)
        i += 1
    else:
        num = (re.compile("nothing is (\d{5}|\d{4}|\d{3})",re.S)).search(page)
        if num != None:
            num = num.group(1)
            print 'running:%d,num:%s'%(i,num)
            i += 1
        else:
            print 'find page like this:' + page
            bingo = False
