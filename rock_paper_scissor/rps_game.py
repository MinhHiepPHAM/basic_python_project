from tkinter import *
from tkinter.ttk import *
import random


class RPS_Application(Tk):
    ERROR = 'Error.TLabel' # Need to use the format xxx.TLabel
    USER_WIN = 'User.TLabel'
    COMP_WIN = 'Computer.TLabel'
    TIE = 'Tie.TLabel'

    def __init__(self):
        super().__init__()
        self.title('Rock Paper Scissor Game')
        self.geometry("450x200")

        self.user_choice_var = StringVar()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.result = Label(self)

        # Set color for the result messages
        self.style = Style(self)
        self.style.configure('Error.TLabel', foreground='red')
        self.style.configure('User.TLabel', foreground='green')
        self.style.configure('Computer.TLabel', foreground='orange')
        self.style.configure('Tie.TLabel', foreground='blue')

        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}

        Label(self, text='User choice:').grid(column=0, row=0, **padding)

        option_list = ["Paper", "Scissors", "Rock"]

        OptionMenu(self, self.user_choice_var, option_list[1], *option_list).grid(column=1, row=0, **padding)
        self.user_choice_var.set("Select an Option")  # This line needs to be after OptionMenu definition
        play_button = Button(self, text='Play', command=self.play_game)
        play_button.grid(column=2, row=0, **padding)

        reset_button = Button(self, text='Reset', command=self.reset_game)
        reset_button.grid(column=2, row=1, **padding)

        close_button = Button(self, text='Close', command=self.close_game)
        close_button.grid(column=1, row=3, **padding)

        self.result.grid(column=0, row=1, columnspan=2, **padding)

    def play_game(self):
        use_choice = self.user_choice_var.get()
        seq = ["Paper", "Scissors", "Rock"]
        comp_choice = random.choice(seq)
        if use_choice == comp_choice:
            str_result = 'tie,you both select same'
            style = self.TIE
        elif use_choice == 'Rock' and comp_choice == 'Paper':
            str_result = 'you loose,computer select paper'
            style = self.COMP_WIN
        elif use_choice == 'Rock' and comp_choice == 'Scissors':
            str_result = 'you win,computer select scissors'
            style = self.USER_WIN
        elif use_choice == 'Paper' and comp_choice == 'Scissors':
            str_result = 'you loose,computer select scissors'
            style = self.COMP_WIN
        elif use_choice == 'Paper' and comp_choice == 'Rock':
            str_result = 'you win,computer select rock'
            style = self.USER_WIN
        elif use_choice == 'Scissors' and comp_choice == 'Rock':
            str_result = 'you loose,computer select rock'
            style = self.COMP_WIN
        elif use_choice == 'Scissors' and comp_choice == 'Paper':
            str_result = 'you win ,computer select paper'
            style = self.USER_WIN
        else:
            str_result = 'invalid: choose any one -- rock, paper, scissors'
            style = self.ERROR

        self.set_result_color(str_result, style)

    def set_result_color(self, message='', tp=None):
        self.result.config(text=message)
        if tp:
            self.result.config(style=tp)

    def reset_game(self):
        self.user_choice_var.set("Select an Option")
        self.set_result_color()

    def close_game(self):
        self.destroy()


if __name__ == "__main__":
    app = RPS_Application()
    app.mainloop()
