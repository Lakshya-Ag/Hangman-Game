from tkinter import *
from tkinter import messagebox
    
def startgame():
    global word
    word = a.get().lower()
    root = Tk()
    root.title("Hangman Game")
    root.minsize(580,580)
    root.geometry("500x500")
    
    canvas = Canvas(root, width = 260, height = 300)      
    canvas.pack()      
    game = PhotoImage(file="gallows.gif")
    canvas.create_image(20,20, anchor=NW, image=game)
    root.mainloop()
    
def playnow():
    top = Tk()
    top.title("Enter a word")
    top.minsize(200,100)
    top.geometry("300x80")
    global a
    a = StringVar()
    
    L1 = Label(top)
    L1.pack()

    E1 = Entry(top, width=30, textvariable=a)
    E1.insert(0, "Enter a word to be guessed.")
    E1.pack()

    benter = Button(top, text="Submit", width=7, command = startgame)
    benter.pack()
    top.mainloop()
    
def quitnow():
    msg = messagebox.showinfo('Thank You','Thanks for Playing. See you soon!')
    exit()

top = Tk()
top.title("Hangman in python.")
top.minsize(380,380)
top.geometry("300x100")

canvas = Canvas(top, width = 260, height = 300)      
canvas.pack()      
img = PhotoImage(file="title.gif")      
canvas.create_image(20,20, anchor=NW, image=img)

bplay = Button(top, text="Play", width=10, command = playnow)
bplay.pack()
bquit = Button(top, text="Quit", width=10, command = quitnow)
bquit.pack()
top.mainloop()
