from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image, ImageGrab
from decimal import Decimal
import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract'

totalSum = 0
totaltotal = 0
def tesseractOCR (img):
    return pytesseract.image_to_string(img)


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def removeNoise(image):
    return cv2.medianBlur(image,5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def getSumFromClipboard():
    global totaltotal
    global totalSum
    totalSum = 0
    totaltotal = 0
    total = 0
    printSum = 0
    a = ""
    b=[]
    # img = Image.open('test3.png')
    im = ImageGrab.grabclipboard()
    try:
        if os.path.exists("/somefile.png"):
            os.remove("/somefile.png")
        im.save('somefile.png','PNG')
        displayError["text"] = ""
        op = cv2.imread('somefile.png')
        op = grayscale(op)
        # op = removeNoise(op)
        # op = thresholding(op)
        text = tesseractOCR(op)
        # print(text)
        a = text.replace(' ','').replace('.','').replace('~','-').split('\n')
        # print(a)
    except:
        displayError["text"] = "ERROR: The clipboard does not have a saved image to be used"
        totalSum = 0
        totaltotal = 0
    
    # text = pytesseract.image_to_string(op)
    # print(text)
    # a = text.replace(' ','').replace('.','').replace('~','-').split('\n')
    # print(a)
    printAllNumbers = ""
    if a != "":
        for val in a:
            try:
                b.append(Decimal(val.replace(',','.')))
                printAllNumbers+= str(val) + '\n'
                total+=1
            except:
                continue
    # text
    totaltotal = total
    try:
        if a != "":
            print(b)
            print(sum(b))
            totalSum = sum(b)
            printSum = str(totalSum).replace(',','')+"\nSummed: "+str(total)+" items"
            displaySum["text"] = printSum
            displayNumberSet["text"] = printAllNumbers+"\nTotal:"+str(total)
            displayNumberSet2["text"] = ""
        else:
            displaySum["text"] = ""
            displayNumberSet["text"] = ""
            displayNumberSet2["text"] = ""
    except:
        print("error end")
    # if os.path.exists("./somefile.png"):
    #     os.remove("somefile.png")
    # return(str(sum(b)),str("\nSummed: "),str(total))
def getSumFromClipboardAdd():
    global totalSum
    global totaltotal
    a = ""
    b=[]
    totals = 0
    # img = Image.open('test3.png')
    im = ImageGrab.grabclipboard()
    try:
        im.save('somefile2.png','PNG')
        displayError["text"] = ""
    except:
        displayError["text"] = "ERROR: The clipboard does not have a saved image to be used"
    if os.path.exists("somefile2.png"):
        op = cv2.imread('somefile2.png')
        op = grayscale(op)
        # op = removeNoise(op)
        # op = thresholding(op)
        # if cv2.imwrite( cv2image.jpg , op):
        #     print("saved")
        # windowName = 'image'
        # cv2.imshow(windowName , op)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        text = tesseractOCR(op)
    # print(text)
        a = text.replace(' ','').replace('.','').replace('~','-').split('\n')
    # print(a)
    
    printAllNumbers = ""
    if a != "":
        for val in a:
            try:
                b.append(Decimal(val.replace(',','.')))
                printAllNumbers+= str(val).replace(',','') + '\n'
                totals+=1
            except:
                continue
    # text
    
    if displayError["text"] == "":
        print(b)
        totalss = totals + totaltotal
        totalSum += sum(b)
        printSum = str(totalSum)+"\nSummed: "+str(totalss)+" items"
        displaySum["text"] = printSum
        displayNumberSet2["text"] = printAllNumbers+"\nTotal:"+str(totals)
        totalSum -= sum(b)
    if os.path.exists("somefile2.png"):
        os.remove("somefile2.png")

root= tk.Tk()
root.title('Clipboard sum') 
canvas1 = tk.Canvas(root, width = 800, height = 500)
canvas1.pack()


displaySum = tk.Label(root, text= "", fg='black', font=('helvetica', 12, 'bold'))
canvas1.create_window(500, 200, window=displaySum)

displayNumberSet = tk.Label(root, text="", fg='black', font=('helvetica', 12, 'bold'))
canvas1.create_window(220, 250, window=displayNumberSet)

displayNumberSet2 = tk.Label(root, text="", fg='black', font=('helvetica', 12, 'bold'))
canvas1.create_window(320, 250, window=displayNumberSet2)

displayError = tk.Label(root, text="", fg='red', font=('helvetica', 15, 'bold'))
canvas1.create_window(400, 470, window=displayError)

button1 = tk.Button(text='Sum',command=getSumFromClipboard, bg='green',fg='white', font = ('bold'))
canvas1.create_window(650, 150, window=button1)

button2 = tk.Button(text='Add',command=getSumFromClipboardAdd, bg='green',fg='white', font = ('bold'))
canvas1.create_window(650, 200, window=button2)

root.mainloop()