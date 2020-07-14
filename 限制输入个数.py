'''
@File         : 
@version      : 
@Author       : Su Daozhen
@Date         : 2020-06-13 20:41:36
@LastEditors  : Su Daozhen
@LastEditTime : 2020-06-13 20:45:58
@Encoding     : UTF-8
@Description  : 
@Attention    : 
@********************COPYRIGHT 2020 Su Daozhen********************
'''
import tkinter as tk
from tkinter import *
root=tk.Tk()


string = tk.StringVar()

max_len = 1
def on_write(*args):
    s = string.get()
    if len(s) > max_len:
        string.set(s[:max_len])

string.trace_variable("w", on_write)

label=tk.Label(root,text="Phone Number:",font=20,bg="#33BEFF")
label.pack()


phno = tk.Entry(root, textvariable=string)
phno.pack()

root.mainloop()