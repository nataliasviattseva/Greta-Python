from tkinter import *
from tkinter import ttk
import random


def add_photo():
    global photo_image
    photo_image = PhotoImage(file="image.gif")
    label_image = Label(cadre_1, image=photo_image)
    label_image.pack(side=TOP, padx=10, pady=10)

def change_smile():
    global img
    fenetre.update()
    values = ['smile-1.png', 'smile-2.png', 'smile-2.png']
    img = PhotoImage(file=random.choice(values))
    label = Label(cadre_2, image=img, anchor='c')
    label.pack(padx=10, pady=10)


fenetre = Tk()
fenetre.geometry("600x300")

cadre_1 = Frame(fenetre, width=320, height=300, bg="red", borderwidth=4, relief=GROOVE)
cadre_1.propagate(False)
cadre_1.pack(side=LEFT)

Button(cadre_1, text="Afficher l'image", command=add_photo).pack(side=TOP, padx=10, pady=10)

cadre_2 = Frame(fenetre, width=320, height=300, bg="red", borderwidth=4, relief=GROOVE)
cadre_2.propagate(False)
cadre_2.pack(side=LEFT)

button = Button(cadre_2, text="Set", command=change_smile)
button.pack(side=TOP, padx=10, pady=10)
Button(cadre_2)

# current_var = StringVar()
# combobox = ttk.Combobox(cadre_2, textvariable=current_var)
# combobox['values'] = ('1', '2', '3')
# button.bind("<<ComboboxSelected>>", change_smile)
# combobox.pack()
fenetre.mainloop()
