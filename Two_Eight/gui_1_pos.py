import tkinter

from PIL import Image as pImage

from PIL import ImageTk as pImageTk

from tkinter import *
# from hand import *
# import deck as d
#import tkinter as tk
#root=tk.Tk()
def main():
    # deck = d.Deck()
    # deck.shuffle()
    # h1 = Hand()
    # h2 = Hand()
    # h3 = Hand()
    # h4 = Hand()
    # h1rank = []
    # h2rank = []
    # h3rank = []
    # h4rank = []
    # h1suit = []
    # h2suit = []
    # h3suit = []
    # h4suit = []
    # for count in range(2):
    #     card1 = deck.deal_card()
    #     h1.add_card(card1)
    #     h1rank.append(int(card1._rank))
    #     h1suit.append(card1._suit)
    #     card2 = deck.deal_card()
    #     h2.add_card(card2)
    #     h2rank.append(int(card2._rank))
    #     h2suit.append(card2._suit)
    #     card3 = deck.deal_card()
    #     h3.add_card(card3)
    #     h3rank.append(int(card3._rank))
    #     h3suit.append(card3._suit)
    #     card4 = deck.deal_card()
    #     h4.add_card(card4)
    #     h4rank.append(int(card4._rank))
    #     h4suit.append(card4._suit)
    root=Tk()
    root.geometry("800x800")
    cv=Canvas(root,bg='red',width=800,height=800)
    #w = Canvas(root, width=400,height=400,bg='blue')
    #root.geometry('2000*1000')
    #my_canvas = Canvas(root, width=600,height=100)
    im1=pImage.open('8_of_hearts.png')  #打开图片文件
    im1 = im1.resize((100,100))#, Image.ANTIALIAS
    im2=pImage.open('ace_of_spades.png')
    im2 = im2.resize((100,100))
    im3=pImage.open('2_of_clubs.png')  #打开图片文件
    im3 = im3.resize((100,100))
    im4=pImage.open('2_of_diamonds.png')
    im4 = im4.resize((100,100))

    im5=pImage.open('2_of_hearts.png')
    im5 = im5.resize((100,100))
    im6=pImage.open('8_of_hearts.png')
    im6 = im6.resize((100,100))


    im7=pImage.open('10_of_hearts.png')
    im7 = im7.resize((100,100))
    im8=pImage.open('10_of_spades.png')
    im8 = im8.resize((100,100))



    p1=pImageTk.PhotoImage(im1)  #建立与tkinter适用的接口
    p2=pImageTk.PhotoImage(im2)
    p3=pImageTk.PhotoImage(im3)  #建立与tkinter适用的接口
    p4=pImageTk.PhotoImage(im4)
    p5=pImageTk.PhotoImage(im5)  #建立与tkinter适用的接口
    p6=pImageTk.PhotoImage(im6)
    p7=pImageTk.PhotoImage(im7)  #建立与tkinter适用的接口
    p8=pImageTk.PhotoImage(im8)
    cv.create_image((350,50),image=p1)
    cv.create_image((450,50),image=p2)
    cv.create_image((350,750),image=p3)
    cv.create_image((450,750),image=p4)
    cv.create_image((50,350),image=p5)
    cv.create_image((50,450),image=p6)
    cv.create_image((750,350),image=p7)
    cv.create_image((750,450),image=p8)
    cv.pack()
    root.mainloop()
    sys.stdout.flush()

if __name__ == "__main__":
    main()

'''


'''







