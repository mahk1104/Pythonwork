import tkinter as tk
a=dir(tk)
print(a)

from tkinter import*

win=Tk()
win.geometry("312x324")
win.title("Calculator")

def btn(item):
    global expression
    expression=expression + str(item)
    input_text.set(expression)

def btnclear():
    global expression
    expression=""
    input_text.set("")

def btnequal():
    try:
        global expression
        result=str(eval(expression))
        input_text.set(result)
        expression=""
    except:
 
        input_text.set(" Error. Enter a valid equation ")
        expression = ""
expression=""
input_text=StringVar()
input_frame=Frame(win,width=300,height=50,bd=0,highlightbackground="black",
                  highlightcolor="black",highlightthickness=2)
input_frame.pack(side=TOP)
input_field=Entry(input_frame,font=("arial",16,"bold"),textvariable=input_text,width=50
                  ,bg="#eee",bd=0,justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)
btns_frame=Frame(win,width="312",height="222",bg="grey")
btns_frame.pack()

clear=Button(btns_frame,text="C",fg="black",width=32,height=3,bd=0,bg="#eee",
             cursor="hand2",command=lambda:btnclear()
             ).grid(row=0,column=0,columnspan=3,padx=1,pady=1)

divide=Button(btns_frame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("/")
              ).grid(row=0,column=3,padx=1,pady=1)

seven=Button(btns_frame,text="7",fg="black",width=10,height=3,bd=0,bg="#fff",
              cursor="hand2",command=lambda:btn("7")
              ).grid(row=1,column=0,padx=1,pady=1)

eight=Button(btns_frame,text="8",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("8")
              ).grid(row=1,column=1,padx=1,pady=1)

nine=Button(btns_frame,text="9",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("9")
              ).grid(row=1,column=2,padx=1,pady=1)

multiply=Button(btns_frame,text="*",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("*")
              ).grid(row=1,column=3,padx=1,pady=1)

four=Button(btns_frame,text="4",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("4")
              ).grid(row=2,column=0,padx=1,pady=1)

five=Button(btns_frame,text="5",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("5")
              ).grid(row=2,column=1,padx=1,pady=1)
six=Button(btns_frame,text="6",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("6")
              ).grid(row=2,column=2,padx=1,pady=1)

minus=Button(btns_frame,text="-",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("-")
              ).grid(row=2,column=3,padx=1,pady=1)


one=Button(btns_frame,text="1",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("1")
              ).grid(row=3,column=0,padx=1,pady=1)

two=Button(btns_frame,text="2",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("2")
              ).grid(row=3,column=1,padx=1,pady=1)

three=Button(btns_frame,text="3",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("3")
              ).grid(row=3,column=2,padx=1,pady=1)

plus=Button(btns_frame,text="+",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("+")
              ).grid(row=3,column=3,padx=1,pady=1)

zero=Button(btns_frame,text="0",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn("0")
              ).grid(row=4,column=0,columnspan=2,padx=1,pady=1)

point=Button(btns_frame,text=".",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btn(".")
              ).grid(row=4,column=2,padx=1,pady=1)

equals=Button(btns_frame,text="=",fg="black",width=10,height=3,bd=0,bg="#eee",
              cursor="hand2",command=lambda:btnequal()
              ).grid(row=4,column=3,padx=1,pady=1)

win.mainloop()