from PIL import Image,ImageDraw
import numpy
image1=numpy.array(Image.open("Output.png"))#This is the image that the encoder generated
image=numpy.array(Image.open("841924.png"))#This is the image I was given to be decoded
def decode(image):
    dictionary={'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10, 'j': 11, 'k': 12, 'l': 13, 'm': 14, 'n': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27,' ':1}#keys are alphabets and values are widths
    value_list=list(dictionary.values())
    key_list=list(dictionary.keys())
    list1=[]
    position=0#initially the position is 0
    while position<800:#while position is less than the width of the canvas
        R=image[200,position]#accessing row 200, change this to RGB for a different png other than the one that is provided
        count=0
        while R.all()==0: #while the pixel is black
            count=count+1#this counts the width of each bar
            position=position+1#for each bar the postion is incremented by one
            R=image[200,position]
        if count in dictionary.values():#if the width is in the dictionary, we append it to the list
            position1=value_list.index(count)
            list1.append(key_list[position1])
        position=position+1
    separator=''
    result=separator.join(list1)#This is for printing it in a line
    print(result)
decode(image1)#The image the encoder generated
decode(image)#The image that I got from the website