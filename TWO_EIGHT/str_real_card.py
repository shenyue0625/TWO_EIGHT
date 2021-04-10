import tkinter

from PIL import Image as pImage

from PIL import ImageTk as pImageTk

from tkinter import *
from hand import *
import deck as d


# import tkinter as tk
# root=tk.Tk()
def str_to_read():  # This function is established to create four players with string cards in their hands.
    deck = d.Deck()  # create a deck.
    deck.shuffle()  # shuffle the deck using random function.
    h1 = Hand()
    h2 = Hand()
    h3 = Hand()
    h4 = Hand()
    h1rank = []
    h2rank = []
    h3rank = []
    h4rank = []
    h1suit = []
    h2suit = []
    h3suit = []
    h4suit = []
    h1ranksuit = []  # set up h1 list will be used for putting two cards in it.
    h2ranksuit = []
    h3ranksuit = []
    h4ranksuit = []
    for count in range(2):    # each hand has two number_cards.
        card1 = deck.deal_card()
        h1.add_card(card1)
        h1rank.append(int(card1._rank))
        h1suit.append(card1._suit)
        h1ranksuit.append(card1)
        card2 = deck.deal_card()
        h2.add_card(card2)
        h2rank.append(int(card2._rank))
        h2suit.append(card2._suit)
        h2ranksuit.append(card2)
        card3 = deck.deal_card()
        h3.add_card(card3)
        h3rank.append(int(card3._rank))
        h3suit.append(card3._suit)
        h3ranksuit.append(card3)
        card4 = deck.deal_card()
        h4.add_card(card4)
        h4rank.append(int(card4._rank))
        h4suit.append(card4._suit)
        h4ranksuit.append(card4)
    print('The cards in player1 are: ')
    for card in h1ranksuit:
        print(card)
    print('The cards in player2 are: ')
    for card in h2ranksuit:
        print(card)
    print('The cards in player3 are: ')
    for card in h3ranksuit:
        print(card)
    print('The cards in player4 are: ')
    for card in h4ranksuit:
        print(card)
    htotal=h1ranksuit+h2ranksuit+h3ranksuit+h4ranksuit # This is the list containing 8 cards.
    return htotal
    # for card in htotal:
    #     print(card)
    # print(type(htotal))
    # print(htotal[0])
    # file_name = str(str(htotal[0]) + '.' + 'png')
    # print(file_name)



def main():
    htotal=str_to_read()
    root = Toplevel() #Tk()
    root.geometry("800x800")
    cv = Canvas(root, bg='red', width=800, height=800)    #.place(1000,300)
    # w = Canvas(root, width=400,height=400,bg='blue')
    # root.geometry('2000*1000')
    # my_canvas = Canvas(root, width=600,height=100)
    # global image
    # global im1,im2,im3,im4,im5,im6,im7,im8
    file_name = str(str(htotal[0]) + '.' + 'png')  # This is a key step to link string card to real image card
    im1 = pImage.open(file_name)  # 打开图片文件  open image file
    im1 = im1.rotate(0)
    im1 = im1.resize((100, 100))  # , Image.ANTIALIAS
    file_name = str(str(htotal[1]) + '.' + 'png')  # This is a key step to link string card to real image card
    im2 = pImage.open(file_name)  # 打开图片文件
    # im2 = pImage.open('ace_of_spades.png')
    im2 = im2.resize((100, 100))
    im2 = im2.rotate(0)
    # im3 = pImage.open('2_of_clubs.png')  # 打开图片文件
    file_name = str(str(htotal[2]) + '.' + 'png')  # This is a key step to link string card to real image card
    im3 = pImage.open(file_name)  # 打开图片文件
    im3 = im3.resize((100, 100))
    # im4 = pImage.open('2_of_diamonds.png')
    file_name = str(str(htotal[3]) + '.' + 'png')  # This is a key step to link string card to real image card
    im4 = pImage.open(file_name)  # 打开图片文件
    im4 = im4.resize((100, 100))

    # im5 = pImage.open('2_of_hearts.png')
    file_name = str(str(htotal[4]) + '.' + 'png')  # This is a key step to link string card to real image card
    im5 = pImage.open(file_name)  # 打开图片文件

    im5 = im5.resize((100, 100))
    im5 = im5.rotate(-90) # rotate image -90 degree.
    # im6 = pImage.open('8_of_hearts.png')
    file_name = str(str(htotal[5]) + '.' + 'png')  # This is a key step to link string card to real image card
    im6 = pImage.open(file_name)  # 打开图片文件

    im6 = im6.resize((100, 100))
    im6 = im6.rotate(-90)       # rotate image -90 degree.
    # im7 = pImage.open('10_of_hearts.png')
    file_name = str(str(htotal[6]) + '.' + 'png')  # This is a key step to link string card to real image card
    im7 = pImage.open(file_name)  # 打开图片文件
    im7 = im7.resize((100, 100))
    im7 = im7.rotate(90)   # rotate image 90 degree.
    # im8 = pImage.open('10_of_spades.png')
    file_name = str(str(htotal[7]) + '.' + 'png')  # This is a key step to link string card to real image card
    im8 = pImage.open(file_name)  # 打开图片文件
    im8 = im8.resize((100, 100))
    im8 = im8.rotate(90)  # rotate image 90 degree.
    p1 = pImageTk.PhotoImage(im1)  # 建立与tkinter适用的接口
    p2 = pImageTk.PhotoImage(im2)
    p3 = pImageTk.PhotoImage(im3)  # 建立与tkinter适用的接口
    p4 = pImageTk.PhotoImage(im4)
    p5 = pImageTk.PhotoImage(im5)  # 建立与tkinter适用的接口
    p6 = pImageTk.PhotoImage(im6)
    p7 = pImageTk.PhotoImage(im7)  # 建立与tkinter适用的接口
    p8 = pImageTk.PhotoImage(im8)
    # p1 = im1 # 建立与tkinter适用的接口
    # p2 = im2
    # p3 = im3  # 建立与tkinter适用的接口
    # p4 = im4
    # p5 = im5  # 建立与tkinter适用的接口
    # p6 = im6
    # p7 = im7 # 建立与tkinter适用的接口
    # p8 = im8
    cv.create_image((350, 50), image=p1) # put card in a certain place of canvas.
    cv.create_image((450, 50), image=p2) # put card in a certain place of canvas.
    cv.create_image((350, 750), image=p3) # put card in a certain place of canvas.
    cv.create_image((450, 750), image=p4) # put card in a certain place of canvas.
    cv.create_image((50, 350), image=p5) # put card in a certain place of canvas.
    cv.create_image((50, 450), image=p6)  # put card in a certain place of canvas.
    cv.create_image((750, 350), image=p7) # put card in a certain place of canvas.
    cv.create_image((750, 450), image=p8) # put card in a certain place of canvas.
    cv.pack()
    # bt = Button(root,text="Deal Card",font=25).place(x=550,y=850)  #str_real_card command=self.main(),command=load_card
    # select_palyers = Label(root,text="Players Number (4/8)",font=25).place(x=20, y=850)
    # select_palyers_input_area = Entry(root, width=50).place(x=180, y=850)

    #bt.pack()
    root.mainloop()
    sys.stdout.flush()


if __name__ == "__main__":
    main()

'''
The cards in player1 are: 
2_of_hearts
7_of_spades
The cards in player2 are: 
10_of_diamonds
5_of_clubs
The cards in player3 are: 
5_of_spades
4_of_diamonds
The cards in player4 are: 
10_of_clubs
6_of_diamonds

'''







