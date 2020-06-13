import tkinter as tk
import tkinter.messagebox  #调用messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    #tk.messagebox.showinfo(title='Hi', message='haha')
    #tk.messagebox.showwarning(title='Hi', message='haha')
    #tk.messagebox.showerror(title='Hi', message='haha')
    #print(tk.messagebox.askquestion(title='Hi', message='haha') )   #return 'yes'/'no'
    #print(tk.messagebox.askyesno(title='Hi', message='haha') )   #return 'Ture'/'False'
    print(tk.messagebox.askretrycancel(title='Hi', message='haha') )   #return 'Ture'/'False'
    #print(tk.messagebox.askokcancel(title='Hi', message='haha') )   #return 'Ture'/'False'
   
tk.Button(window, text='hit me',command=hit_me).pack()


window.mainloop()