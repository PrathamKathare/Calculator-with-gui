import tkinter as calculator
calculation=" "

def operation(operand):
    global calculation
    calculation +=str(operand)
    text.delete(1.0,"end")
    text.insert(1.0,calculation)
    
def calculate():
    global calculation
    try:
        calculation=str(eval(calculation))
        text.delete(1.0,"end")
        text.insert(1.0,calculation)
    except:
        clear()
        text.insert(1.0,"error")
        
def clear():
    global calculation
    calculation=" "
    text.delete(1.0,"end")



root=calculator.Tk()
root.geometry("300x275")
text = calculator.Text(root, height=2,width=16,font=("Arial",24))
text.grid(columnspan=5)

#creating buttons
b1=calculator.Button(root,text="1",command=lambda:operation(1),width=5,font=("Arial",14))
b1.grid(row=2,column=1)

b2=calculator.Button(root,text="2",command=lambda:operation(2),width=5,font=("Arial",14))
b2.grid(row=2,column=2)

b3=calculator.Button(root,text="3",command=lambda:operation(3),width=5,font=("Arial",14))
b3.grid(row=2,column=3)

b4=calculator.Button(root,text="4",command=lambda:operation(4),width=5,font=("Arial",14))
b4.grid(row=3,column=1)

b5=calculator.Button(root,text="5",command=lambda:operation(5),width=5,font=("Arial",14))
b5.grid(row=3,column=2)

b6=calculator.Button(root,text="6",command=lambda:operation(6),width=5,font=("Arial",14))
b6.grid(row=3,column=3)

b7=calculator.Button(root,text="7",command=lambda:operation(7),width=5,font=("Arial",14))
b7.grid(row=4,column=1)

b8=calculator.Button(root,text="8",command=lambda:operation(8),width=5,font=("Arial",14))
b8.grid(row=4,column=2)

b9=calculator.Button(root,text="9",command=lambda:operation(9),width=5,font=("Arial",14))
b9.grid(row=4,column=3)

b0=calculator.Button(root,text="0",command=lambda:operation(0),width=5,font=("Arial",14))
b0.grid(row=5,column=2)

badd=calculator.Button(root,text="+",command=lambda:operation("+"),width=5,font=("Arial",14))
badd.grid(row=2,column=4)

bsub=calculator.Button(root,text="-",command=lambda:operation("-"),width=5,font=("Arial",14))
bsub.grid(row=3,column=4)

bmulti=calculator.Button(root,text="x",command=lambda:operation("*"),width=5,font=("Arial",14))
bmulti.grid(row=4,column=4)

bdivi=calculator.Button(root,text="/",command=lambda:operation("/"),width=5,font=("Arial",14))
bdivi.grid(row=5,column=4)

b_left=calculator.Button(root,text="(",command=lambda:operation("("),width=5,font=("Arial",14))
b_left.grid(row=5,column=1)

b_right=calculator.Button(root,text=")",command=lambda:operation(")"),width=5,font=("Arial",14))
b_right.grid(row=5,column=3)

bquals=calculator.Button(root,text="=",command=calculate,width=11,font=("Arial",14))
bquals.grid(row=6,column=3,columnspan=2)

bclear=calculator.Button(root,text="⌫",command=clear,width=11,font=("Arial",14))
bclear.grid(row=6,column=1,columnspan=2)

root.mainloop()