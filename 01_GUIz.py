from tkinter import *
from random import shuffle


class Converter:
    def __init__(self):
        self.temp_frame = Frame(padx=15, pady=15, bg='forest green')
        self.temp_frame.grid()
        self.temp_heading = Label(self.temp_frame,
                                  text="Welcome To The Quiz",
                                  font=("Terminal", "20", "bold"),
                                  bg='forest green')
        self.temp_heading.grid(row=0)

        explanation = "This quiz will test your knowledge of pop culture"
        self.temp_explanation = Label(self.temp_frame, text=explanation, font='system',
                                      bg='forest green')
        self.temp_explanation.grid(row=1)

        explanation2 = "and your ability to make educated guesses."
        self.temp_explanation = Label(self.temp_frame, text=explanation2, font='system',
                                      bg='forest green')
        self.temp_explanation.grid(row=2)

        stakes = "You have 3 Lives. Make them count."
        self.temp_explanation = Label(self.temp_frame, text=stakes, font='system',
                                      bg='forest green', fg='red')
        self.temp_explanation.grid(row=3)

        self.button_frame = Frame(self.temp_frame, bg='forest green')
        self.button_frame.grid(row=4)

        self.begin = Button(self.button_frame,
                            text="Start", bg='deep pink', font=('system', 25))
        self.begin.grid(row=0, column=0, padx=15, pady=15)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz Game")
    Converter()
    root.mainloop()
