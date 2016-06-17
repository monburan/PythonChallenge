import zipfile
import re
bingo = True
lists = []
z = zipfile.ZipFile('channel.zip','r')
filename = '90052.txt'
while bingo:
    num = (z.namelist()).index(filename)
    line = z.read(z.namelist()[num])
    lists.append(z.getinfo(filename).comment)
    num = re.search(re.compile('(\d{5}|\d{4}|\d{3}|\d{2})',re.S),line)
    if num != None:
        filename = num.group(0)+'.txt'
    else:
        print 'find this : ' + line
        bingo = False

print ''.join(lists)
