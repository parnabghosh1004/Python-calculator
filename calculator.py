from tkinter import *
import math as m
from math import pi,nan,e 
root = Tk()
root.title('Calculator by Parnab')
root.wm_iconbitmap('calci.ico')
a = ''
rad = True
def all_children (window) :
    _list = window.winfo_children()
    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    return _list

def sin(x):
    if rad==False:
        x = (x*pi)/180    
    if x%pi==0:
        return 0
    elif (x/(pi/2))%4==1:
        return 1
    elif (x/(pi/2))%4==3:
        return -1
    else:
        return m.sin(x)
def cos(x):
    if rad==False:
        x = (x*pi)/180
    if x%(pi/2)==0 and x%pi!=0:
        return 0
    elif (x/pi)%2==0:
        return 1
    elif (x/pi)%2==1:
        return -1
    else:
        return m.cos(x)
def tan(x):
    if rad==False:
        x = (x*pi)/180
    if x%pi==0:
        return 0
    elif x%(pi/2)==0 and x%pi!=0:
        return nan
    else:
        return m.tan(x)
def log(x):
    return m.log10(x)
def ln(x):
    return m.log(x,e)    
def sqrt(x):
    return m.sqrt(x)
def fact(x):
    return m.factorial(x)
def more():
    widget_list = all_children(root)
    for item in widget_list:
        item.pack_forget()

    def click1(event):
        global a,rad
        text = event.widget.cget('text')
        if text in ['*','%','/','-','+']: 
            sc1value.set(text)
            s1.update()
            a +=text
            sc2value.set(a)
            s2.update()     
        elif text in ['1','2','3','4','5','6','7','8','9','0','.','sin','cos','tan','(',')','pi','e','log','ln','sqrt']:
            a +=text
            sc2value.set(a)
            s2.update()
        elif text=='1/x':
            a+='1/'
            sc2value.set(a)
            s2.update()
        elif text=='x!':
            a +='fact'
            sc2value.set(a)
            s2.update()
        elif text=='deg':
            rad = False
            angle['text'] = 'rad'
        elif text=='rad':
            rad = True
            angle['text'] = 'deg'    
        elif text=='=':
            try:
                sc1value.set('Ans.')
                sc2value.set(eval(a))
                s1.update()
                s2.update()
                a = ''
            except:
                sc1value.set('')
                sc2value.set('error')
                s1.update()
                s2.update()
                a= ''
        elif text=='X':
            a = a[:-1]
            sc2value.set(a)
            s2.update()                
        elif text=='AC':
            sc1value.set('')
            sc2value.set('0')
            s1.update()
            s2.update()
            a = ''
    root.geometry('740x650')
    root.minsize(740,650)
    root.maxsize(740,650)
    sc1value,sc2value = StringVar(),StringVar()
    sc1value.set('')
    sc2value.set('0')
    f1 = Frame(root,bg='grey')
    s1 = Entry(f1,textvar=sc1value,font='lucida 35 bold',width=3,justify=CENTER)
    s2 = Entry(f1,textvar=sc2value,font='lucida 23 bold',justify=RIGHT,width=16)
    s1.grid(row=0,column=0,ipady = 10,padx = 5,pady=10,ipadx=20)
    s2.grid(row=0,column=1,ipady = 20,padx = 5,pady=10,ipadx=160)
    f1.pack()
    i,j=0,0
    button = ['sin','cos','sqrt','AC','X','%','/','tan','rad','x!','7','8','9','*','log','ln','1/x','4','5','6','-','(',')','^','1','2','3','+','m','exp','pi','e','0','.','=']
    f2 = Frame(root)
    for b in button:
        if (i!=4 or j!=0) and (i!=1 or j!=1):
            b1=Button(f2,text=b,font='lucida 35',width=3)
            b1.bind('<Button-1>',click1)
            b1.grid(row=i,column=j,pady=6,padx=6)
        j+=1
        if j%7==0:
            i+=1
            j=0
    # if rad==False:
    #     text1 = 'rad';
    #     print('cmsc')
    # else:
    #     text1 = 'deg';    
    angle = Button(f2,text='deg',font='lucida 35',width=3)
    angle.bind('<Button-1>',click1)
    angle.grid(row=1,column=1,pady=6,padx=6)

    Button(f2,text='less',font='lucida 20',width=3,command=less).grid(row=4,column=0,pady=1,padx=1,ipadx=17,ipady=18)
    f2.pack(side=LEFT,padx=10)
    root.configure(background='black')

def less():
    
    widget_list = all_children(root)
    for item in widget_list:
        item.pack_forget()

    def click(event):
        global a
        text = event.widget.cget('text')
        if text in ['*','%','/','-','+']: 
            sc1value.set(text)
            s1.update()
            a +=text
            sc2value.set(a)
            s2.update()     
        elif text in ['1','2','3','4','5','6','7','8','9','0','.']:
            a +=text
            sc2value.set(a)
            s2.update()
        elif text=='=':
            try:
                sc1value.set('Ans.')
                sc2value.set(eval(a))
                s1.update()
                s2.update()
                a = ''
            except:
                sc1value.set('')
                sc2value.set('error')
                s1.update()
                s2.update()
                a= ''
        elif text=='X':
            a = a[:-1]
            sc2value.set(a)
            s2.update()            
        elif text=='AC':
            sc1value.set('')
            sc2value.set('0')
            s1.update()
            s2.update()
            a = ''   
                
    root.geometry('410x600')
    root.maxsize(410,600)
    root.minsize(410,600)
    i,j=0,0
    sc1value,sc2value = StringVar(),StringVar()
    sc1value.set('')
    sc2value.set('0')
    f = Frame(root,bg='grey')
    s1 = Entry(f,textvar=sc1value,font='lucida 35 bold',width=3,justify=CENTER)
    s2 = Entry(f,textvar=sc2value,font='lucida 23 bold',justify=RIGHT,width=16)
    s1.grid(row=0,column=0,ipady = 10,padx = 5,pady=10,ipadx=5)
    s2.grid(row=0,column=1,ipady = 20,padx = 5,pady=10,ipadx=10)
    f.pack()
    button = ['AC','X','%','/','7','8','9','*','4','5','6','-','1','2','3','+','m','0','.','=']
    f = Frame(root,bg='grey')
    for b in button:
        if i!=4 or j!=0:    
            b1=Button(f,text=b,font='lucida 35',width=3)
            b1.bind('<Button-1>',click)
            b1.grid(row=i,column=j,pady=1,padx=1)
        j+=1
        if j%4==0:
            i+=1
            j=0
    Button(f,text='more',font='lucida 20',width=3,command=more).grid(row=4,column=0,pady=1,padx=1,ipadx=17,ipady=18)        
    f.pack()
    root.configure(background='black')

less()
root.mainloop()