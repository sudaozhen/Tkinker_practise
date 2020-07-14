import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas = tk.Canvas(window,bg='blue',height=100,width=200)
image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
#  nw 以图片的左上角为基点，放在0，0坐标。
#  nw        n        ne
#
#   w      center     e
#
#  sw        s        se


x0,y0,x1,y1 = 50, 50, 80, 80

line = canvas.create_line(x0, y0, x1, y1)   #画直线，从x0,y0 到x1，y1

oval = canvas.create_oval(x0, y0, x1, y1+10, fill='red') #画椭圆，填充红色
#x1=y1为圆

arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
#画扇形，从0度到180度

rect = canvas.create_rectangle(100, 30, 100+20, 30+20)      #画矩形

canvas.pack()

def moveit():
    canvas.move(rect, 0, 2) #移动矩形

b = tk.Button(window, text='move', command=moveit).pack()


window.mainloop()
