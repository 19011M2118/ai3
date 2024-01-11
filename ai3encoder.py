from PIL import Image,ImageDraw
image = Image.new("RGB", (800,400),(255,255,255)) #creating the blank canvas
image1=ImageDraw.Draw(image)
#input_string=input("Enter a string: ")#The string to be encoded
input_string=("Abbas Cheddad")
input_string=input_string.lower()
dictionary={'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10, 'j': 11, 'k': 12, 'l': 13, 'm': 14, 'n': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27,' ':1}#keys are alphabets and values are widths
list1=[]#this list stores the widths of each character in the barcode
for i in input_string:#iterating through the input string
    if i in dictionary.keys():#If the string literal is a letter or a ' '
        list1.append(dictionary[i])
#print(list1)
x=9
for i in list1:#iterating through the string
    if i==1:
        for character in range(i):
            image1.line([(x+character,150),(x+character,250)],fill="black",width=1)#If the character has a width of 1 draw a line between rows 150 and 250
    else:
        for character in range(i):
            image1.line([(x+character,10),(x+character,350)],fill="black",width=1)#otherwise draw a line between rows 10 and 350    
    x+=i+9#standard spacing is 9
image.show()#show the image
image.save("Output.png")#save the image

