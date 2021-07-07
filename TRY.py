from tkinter import *
THEME_COLOR = "#375362"
window = Tk()
window.title("Quizzler")
window.config(padx=20,pady=20,bg=THEME_COLOR)
score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
score_label.grid(row=0,column=1)
canvas = Canvas(width=300,height=250,bg="white")
que_text = canvas.create_text(150,125, text="",fill =THEME_COLOR, font=("Arial",20,"italic"),width = 280)
canvas.grid(row=1,column=0,columnspan=2,pady=50)
correct = PhotoImage(file="./images/true.png")
wrong = PhotoImage(file="./images/false.png")
correct_button = Button(image=correct,highlightthickness=0)
correct_button.grid(column=0,row=2)
wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.grid(column=1,row=2)


window.mainloop()