# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:35:56 2020

@author: pc
"""

import tkinter as tk
root=tk.Tk()
global num,num2,num3,num4,num5,num6,num7,count
num=0
num2=1
num3=1
num4=0
num5=0
num6=0
num7=0
global sign
sign=-1
count=0
root.title("simple calculator")
e=tk.Entry(root,width=42,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
def myclick(number1):
   
    current=e.get()
    e.delete(0,tk.END)
    e.insert(0,str(current)+str(number1))
   
def ClearClick():
    global num1,num
    e.delete(0,tk.END)
    num1=0
    num=0
def AddClick():
    global num
    global sign
    current1=e.get() 
    e.delete(0,tk.END)
    num+=float(current1)
    sign=0
def SubClick():
    global num4
    global sign,count
    current1=e.get()
    e.delete(0,tk.END)
    if count==0:
        num4=float(current1)
    else:
        num4-=float(current1) 
    count+=1    

    sign=1
def MultClick():
    global num,num3
    global sign
    current1=e.get()
    e.delete(0,tk.END)
    num3*=float(current1)
    sign=2
def DivideClick():
    global num6
    global sign,count
    current1=e.get()
    e.delete(0,tk.END)
    if count==0:
        num6=float(current1)
    else:
        num6/=float(current1) 
    count+=1
    print(num6)
    sign=3
def EqualClick(): 
    global sign
    global num,num2,num3,num4,num5,num6,num7,count
    current1=e.get()
    
    e.delete(0,tk.END)
    if sign==0:
        num1=num+float(current1)
        num=0
        e.insert(0,num1)
        
    elif sign==1:
        num5=num4-float(current1)
        num4=0
        count=0
        e.insert(0,num5)
        
    elif sign==2:
        num2=num3*float(current1)
        num3=1
        e.insert(0,num2)
    elif sign==3:
        num7=num6/float(current1)
        num6=0
        count=0
        e.insert(0,num7)
    #else:
     #   e.insert(0,int(current1))
 #   hello="hello"+e.get()
  #  #label1=Label(root,text=e.get())
   # label1=Label(root,text=hello)
#Defining Buttons#
Button1=tk.Button(root,text='1',padx=40,pady=20,command=lambda:myclick(1)) 
Button2=tk.Button(root,text='2',padx=40,pady=20,command=lambda:myclick(2)) 
Button3=tk.Button(root,text='3',padx=40,pady=20,command=lambda:myclick(3))
 
Button4=tk.Button(root,text='4',padx=40,pady=20,command=lambda:myclick(4)) 
Button5=tk.Button(root,text='5',padx=40,pady=20,command=lambda:myclick(5)) 
Button6=tk.Button(root,text='6',padx=40,pady=20,command=lambda:myclick(6)) 

Button7=tk.Button(root,text='7',padx=40,pady=20,command=lambda:myclick(7)) 
Button8=tk.Button(root,text='8',padx=40,pady=20,command=lambda:myclick(8)) 
Button9=tk.Button(root,text='9',padx=40,pady=20,command=lambda:myclick(9))
Button0=tk.Button(root,text='0',padx=40,pady=20,command=lambda:myclick(0))

Buttonequal=tk.Button(root,text='=',padx=40,pady=20,command=EqualClick)
Buttonclear=tk.Button(root,text='Clear',padx=30,pady=20,command=ClearClick)
Buttonadd=tk.Button(root,text='+',padx=38,pady=20,command=AddClick)
Buttonsub=tk.Button(root,text='-',padx=40,pady=20,command=SubClick)
ButtonMul=tk.Button(root,text='x',padx=39,pady=20,command=MultClick)
Buttondiv=tk.Button(root,text='/',padx=40,pady=20,command=DivideClick)
 #creating Buttons on the screen
Button1.grid(row=3,column=0)
Button2.grid(row=3,column=1)
Button3.grid(row=3,column=2)

Button4.grid(row=2,column=0)
Button5.grid(row=2,column=1)
Button6.grid(row=2,column=2)

Button7.grid(row=1,column=0)
Button8.grid(row=1,column=1)
Button9.grid(row=1,column=2)
Button0.grid(row=4,column=0)

Buttonadd.grid(row=4,column=1)
Buttonsub.grid(row=4,column=2)
ButtonMul.grid(row=3,column=3)
Buttondiv.grid(row=2,column=3)
Buttonequal.grid(row=4,column=3)
Buttonclear.grid(row=1,column=3)



#mybutton=Button(root,text="clickme!",state=DISABLED)
#mybutton=Button(root,text="clickme!",padx=50,command=myclick)
   
#mybutton=Button(root,text="Enter your name",padx=50,command=myclick,fg="blue",bg="red")
#mybutton.pack()
root.mainloop()
