#!/usr/bin/python3



import random


life = 9
rand = random.randint (1,100)

while life>1:
    valeur = int (input ("Entrer votre numéro.."))
    if valeur > rand:
        print ("plus petit")
        life = life - 1
    elif valeur > rand:
        print ("plus grand")
        life = life - 1
    else:
        print ("Gagné")
    break

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
fenetre = Tk()
label = Label(fenetre, text="Hello World")
label.pack()
textbox = Label(fenetre,text = "Hello")
label.pack()
fenetre.mainloop()

