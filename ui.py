import tkinter.messagebox
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.que_text = self.canvas.create_text(150,125, text="t",fill =THEME_COLOR, font=("Arial",20,"italic"),width = 280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        correct = PhotoImage(file="./images/true.png")
        wrong = PhotoImage(file="./images/false.png")
        self.correct_button = Button(image=correct,highlightthickness=0,command=self.true_pressed)
        self.correct_button.grid(column=0,row=2)
        self.wrong_button = Button(image=wrong, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1,row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score :{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.que_text, text=q_text)
        else:
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.canvas.itemconfig(self.que_text,text="you have reached the end of te game")
            var = tkinter.messagebox.showinfo(title="game ended", message=f"Your score is {self.quiz.score}")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)