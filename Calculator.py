from tkinter import *
window=Tk()
window.geometry("700x500+150+50")
window.title("Calculator ")
expn=StringVar()
def change(num):
    cur = expn.get()
    expn.set( str(cur)+str(num))
def evalexpn():
    
    expn.set(eval(expn.get()))

Entry(window,textvariable=expn,bg="#000000",
           fg="#FFFFFF",font=("Arial",18,"bold"),
           width=20).grid(row=0, column=1, columnspan=4 )
button_1 = Button(window, text="1", padx=40, pady=20, command=lambda:change(1)).grid(row=1, column=1 )
button_2 =  Button(window, text="2", padx=40, pady=20, command=lambda: change(2)).grid(row=1, column=2 )
button_3 =  Button(window, text="3", padx=40, pady=20, command=lambda: change(3)).grid(row=1, column=3 )
button_4 =  Button(window, text="4", padx=40, pady=20, command=lambda: change(4)).grid(row=2, column=1 )
button_5 =  Button(window, text="5", padx=40, pady=20, command=lambda: change(5)).grid(row=2, column=2)
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: change(6)).grid(row=2, column=3)
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: change(7)).grid(row=3, column=1)
button_8 =  Button(window, text="8", padx=40, pady=20, command=lambda: change(8)).grid(row=3, column=2)
button_9 =  Button(window, text="9", padx=40, pady=20, command=lambda: change(9)).grid(row=3, column=3 )
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: change(0)).grid(row=4, column=1)
button= Button(window, text=".", padx=40, pady=20, command=lambda: change(".")).grid(row=4, column=2)

button_add =  Button(window, text="+", padx=40, pady=20, command=lambda: change("+")).grid(row=1, column=4)
button_subtract =  Button(window, text="-", padx=40, pady=20, command=lambda:  change("-")).grid(row=2, column=4)
button_multiply = Button(window, text="*", padx=40, pady=20, command=lambda: change("*")).grid(row=3, column=4)
button_divide = Button(window, text="/", padx=40, pady=20, command=lambda: change("/")).grid(row=4, column=3)

button_equals = Button(window, text="=", padx=40, pady=20, command=evalexpn ).grid(row=4, column=4)


window.mainloop()
