import string
s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "defghijklmnopqrstuvwxyzabc"
s3 = raw_input('map:')
print s3.translate(string.maketrans(s1,s2))
