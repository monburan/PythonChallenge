import pickle

pfile = open("banner.p")
data = pickle.load(pfile)
for line in data:
    for string in line:
         print ''.join(string[0] * string[1]),
    print ''
