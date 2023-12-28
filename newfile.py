from tkinter import *
from tkinter import messagebox
import os


    


questions={
"bonjour":"bonjour,\ncomment puis-je vous aider",
"qui es tu":"je suis chatbot"
}


def reponse():
    message=str(entry.get())
    global texte
    if message in questions:
        msg['text']=questions[message]
        print(f"{msg}")
    else:
        messagebox.showinfo("reponse","desolee")
        
fen=Tk()


fen.title("chatbot")

tete=Label(fen,text="bienvenue a mon systeme").pack()

lab=Label(fen,text="entrer la question",)
lab.pack()

entry=Entry(fen)
entry.pack()

msg=Label(fen,text="votre reponse",font=("",11))
msg.pack()

boutton=Button(fen,text="click",command=reponse)

boutton.pack()

fen.mainloop()

print("fin du programme")