f = open('1.txt','r')
txt =f.readlines()
string = []
for i in range(0,(len(txt))):
    for j in range(0,len(txt[i])):
        if (txt[i][j] >= 'a' and txt[i][j] <= 'z'):
            string.append(txt[i][j])
print ''.join(string)
