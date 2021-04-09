import tkinter

from PIL import Image as pImage

from PIL import ImageTk as pImageTk

from tkinter import *
#import tkinter as tk
#root=tk.Tk()
root=Tk()
root.geometry("800x800")
#w = Canvas(root, width=800,height=400)
#root.geometry('2000*1000')
#my_canvas = Canvas(root, width=600,height=100)
im1=pImage.open('ace_of_hearts.png')  #打开图片文件
im1 = im1.resize((100,100))#, Image.ANTIALIAS
im2=pImage.open('ace_of_spades.png')
im2 = im2.resize((150,150))
im3=pImage.open('ace_of_clubs.png')  #打开图片文件
im3 = im3.resize((100,100))
im4=pImage.open('ace_of_diamonds.png')
im4 = im4.resize((150,150))
p1=pImageTk.PhotoImage(im1)  #建立与tkinter适用的接口
p2=pImageTk.PhotoImage(im2)
p3=pImageTk.PhotoImage(im3)  #建立与tkinter适用的接口
p4=pImageTk.PhotoImage(im4)
Label1 = Label(root,image=p1, anchor='w')  #建立标签

Label2 = Label(root,image=p2, anchor="n")
Label3 = Label(root,image=p3, anchor="e")   #建立标签
Label4 = Label(root,image=p1, anchor='s')   #tkinter.S

Label1['image']=p1  #把图片放入标签
Label2['image']=p2
Label3['image']=p3 #把图片放入标签
Label4['image']=p4
Label1.image=p1  #这句话不可不放，否则影响及时更新
Label2.image=p2
Label3.image=p3 #这句话不可不放，否则影响及时更新
Label4.image=p4
# w.pack(pady=20)
# w.Label1['image'], w.Label2['image'], w.Label3['image'], w.Label4['image'] = p1, p2, p3, p4
#
# w.Label1.image, w.Label2.image, w.Label3.image, w.Label4.image = p1, p2, p3, p4
Label1.pack()
Label2.pack()
Label3.pack()
Label4.pack()

root.mainloop()







'''
from tkinter import *
import cv2
# import card
# card._rank=int(input('Please input the rank of the card: '))
# card._suit=input('Please input the suits of the card: ')
# if card._rank==1 and card._suit=='spades':
#    I = cv2.imread('C:/Users/xuyan/PycharmProjects/Two_Eight/PNG-cards-1.3/ace_of_spades.png')
I1 = cv2.imread('ace_of_spades.png')
I2 = cv2.imread('ace_of_hearts.png')
#import tkinter as tk
#root=tk.Tk()
root=Tk()
Label1 = Label(root)   #建立标签
Label2 = Label(root)

#print (I.shape)
p1=cv2.imshow('image',I1)
p2=cv2.imshow('image',I2)
Label1['image']=p1
Label2['image']=p2
#
# cv2.imshow('image',I1)
#cv2.waitKey(0)

Label1.image=p1
Label2.image=p2
Label1.pack()
Label2.pack()
root.mainloop()
#cv2.destroyAllWindows()
'''


