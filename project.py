# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:25:36 2022

@author: ANJAN
"""

# import tkinter module
from tkinter import *
# import other necessery modules
import random
# modules for encryption and decryption
import base64
import onetimepad
import pyDes
import modules

# creating root object
root = Tk()

# defining size of window
root.geometry("12000x6000")

# setting up the title of window
root.title("Message Encryption and Decryption")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=LEFT)

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
                text="MULTI-LAYERED \n ENCRYPTION AND DECRYPTION",
                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

# Initializing variables
Msg = StringVar()
mode = StringVar()
Result = StringVar()

# labels for the message
lblMsg = Label(f1, font=('arial', 16, 'bold'),
                text="MESSAGE", bd=16, anchor="w")

lblMsg.grid(row=1, column=0)
# Entry box for the message
txtMsg = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=Msg, bd=10, insertwidth=4,
                bg="powder blue", justify='right')


txtMsg.grid(row=1, column=1)

# labels for the mode
lblmode = Label(f1, font=('arial', 16, 'bold'),
                text="MODE(e for encrypt, d for decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=3, column=0)
# Entry box for the mode
txtmode = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="powder blue",)

txtmode.grid(row=3, column=1)

# labels for the result
lblResult = Label(f1, font=('arial', 16, 'bold'),
                text="The Result-", bd=16, anchor="w")

lblResult.grid(row=2, column=2)

# Entry box for the result
txtResult = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=Result, bd=10, insertwidth=4,
                bg="powder blue",)

txtResult.grid(row=2, column=3)


def Results():
    # print("Message= ", (Msg.get()))

    msg = Msg.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(str(modules.encoding(msg)))
    else:
        Result.set(modules.decoding(msg))

# exit function

def qExit():
    root.destroy()

# Function to reset the window

def Reset():

    Msg.set("")
    mode.set("")
    Result.set("")


# Show message button
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                    font=('arial', 16, 'bold'), width=10,
                    text="Show Message", bg="powder blue",
                    command=Results).grid(row=7, column=1)

# Reset button
btnReset = Button(f1, padx=16, pady=8, bd=16,
                    fg="black", font=('arial', 16, 'bold'),
                    width=10, text="Reset", bg="green",
                    command=Reset).grid(row=7, column=2)

# Exit button
btnExit = Button(f1, padx=16, pady=8, bd=16,
                    fg="black", font=('arial', 16, 'bold'),
                    width=10, text="Exit", bg="red",
                    command=qExit).grid(row=7, column=3)

# keeps window alive
root.mainloop()