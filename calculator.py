from tkinter import *

a = {
    'fg' : "orange",
    'bg' : 'black',
    'activebackground' : 'black',
    'font' : ("",50),
    'relief' : 'sunken'
}

def insert(n):
    ent.insert(END,n)

def clear():
    ent.delete(0,END)

def clear1():
    tool = len(ent.get())
    ent.delete(tool-1 , END)

def mosavi():
    try:
        res = eval(ent.get())
        clear()
        ent.insert(0 , res)
    except:
        clear()
        ent.insert(0 , 'Error')

root = Tk()
root.title("nanvaee")
root.resizable(0,0)
root.config(background='#494a4a')

ent = Entry(root, font=("",30), fg="white", bg="#333333")

label = Label(root, text="Error", cnf=a)

btn0       = Button(root, text="0"   , cnf=a, command=lambda:insert('0'))
btn00      = Button(root, text="00"  , cnf=a, command=lambda:insert('00'))
btn000     = Button(root, text="000" , cnf=a, command=lambda:insert('000'))
btn1       = Button(root, text="1"   , cnf=a, command=lambda:insert('1'))
btn2       = Button(root, text="2"   , cnf=a, command=lambda:insert('2'))
btn3       = Button(root, text="3"   , cnf=a, command=lambda:insert('3'))
btn4       = Button(root, text="4"   , cnf=a, command=lambda:insert('4'))
btn5       = Button(root, text="5"   , cnf=a, command=lambda:insert('5'))
btn6       = Button(root, text="6"   , cnf=a, command=lambda:insert('6'))
btn7       = Button(root, text="7"   , cnf=a, command=lambda:insert('7'))
btn8       = Button(root, text="8"   , cnf=a, command=lambda:insert('8'))
btn9       = Button(root, text="9"   , cnf=a, command=lambda:insert('9'))
btnmosavi  = Button(root, text="="   , cnf=a, command=mosavi)
btnpusitiv = Button(root, text="+"   , cnf=a, command=lambda:insert('+'))
btnnegetiv = Button(root, text="-"   , cnf=a, command=lambda:insert('-'))
btnzarb    = Button(root, text="x"   , cnf=a, command=lambda:insert('*'))
btntaghsim = Button(root, text="÷"   , cnf=a, command=lambda:insert('/'))
btnnogh    = Button(root, text="."   , cnf=a, command=lambda:insert('.'))
btnAC      = Button(root, text="AC"  , cnf=a, command=clear)
btnback    = Button(root, text="←" , cnf=a, command=clear1)

ent.grid(row=1,column=1,columnspan=100,sticky='news')

btn0.grid(row=5,column=1)
btn00.grid(row=5,column=2,columnspan=2,sticky="news")
btn000.grid(row=5,column=4,columnspan=3,sticky='news')
btn1.grid(row=4,column=1)
btn2.grid(row=4,column=2)
btn3.grid(row=4,column=3)
btn4.grid(row=3,column=1)
btn5.grid(row=3,column=2)
btn6.grid(row=3,column=3)
btn7.grid(row=2,column=1)
btn8.grid(row=2,column=2)
btn9.grid(row=2,column=3)
btnmosavi.grid(row=4,column=6,sticky='news')
btnpusitiv.grid(row=2,column=4,rowspan=2,sticky='news')
btnnegetiv.grid(row=4,column=4,sticky='news')
btnzarb.grid(row=2,column=5)
btntaghsim.grid(row=3,column=5,sticky='news')
btnnogh.grid(row=4,column=5,sticky='news')
btnAC.grid(row=2,column=6)
btnback.grid(row=3,column=6,sticky='news')

mainloop()