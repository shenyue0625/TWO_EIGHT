'''
Leaving load_imagge(), ImageTk.PhotoImage() disappear。
you need to add :root.mainloop()  at the end of load_image()!!!

'''
from PIL import Image as pImage
from PIL import ImageTk as pImageTk
from tkinter import messagebox
from tkinter import *
from hand import *
import deck as d
import str_real_card

def load_image():
    str_real_card.main()
    root.mainloop()  #you need to add :root.mainloop()  at the end of load_image()!!!
root = Toplevel()  #Tk()
root.geometry("400x200")
root.title('二-八 / TWO_EIGHT')
bt = Button(root,text="Deal Card",font=25,command=load_image).place(x=150,y=100)    #str_to_read    text='TWO_EIGHT',
#select_palyers = Label(root,text="Players Number (4/8)",font=25).place(x=60, y=100)
#select_palyers_input_area = Entry(root, width=20).place(x=240, y=100)
#bt.pack()
root.mainloop()
sys.stdout.flush()



