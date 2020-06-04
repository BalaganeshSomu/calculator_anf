#ANF CALCULATOR
#BALAGANESH .S 

from tkinter import *
from tkinter import messagebox
screen=Tk()
x=''
screen.geometry('500x500')
screen.title('ANF CALCULATOR')
N=IntVar()


backgroundimage=PhotoImage(file='C:/Users/Balaganesh/Downloads/—Pngtree—abstract blue digital technology background_3527869.png')
backgroundlabel=Label(screen,image=backgroundimage)
backgroundlabel.place(relheight=1,relwidth=1)


mb=  Menubutton ( screen, text="MENU", bg='grey',bd=4,relief='ridge' )
mb.place(relheight=0.1,relwidth=0.1)
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

def CREDITS():
    messagebox.showinfo('CREATED BY:','DONE BY: BALAGANESH.S & MOHAMMED AYYUB.M')

def HELP():
    messagebox.showinfo('INSTRUCTIONS','1.Enter your boolean expression \n 2.Enter the number of varialbes (1-5) \n 3.Press CALCULATE ')
    
    
mb.menu.add_checkbutton ( label="Help",command=HELP )
mb.menu.add_checkbutton ( label="Credits",command=CREDITS )



def A():
    global x
    x=x+"a "
    label=Label(lowerframe,text=x,bg='white').place(relheight=0.1,relwidth=1)

def B():
    global x
    x=x+"b "
    label=Label(lowerframe,text=x,bg='white').place(relheight=0.1,relwidth=1)

def C():
    global x
    x=x+"c "
    label=Label(lowerframe,text=x,bg='white').place(relheight=0.1,relwidth=1)

def D():
    global x
    x=x+"d "
    label=Label(lowerframe,text=x,bg='white').place(relheight=0.1,relwidth=1)

def E():
    global x
    x=x+"e "
    label=Label(lowerframe,text=x,bg='white').place(relheight=0.1,relwidth=1)

def AND():
    global x
    x=x+"and "
    label=Label(lowerframe,text=x,bg='white').place(relheight=0.1,relwidth=1)
def OR():
    global x
    x=x+"or "
    label=Label(lowerframe,text=x,bg='white').place(relheight=0.1,relwidth=1)
    
def space():
    global x
    x=x+" "
    label=Label(lowerframe,text=x,bg='white').place(relheight=0.1,relwidth=1)
    
def brl():
    global x
    x=x+"("
    label=Label(lowerframe,text=x,bg='white').place(relheight=0.1,relwidth=1)

def brr():
    global x
    x=x+")"
    label=Label(lowerframe,text=x,bg='white').place(relheight=0.1,relwidth=1)

def AC():
    global x
    x=''
    label=Label(lowerframe,text='',bg='white').place(relheight=0.1,relwidth=1)


def calc():
    global x 
    res=[]
    xx=[]
    xx1=[]
    xx2=[]
    global N
    n=N.get()
    if n>=6:
        messagebox.showwarning("WARNING!!!!", "N should be less than 6")        
    

    for i in range (0,2**n ):
        xx.append(bin(i))

    for i in xx:
        xx1.append(i.replace('0b',''))

    for i in xx1:
            if len(i)!=n:
                    xx2.append(i.zfill(n))
            else :
                    xx2.append(i)
    for i in xx2:
            if n==1:
                    a=int(i[0])

            elif n==2:
                    a=int(i[0])
                    b=int(i[1])

            elif n==3:
                    a=int(i[0])
                    b=int(i[1])
                    c=int(i[2])

            elif n==4:
                    a=int(i[0])
                    b=int(i[1])
                    c=int(i[2])
                    d=int(i[3])

            elif n==5:
                    a=int(i[0])
                    b=int(i[1])
                    c=int(i[2])
                    d=int(i[3])
                    e=int(i[4])
            res.append(eval(x))
            l=[]
    l=res
    for i in range(2**(n-1)):
        l.append(0)
    def twovar(tt):
        a0=0 if [tt[0]].count(1)%2==0 else 1
        a1=0 if [tt[0],tt[1]].count(1)%2==0 else 1
        a2=0 if [tt[0],tt[2]].count(1)%2==0 else 1
        a3=0 if [tt[0],tt[1],tt[2],tt[3]].count(1)%2==0 else 1
        l=[a0,a1,a2,a3]
        return l
    def threevar(t):
        l1=twovar(t[0:4])
        l2=twovar(t[4:8])
        for i in range(4):
            l1.append(0 if [l1[i],l2[i]].count(1)%2==0 else 1)
        return l1
    def fourvar(t):
        l1=threevar(t[0:8])
        l2=threevar(t[8:16])
        for i in range(8):
            l1.append(0 if [l1[i],l2[i]].count(1)%2==0 else 1)
        return l1
    def fivevar(t):
        l1=fourvar(t[0:16])
        l2=fourvar(t[16:32])
        for i in range(16):
            l1.append(0 if [l1[i],l2[i]].count(1)%2==0 else 1)
        return l1
    if n==2:
        l1=twovar(l)
    elif n==3:
        l1=threevar(l)
    elif n==4:
        l1=fourvar(l)
    elif n==5:
        l1=fivevar(l)    
    l=['1','a','b','ab','c','ac','bc','abc','d','ad','bd','abd','cd','acd','bcd','abcd','e','ae','be','abe','ce','ace','bce','abce','de','ade','bde','abde','cde','acde','bcde','abcde']
    l9=[]
    for i in range(2**n):
        if l1[i]==1:
            l9.append(l[i])
    result=[]
    if len(l9)!=1:
        for i in range(len(l9)-1):
            result.append(l9[i])
            result.append('xor')
        result.append(l9[i+1])
    else:
        result.append(l9[0])

            
    
    label=Label(lowerframe,text=result,bg='white').place(rely=0.90,relheight=0.1,relwidth=1)

heading=Label(screen,text='ALGEBRAIC NORMAL FORM ',font='80',bg='#0DA7CE')
heading.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=1,anchor='n')


upperframe=Frame(screen,bg='#0DA7CE',bd=5)
upperframe.place(relx=0.5,rely=0.25,relheight=0.075,relwidth=0.8,anchor='n')
entry=Entry(upperframe,textvariable=N).place(relheight=1,relwidth=0.55)
calculate_button=Button(upperframe,text='CALCULATE',command=calc,height=2,width=10,bg='grey',bd=4,relief='ridge').place(relx=0.6,relwidth=0.35,relheight=1)


lowerframe=Frame(screen,bg='#226697',bd=5)
lowerframe.place(relx=0.5,rely=0.35,relheight=0.6,relwidth=0.8,anchor='n')
           

b1=Button(lowerframe,text="  A  " ,command=A,bg='#D4EAFA',bd=4,relief='ridge').place(relx=0.15,rely=0.15,relheight=0.15,relwidth=0.15,anchor='n')
b2=Button(lowerframe,text="  B  " ,command=B,bg='#D4EAFA',bd=4,relief='ridge').place(relx=0.35,rely=0.15,relheight=0.15,relwidth=0.15,anchor='n')
b3=Button(lowerframe,text="  C  " ,command=C,bg='#D4EAFA',bd=4,relief='ridge').place(relx=0.15,rely=0.40,relheight=0.15,relwidth=0.15,anchor='n')
b4=Button(lowerframe,text="  D  " ,command=D,bg='#D4EAFA',bd=4,relief='ridge').place(relx=0.35,rely=0.40,relheight=0.15,relwidth=0.15,anchor='n')
b5=Button(lowerframe,text="  E  " ,command=E,bg='#D4EAFA',bd=4,relief='ridge').place(relx=0.25,rely=0.65,relheight=0.15,relwidth=0.15,anchor='n')

b6=Button(lowerframe,text="  AND  " ,command=AND,bg='#D4EAFA',bd=4,relief='ridge').place(relx=0.70,rely=0.15,relheight=0.15,relwidth=0.15,anchor='n')
b7=Button(lowerframe,text="  OR  " ,command=OR,bg='#D4EAFA',bd=4,relief='ridge').place(relx=0.90,rely=0.15,relheight=0.15,relwidth=0.15,anchor='n')
b8=Button(lowerframe,text="  (  " ,command=brl,bg='#D4EAFA',bd=4,relief='ridge').place(relx=0.70,rely=0.40,relheight=0.15,relwidth=0.15,anchor='n')
b9=Button(lowerframe,text="  )  " ,command=brr,bg='#D4EAFA',bd=4,relief='ridge').place(relx=0.90,rely=0.40,relheight=0.15,relwidth=0.15,anchor='n')
b10=Button(lowerframe,text=" SPACE " ,command=space,bg='#D4EAFA',bd=4,relief='ridge').place(relx=0.70,rely=0.65,relheight=0.15,relwidth=0.15,anchor='n')
b11=Button(lowerframe,text="  AC " ,command=AC,bg='#D4EAFA',bd=4,relief='ridge').place(relx=0.90,rely=0.65,relheight=0.15,relwidth=0.15,anchor='n')

screen.mainloop()

