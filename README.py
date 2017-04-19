# Rock-Paper-Scissors-Game
# A Simple Rock Paper scissors with GUI
#A SIMPLE ROCK PAPER SCISSORS GAME WITH PYTHON BUILT WITH PYTHON 3.4

from tkinter import *
import random
#import simple_Game_ext.py

Simple_Game= Tk()
Simple_Game.geometry("500x500")
Simple_Game.title("Rock Paper Scissors")

You =StringVar()
Opponent=StringVar()
result_1=StringVar()
choice_1=StringVar()
Balance= StringVar()
balance_1 =0
#balance_2=0


#COMMAND BUTTONS FOR THE BUTTONS 
def Buttons_Rock():
    result= random.randint(0,99)
    global balance_1
    if result<=33:
        You.set("TIED,PLAY AGAIN")
        Opponent.set("Rock")
        #Balance.set( "KSH 0.00")
        balance_1+=0
        #print (balance_1)
        Balance.set( str(balance_1))
    elif result <=66:
        You.set("LOST!!!")
        Opponent.set ("Paper")
        Balance.set("KSH - 10.00")
        balance_1-=10
        #print (balance_1)
        Balance.set( str(balance_1))
    elif result <=99:
        You.set("WON!!")
        Opponent.set("Scissors")
        Balance.set("KSH 10.00")
        balance_1+=10
        #print (balance_1)
        Balance.set( str(balance_1))
    return #balance_1      
def Buttons_Paper():
    result= random.randint(0,99)
    global balance_1
    if result<=33:
        You.set("WON!!")
        Opponent.set("Rock")
        Balance.set("KSH 10.00")
        balance_1+=10
        #print (balance_1)
        Balance.set( str(balance_1))
    elif result <=66:
        You.set("TIED,PLAY AGAIN")
        Opponent.set ("Paper")
        Balance.set( "KSH 0.00")
        balance_1+=0
        #print (balance_1)
        Balance.set( str(balance_1))
    elif result <=99:
        You.set("LOST!!")
        Opponent.set("Scissors")
        Balance.set("KSH - 10.00")
        balance_1-=10
        #print (balance_1)
        Balance.set( str(balance_1))
    return #balance_1     
def Buttons_Scissors():
    result= random.randint(0,99)
    global balance_1
    if result<=33:
        You.set("LOST!!")
        Opponent.set("Rock")
        Balance.set("KSH - 10.00")
        balance_1-=10
        #print (balance_1)
        Balance.set( str(balance_1))
    elif result <=66:
        You.set("WON!!")
        Opponent.set ("Paper")
        Balance.set("KSH 10.00")
        balance_1+=10
        #print (balance_1)
        Balance.set( str(balance_1))
    elif result <=99:
        You.set("TIED,PLAY AGAIN")
        Opponent.set("Scissors")
        Balance.set( "KSH 0.00")
        balance_1+=0
        #print (balance_1)
        Balance.set( str(balance_1))
#balance_2+=#balance_1
#print (#balance_2)

def Play():
    global balance_1
    ##balance_1=10
    #if You=="WON!!":
        ##balance_1+= 10
        ##balance.set (#balance)
        ##print (#balance_1)
        #You.set("")
        #Opponent.set("")
    #elif You== "LOST!!":
        ##balance_1-= 10
        ##balance.set (#balance)
        ##print (#balance_1)
        #You.set("")
        #Opponent.set("")
    #elif You=="TIED,PLAY AGAIN":
        ##balance_1=0
        ##balance.set(#balance)
        ##print (#balance_1)
        #You.set("")
        #Opponent.set("")
    You.set("")
    Opponent.set("")
    balance_1=0
    Balance.set( str(balance_1))
    
# Below are the codes for the Graphical User Interface Using Tkinter
    #Main Frames :top.left and right
TF=Frame(Simple_Game,width=500 ,height=90, bd=8 ,relief='raise',bg='red' )
TF.pack(side=TOP)
LF=Frame(Simple_Game,width=250 ,height=400, bd=16 ,relief='raise',bg='blue' )
LF.pack(side=LEFT)
RF=Frame(Simple_Game,width=250 ,height=400 ,bd=16 ,relief='raise',bg='black')
RF.pack(side=RIGHT)

#XXXXXXXXXXX INSIDE TOP FRAMEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

lblInfo= Label(TF ,font=('arial',20,'bold'),text="Rock Paper Scissors" ,fg='Red',bd=1)
lblInfo.grid(row=0,column=0)
button= Button (TF  ,padx=8 ,bd=8 ,fg="black",font=('arial',12,'bold') ,width=14, text= "Withdraw",bg= 'sky blue').place(x=10,y=200)

lblbalance= Label(TF,font=('arial',12,'bold'),text="Acc balance" ,fg='Steel Blue',bd=10, anchor='w')
lblbalance.grid(row=1,column=0)
txtbalance= Entry(TF,font=('arial',12,'bold'),bd=10, width=18,bg='Powder Blue',justify='right' ,textvariable=Balance)
txtbalance.grid(row=2,column=0)

#XXXXXXXXXXX INSIDE RIGHT & LEFT FRAMES XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

LeftInsideLF=Frame(LF ,width=200 ,height=50, bd=8 ,relief='raise',bg='blue')
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF ,width=250 ,height=300, bd=8 ,relief='raise' ,bg='red')
LeftInsideLFLF.pack(side=LEFT)

RightInsideRF=Frame(RF ,width=200 ,height=50, bd=8 ,relief='raise',bg='blue')
RightInsideRF.pack(side=TOP)
RightInsideRFRF=Frame(RF ,width=250 ,height=300, bd=8 ,relief='raise' ,bg='red')
RightInsideRFRF.pack(side=LEFT)
#XXXXXXXXXXXX BUTTONS INSIDE THE LEFT FRAME XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
lblButton= Label(LeftInsideLF ,font=('arial',12,'bold'),text="Click Button" ,fg='Steel Blue',bd=10, anchor='w')
lblButton.grid(row=0,column=0)

Rock= Button (LeftInsideLFLF ,padx=8 ,bd=8 ,fg="black",font=('arial',12,'bold') ,width=14, text= "Rock",bg= 'sky blue',command= Buttons_Rock).grid (row=0,column=0)

Paper= Button (LeftInsideLFLF ,padx=8 ,bd=8 ,fg="black",font=('arial',12,'bold') ,width=14, text= "Paper",bg= 'sky blue',command=Buttons_Paper).grid (row=1,column=0)

Scissors= Button (LeftInsideLFLF ,padx=8 ,bd=8 ,fg="black",font=('arial',12,'bold') ,width=14, text= "Scissors",bg= 'sky blue',command=Buttons_Scissors).grid (row=2,column=0)


#XXXXXXX iNSIDE THE RIGHT FRAME #################
lblResults= Label(RightInsideRF ,font=('arial',12,'bold'),text="Results" ,fg='Steel Blue',bd=10, anchor='w')
lblResults.grid(row=0,column=0)

lblYou= Label(RightInsideRFRF,font=('arial',12,'bold'),text="YOU" ,fg='Steel Blue',bd=10, anchor='w')
lblYou.grid(row=1,column=0)
txtYou= Entry(RightInsideRFRF,font=('arial',12,'bold'),bd=10, width=18,bg='light green',justify='left' ,textvariable=You)
txtYou.grid(row=2,column=0)

lblOpponent= Label(RightInsideRFRF,font=('arial',12,'bold'),text="Computer Chose" ,fg='Steel Blue',bd=10, anchor='w')
lblOpponent.grid(row=3,column=0)
txtOpponent= Entry(RightInsideRFRF,font=('arial',12,'bold'),bd=10, width=18,bg='light green',justify='left' ,textvariable=Opponent)
txtOpponent.grid(row=4,column=0)

Play= Button (RightInsideRFRF,padx=8 ,bd=8 ,fg="black",font=('arial',12,'bold') ,width=14, text= "Play",bg= 'sky blue',command=Play).grid (row=0,column=0)




Simple_Game.mainloop()
