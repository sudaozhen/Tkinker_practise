import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

e = tk.Entry(window,show=None)
#e = tk.Entry(window,show='*')   #显示*
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert('end',var)   #在末尾插入
#    t.insert(1.1,var)   #在1行1列插入

b1 = tk.Button(window, text='insert point', width=15, height=2,command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', width=15, height=2,command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()