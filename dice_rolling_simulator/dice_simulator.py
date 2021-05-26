from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import scrolledtext as sr
import random

class Dice_Smulator(Tk):
    def __init__(self):
        super().__init__()
        self.title("Dice Rolling Simulator")
        self.geometry("300x300")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.log_history = Text()
        self.image_label = Label()

        self.dice_surfaces = ['figures/die1.png', 'figures/die2.png', 'figures/die3.png', 'figures/die4.png',
                              'figures/die5.png', 'figures/die6.png']
        self.output = ''
        self.counter = 0

        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}

        self.show_image(self.dice_surfaces[0])

        Style().configure("TButton", foreground="red", background="white")
        roll_button = Button(self, text='Roll', command=self.rolling, style="TButton")
        roll_button.grid(column=0, row=1, **padding)

        reset_button = Button(self, text='Reset', command=self.reset, style="TButton")
        reset_button.grid(column=1, row=1, **padding)

        self.log_history = sr.ScrolledText(self, wrap=WORD, width=15, height=10, font=("Times New Roman", 10))
        self.log_history.grid(column=1, row=0, padx=5, pady=5)

    def show_image(self, dice):
        padding = {'padx': 5, 'pady': 5}
        image = ImageTk.PhotoImage(Image.open(dice).resize((120, 120), Image.ANTIALIAS))
        self.image_label.config(image=image)
        self.image_label.grid(column=0, row=0, **padding)
        self.image_label.image = image

    def rolling(self):
        dice = random.choice(self.dice_surfaces)
        self.show_image(dice)
        self.counter += 1
        if dice == 'figures/die1.png':
            string = ': 1'
        elif dice == 'figures/die2.png':
            string = ': 2'
        elif dice == 'figures/die3.png':
            string = ': 3'
        elif dice == 'figures/die4.png':
            string = ': 4'
        elif dice == 'figures/die5.png':
            string = ': 5'
        else:
            string = ': 6'

        self.log_history.insert(INSERT, 'Rolling ' + str(self.counter) + string + '\n')

    def reset(self):
        self.log_history.delete('1.0', END)
        self.counter = 0

if __name__ == "__main__":
    app = Dice_Smulator()
    app.mainloop()