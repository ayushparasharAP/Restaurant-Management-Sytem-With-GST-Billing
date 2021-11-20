#    ---> Restaurant Management With GST Billing <---


from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1480x5000")
root.title("Restaurant Management With GST Billing")

text_Input = StringVar()


Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=300, height=700,bg="Grey", relief=SUNKEN)
f2.pack(side=RIGHT)




#         -->      TIME AND HEADING NAME   <--


localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('Courier New',50,'bold'),text="AM RESTAURANT ",fg="Navy",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('Bradley Hand ITC',20,'bold'),text="Best place for Food Lovers ",fg="Navy",bd=5,anchor='w')
lblInfo.grid(row=1,column=0)

lblInfo=Label(Tops,font=('arial',12,'bold'),text=localtime,fg="Black",bd=10,anchor='w')
lblInfo.grid(row=2,column=0)

#           -->      CALCULATOR    <--

def btnclick(numbers):
    global operator
    operator =operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator = ""

txtDisplay = Entry(f2,font=('arail', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="Grey", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="7", bg="Grey", command=lambda: btnclick(7))
btn7.grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="8", bg="Grey", command=lambda: btnclick(8))
btn8.grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="9", bg="Grey", command=lambda: btnclick(9))
btn9.grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="+", bg="Grey", command=lambda: btnclick("+"))
Addition.grid(row=2,column=3)

btn4=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="4", bg="Grey", command=lambda: btnclick(4))
btn4.grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="5", bg="Grey", command=lambda: btnclick(5))
btn5.grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="6", bg="Grey", command=lambda: btnclick(6))
btn6.grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="-", bg="Grey", command=lambda: btnclick("-"))
Subtraction.grid(row=3,column=3)

btn1=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="1", bg="Grey", command=lambda: btnclick(1))
btn1.grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="2", bg="Grey", command=lambda: btnclick(2))
btn2.grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="3", bg="Grey", command=lambda: btnclick(3))
btn3.grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="*", bg="Grey", command=lambda: btnclick("*"))
Multiply.grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="0", bg="Black", command=lambda: btnclick(0))
btn0.grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="C", bg="Black", command=btnClearDisplay)
btnClear.grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="=", bg="Black", command=btnEqualsInput)
btnEquals.grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="/", bg="Black", command=lambda: btnclick("/"))
Division.grid(row=5,column=3) 



#               -->     PROGRAM   <--


def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (PavBhaji.get()==""):
        CoPavBhaji=0
    else:
        CoPavBhaji=float(PavBhaji.get())

   
    if (CholeBathura.get()==""):
        CoCholeBathura=0
    else:
        CoCholeBathura=float(CholeBathura.get())


    if (IceCream.get()==""):
        CoIceCream=0
    else:
        CoIceCream=float(IceCream.get())


    if (Biryani.get()==""):
        CoBiryani=0
    else:
        CoBiryani=float(Biryani.get())

        
    if (Coffee.get()==""):
        CoCoffee=0
    else:
        CoCoffee=float(Coffee.get())

     
    if (Water.get()==""):
        CoWater=0
    else:
        CoWater=float(Water.get())

                   
    CostofPavBhaji = CoPavBhaji * 10
    CostofWater= CoWater * 5
    CostofCholeBathura = CoCholeBathura* 10
    CostofIceCream = CoIceCream * 5
    CostBiryani = CoBiryani* 15
    CostCoffee = CoCoffee * 5


    Central_GST= (((CostofPavBhaji+CostofWater+CostofCholeBathura+CostofIceCream+CostBiryani+CostCoffee)* 2.5)/100)

    State_GST =(((CostofPavBhaji+CostofWater+CostofCholeBathura+CostofIceCream+CostBiryani+CostCoffee)* 2.5)/100)

    Total_cost = (CostofPavBhaji+CostofWater+CostofCholeBathura+CostofIceCream+CostBiryani+CostCoffee)

    CostofMeal= "₹", str('%.2f' % (CostofPavBhaji+CostofWater+CostofCholeBathura+CostofIceCream+CostBiryani+CostCoffee))
    C_gst = "₹", str ('%.2f' % Central_GST)
    S_gst = "₹", str ('%.2f' % State_GST)
    OverAllCost ="₹", str ('%.2f' % (Total_cost+Central_GST+State_GST))


    Sgst.set(S_gst)
    Cost.set(CostofMeal)
    Cgst.set(C_gst)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    Coffee.set("")
    PavBhaji.set("")
    CholeBathura.set("")
    IceCream.set("")
    Biryani.set("")
    Water.set("")

    rand.set("")

    Total.set("")
    Sgst.set("")
    Cgst.set("")
    Cost.set("")
    

#            -->        RESTAURANT MENU    <--

Coffee=StringVar()
PavBhaji=StringVar()
CholeBathura=StringVar()
IceCream=StringVar()
Biryani=StringVar()
Water=StringVar()

rand = StringVar()

Cost=StringVar()
Sgst=StringVar()
Cgst=StringVar()
Total=StringVar()


lblCoffee= Label(f1, font=('Courier New', 16, 'bold'),text="Coffee",bd=10,anchor="w")
lblCoffee.grid(row=0, column=0)
txtCoffee=Entry(f1, font=('Courier New',16,'bold'),textvariable=Coffee,bd=10,insertwidth=4,bg="white",justify='right')
txtCoffee.grid(row=0,column=1)

lblWater= Label(f1, font=('Courier New', 16, 'bold'),text="Water",bd=10,anchor="w")
lblWater.grid(row=1, column=0)
txtWater=Entry(f1, font=('Courier New',16,'bold'),textvariable=Water,bd=10,insertwidth=4,bg="white",justify='right')
txtWater.grid(row=1,column=1)

lblIceCream= Label(f1, font=('Courier New', 16, 'bold'),text="Ice-Cream",bd=10,anchor="w")
lblIceCream.grid(row=2, column=0)
lblIceCream=Entry(f1, font=('Courier New',16,'bold'),textvariable=IceCream,bd=10,insertwidth=4,bg="white",justify='right')
lblIceCream.grid(row=2,column=1)

lblPavBhaji= Label(f1, font=('Courier New', 16, 'bold'),text="PavBhaji",bd=10,anchor="w")
lblPavBhaji.grid(row=3, column=0)
txtPavBhaji=Entry(f1, font=('Courier New',16,'bold'),textvariable=PavBhaji,bd=10,insertwidth=4,bg="white",justify='right')
txtPavBhaji.grid(row=3,column=1)

lblCholeBathura= Label(f1, font=('Courier New', 16, 'bold'),text="CholeBathura",bd=10,anchor="w")
lblCholeBathura.grid(row=4, column=0)
txtCholeBathura=Entry(f1, font=('Courier New',16,'bold'),textvariable=CholeBathura,bd=10,insertwidth=4,bg="white",justify='right')
txtCholeBathura.grid(row=4,column=1)

lblBiryani= Label(f1, font=('Courier New', 16, 'bold'),text="Biryani",bd=10,anchor="w")
lblBiryani.grid(row=5, column=0)
txtBiryani=Entry(f1, font=('Courier New',16,'bold'),textvariable=Biryani,bd=10,insertwidth=4,bg="white",justify='right')
txtBiryani.grid(row=5,column=1)


#         -->           RESTAURANT BILL INFO    <--


lblBillNo= Label(f1, font=('Courier New', 16, 'bold'),text="Bill No",bd=16,anchor="w")
lblBillNo.grid(row=0, column=2)
txtBillNo=Entry(f1, font=('Courier New',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="White",justify='right')
txtBillNo.grid(row=0,column=3)

lblCost= Label(f1, font=('Courier New', 16, 'bold'),text="Meal Cost",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('Courier New',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="White",justify='right')
txtCost.grid(row=1,column=3)


lblSgst= Label(f1, font=('Courier New', 16, 'bold'),text="SGST",bd=16,anchor="w")
lblSgst.grid(row=2, column=2)
txtSgst=Entry(f1, font=('Courier New',16,'bold'),textvariable=Sgst,bd=10,insertwidth=4,bg="White",justify='right')
txtSgst.grid(row=2,column=3)


lblCgst= Label(f1, font=('Courier New', 16, 'bold'),text="CGST",bd=16,anchor="w")
lblCgst.grid(row=3, column=2)
txtCgst=Entry(f1, font=('Courier New',16,'bold'),textvariable=Cgst,bd=10,insertwidth=4,bg="White",justify='right')
txtCgst.grid(row=3,column=3)

lblTotalCost= Label(f1, font=('Courier New', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=4, column=2)
txtTotalCost=Entry(f1, font=('Courier New',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="White",justify='right')
txtTotalCost.grid(row=4,column=3)


#         -->           BUTTONS   <--

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="Grey",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="Grey",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="Grey",command=qExit).grid(row=7,column=3)


root.mainloop()


