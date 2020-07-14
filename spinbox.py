'''
@File         : 
@version      : 
@Author       : Su Daozhen
@Date         : 2020-06-13 20:15:20
@LastEditors  : Su Daozhen
@LastEditTime : 2020-06-13 20:30:48
@Encoding     : UTF-8
@Description  : 
@Attention    : 
@********************COPYRIGHT 2020 Su Daozhen********************
'''
import tkinter as tk

def keyPress(a):
    l = list(entry.get())
    for i in range(len(l) - 1, -1, -1):
        if not(48 <= ord(l[i]) <= 57 or ord(l[i]) == 46):
            entry.delete(i, i+1)
root = tk.Tk()
entry = tk.Entry(root)
entry.bind('<KeyRelease>', keyPress)
entry.pack() 
root.mainloop()