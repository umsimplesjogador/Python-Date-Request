import tkinter as tk 
from tkinter import *
import random
from tkinter import messagebox


root = tk.Tk()
root.title('Aceitas, baleia?')
root.geometry('600x600')
root.configure(background='#ffc8dd')


def move_buton_1(e):
    if abs(e.x - button_1.winfo_x()) < 80 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)


def accepted():
    messagebox.showinfo(
        'Meu amor', 'minha juca gorda, eu te amo muito, rango mais tarde?')
    

def denied():
    button_1.destroy()


margin = Canvas(root, width=500, bg='#ffc8dd', height=100,
                bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#ffc8dd', text= 'Quer namorar comigo, baleia?',
                fg='#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não, seu maluco!', bg='#ffb3c1', command=denied,
                     relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
root.bind('<Motion>', move_buton_1)
button_2 = tk.Button(root, text='Sim, meu gostoso!', bg='#ffb3c1', relief=RIDGE,
                     bd=3, command=accepted, font=('Montserrat', 14, 'bold'))
button_2.pack()


root.mainloop()