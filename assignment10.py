from tkinter import *
import webbrowser as wb
obj=Tk(className="window")



e=Entry(obj,font=("Times New Roman",25))
e.grid()


def nav():
    search=e.get()
    wb.open("https://www.instagram.com/"+search+"/")


b=Button(obj,text="click",font=("Times New Roman",25),
         command=nav
         )


b.grid()
obj.mainloop()