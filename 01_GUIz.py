from tkinter import *
from random import shuffle


class Converter:
    def __init__(self):
        self.temp_frame = Frame(padx=15, pady=15, bg='dodger blue')
        self.temp_frame.grid()
        self.temp_heading = Label(self.temp_frame,
                                  text="Welcome To The Quiz",
                                  font=("Times", "20", "bold"),
                                  bg='dodger blue')
        self.temp_heading.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz Game Video Game For Quiz")
    Converter()
    root.mainloop()
