from tkinter import*
win=Tk()
win.title("Calculater")
win.geometry("425x280")
win.resizable(0,0)
win.configure(bg="black")

a=StringVar()

def show(x):
    a.set(a.get()+x)

def equ():
    ex=a.get()
    a.set(eval(ex))

def clr():
    a.set("")
    
E1=Entry(font=("",30),justify="right",textvariable=a)            
E1.place(x=0,y=0,width=430,height=50)

B=[Button()]*16
Data=["7","8","9","+","4","5","6","-","1","2","3","*","C","0","=","/"]
k=0
x=5
y=55

for i in range(4):
    for j in range(4):
        B[k]=Button(win,text=Data[k],font=("",25),bg="grey",fg="white",activebackground="yellow",activeforeground="red")
        B[k].place(x=x,y=y,width=100,height=50)
        k+=1
        x+=105
    x=5
    y+=55


B[0].configure(command=lambda:show(Data[0]))
B[1].configure(command=lambda:show(Data[1]))
B[2].configure(command=lambda:show(Data[2]))
B[3].configure(command=lambda:show(Data[3]))
B[4].configure(command=lambda:show(Data[4]))

B[5].configure(command=lambda:show(Data[5]))
B[6].configure(command=lambda:show(Data[6]))
B[7].configure(command=lambda:show(Data[7]))
B[8].configure(command=lambda:show(Data[8]))
B[9].configure(command=lambda:show(Data[9]))

B[10].configure(command=lambda:show(Data[10]))
B[11].configure(command=lambda:show(Data[11]))
B[12].configure(command=clr)
B[13].configure(command=lambda:show(Data[13]))
B[14].configure(command=equ)
B[15].configure(command=lambda:show(Data[15]))






win.mainloop()
