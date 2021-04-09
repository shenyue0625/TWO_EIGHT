import cv2
# import card
# card._rank=int(input('Please input the rank of the card: '))
# card._suit=input('Please input the suits of the card: ')
# if card._rank==1 and card._suit=='spades':
#I = cv2.imread('C:/Users/xuyan/PycharmProjects/Two_Eight/PNG-cards-1.3/ace_of_spades.png')
#I = cv2.imread('ace_of_spades.png')
I = cv2.imread('ace_of_hearts.png')
#print (I.shape)

cv2.imshow('',I)

cv2.waitKey(0)
