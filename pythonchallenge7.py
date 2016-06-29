import Image
pic = Image.open("oxygen.png")
x,y = pic.size
for j in range(0,y,9):
    for i in range(0,x,7):
        pix = pic.getpixel((i,j))
        if pix[0]==pix[1]==pix[2]:
            print chr(pix[0]),
p = [105,110,116,101,103,114,105,116,121]
for i in p:
    print chr(i),
