from tkinter import *
import pyttsx3 



window = Tk()

window.geometry("600x500")
window.configure(bg="white")
window.title("Jarvis")
window.resizable(0,0)




def com():
    g = str(type.get("1.0", END))
    type.delete("1.0", END)
    from main import jarvis
    jarvis("no", g[:-1])

def com2():
    label5 = Label(window, text="Listening...", font=("Arial Bold", 15), bg="white")
    label5.grid(row=6, column=2, pady=5, padx=5)
    import main
    main.jarvis("yes","")
    label6.config(text=main.command)
    

label6 = Label(window, text="", font=("Arial Bold", 15), bg="white")
label6.grid(row=7, column=2, pady=5, padx=5)

# Image

bg = PhotoImage(file = "ironman3.png")
bg = bg.subsample(3,3)

photo = PhotoImage(file = "keyboard.png")
photo = photo.subsample(10,10)

photo2 = PhotoImage(file = "speaks.png")
photo2 = photo2.subsample(10,10)

label1 = Label(window, image = bg, bg="white")
label1.grid(row=1, column=2)


# Title

label4 = Label(window, text="Jarvis", font=("Arial Bold", 20), bg="white", fg="red")
label4.grid(row=2, column=2, pady=5, padx=5)



# Type or Speak Button

button = Button(window, width=15, text="Type", bg="lightgreen", height=1, command=com, bd=4, 
activebackground="grey", fg="red", font="Helvetica", highlightcolor="blue")

button.grid(row=4, column=1, pady=5, padx=15)


button = Button(window, width=15, text="Speak", bg="cyan", height=1, command=com2, bd=4, 
activebackground="grey", fg="red", font="Helvetica", highlightcolor="blue")

button.grid(row=4, column=3, pady=5, padx=5)



# Icons

label2 = Label(window, image = photo, bg="white")
label2.grid(row=3, column=1, pady=5, padx=5)


label3 = Label(window, image = photo2, bg="white")
label3.grid(row=3, column=3, pady=5, padx=5)



# Text Input

type = Text(window,height = 3,width = 20, bd=4)
type.grid(row=8, column=2, pady=5, padx=5)


# Greet

eng = pyttsx3.init()
eng.say("Hello sir")  
eng.runAndWait()  


window.mainloop()

