from tkinter import *
import tkinter.messagebox # for python 3

tk = Tk() # python 3
tk.title('TIC TAC TOE')

click = True

def checker (buttons) :
    global click
    
    # check first if a player has won
    if (button1['text'] =='X' and button2['text'] =='X' and button3['text'] =='X' or
          button1['text'] =='X' and button5['text'] =='X' and button9['text'] =='X' or
          button1['text'] =='X' and button4['text'] =='X' and button7['text'] =='X' or
          button4['text'] =='X' and button5['text'] =='X' and button6['text'] =='X' or
          button7['text'] =='X' and button8['text'] =='X' and button9['text'] =='X' or
          button3['text'] =='X' and button5['text'] =='X' and button7['text'] =='X' or
          button2['text'] =='X' and button5['text'] =='X' and button8['text'] =='X' or
          button3['text'] =='X' and button6['text'] =='X' and button9['text'] =='X' ) :
        tkinter.messagebox.showinfo ('WINNER X', 'PLAYER X WON THE GAME')
         
    elif (button1['text'] =='O' and button2['text'] =='O' and button3['text'] =='O' or
          button1['text'] =='O' and button5['text'] =='O' and button9['text'] =='O' or
          button1['text'] =='O' and button4['text'] =='O' and button7['text'] =='O' or
          button4['text'] =='O' and button5['text'] =='O' and button6['text'] =='O' or
          button7['text'] =='O' and button8['text'] =='O' and button9['text'] =='O' or
          button3['text'] =='O' and button5['text'] =='O' and button7['text'] =='O' or
          button2['text'] =='O' and button5['text'] =='O' and button8['text'] =='O' or
          button3['text'] =='O' and button6['text'] =='O' and button9['text'] =='O' ) :
        tkinter.messagebox.showinfo ('WINNER O', 'PLAYER O WON THE GAME')
        
    #  when there is no winner or wrong move
    elif buttons['text'] != " " :
        if (button1['text'] !=" " and button2['text'] !=" " and button3['text'] !=" " and
          button1['text'] !=" " and button5['text'] !=" " and button9['text'] !=" " and
          button1['text'] !=" " and button4['text'] !=" " and button7['text'] !=" " and
          button4['text'] !=" " and button5['text'] !=" " and button6['text'] !=" " and
          button7['text'] !=" " and button8['text'] !=" " and button9['text'] !=" " and
          button3['text'] !=" " and button5['text'] !=" " and button7['text'] !=" " and
          button2['text'] !=" " and button5['text'] !=" " and button8['text'] !=" " and
          button3['text'] !=" " and button6['text'] !=" " and button9['text'] !=" ") :
            tkinter.messagebox.showinfo ('DRAW', 'NO WINNER')
        else :
            tkinter.messagebox.showinfo ('WRONG MOVE', 'PLEASE SELECT ANOTHER BOX')

    elif buttons['text'] == " " and click == True :
        buttons['text'] = "X"
        buttons['fg'] = 'green'
        click = False
    elif buttons['text'] == " " and click == False :
        buttons['text'] = "O"
        buttons['fg'] = 'red'
        click = True

buttons=StringVar()

button1 = Button(tk, text=" ", font=('Arial 30 bold'), height=4 , width=8 , command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(tk, text=" ", font=('Arial 30 bold'), height=4 , width=8 , command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3 = Button(tk, text=" ", font=('Arial 30 bold'), height=4 , width=8 , command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(tk, text=" ", font=('Arial 30 bold'), height=4 , width=8 , command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5 = Button(tk, text=" ", font=('Arial 30 bold'), height=4 , width=8 , command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6 = Button(tk, text=" ", font=('Arial 30 bold'), height=4 , width=8 , command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7 = Button(tk, text=" ", font=('Arial 30 bold'), height=4 , width=8 , command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8 = Button(tk, text=" ", font=('Arial 30 bold'), height=4 , width=8 , command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9 = Button(tk, text=" ", font=('Arial 30 bold'), height=4 , width=8 , command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)

def SetToBlank():
    button1['text'] = " "
    button2['text'] = " "
    button3['text'] = " "
    button4['text'] = " "
    button5['text'] = " "
    button6['text'] = " "
    button7['text'] = " "
    button8['text'] = " "
    button9['text'] = " "
    
reset = Button(tk, text=' Play Again ', font=('Arial 20 '), fg='grey', command=SetToBlank)
reset.grid(row=4,column=1)

tk.mainloop()