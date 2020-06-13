import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

#不要在同个窗口同时使用pack和grid

   
# tk.Button(window, text='hit me').pack(side='top')
# tk.Button(window, text='hit me').pack(side='bottom')
# tk.Button(window, text='hit me').pack(side='left')
# tk.Button(window, text='hit me').pack(side='right')


# for i in range(4):
#     for j in range(3):   #放置4行3列
#         tk.Button(window, text='hit me').grid(row=i, column=j)
#         tk.Button(window, text='hit me').grid(row=i, column=j, ipadx=10, ipady=10)
#         tk.Button(window, text='hit me').grid(row=i, column=j, padx=10, pady=10)

tk.Button(window, text='hit me').place(x=10, y=100, anchor='nw')



window.mainloop()