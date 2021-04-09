import card
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
card._rank=int(input('Please input the rank of the card: '))
card._suit=input('Please input the suits of the card: ')
if card._rank==1 and card._suit=='spades':
   img = Image.open('C:/Users/xuyan/PycharmProjects/Two_Eight/PNG-cards-1.3/ace_of_spades.png')  # This is an open way to a certain folder.
   #img = Image.open('ace_of_spades.png')
   plt.imshow(img)  # make sure it is gray image
   plt.show()



