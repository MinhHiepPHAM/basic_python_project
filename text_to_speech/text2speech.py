from tkinter import *
from tkinter.ttk import *
from gtts import gTTS
from playsound import playsound

class Text2Speech(Tk):
    def __init__(self):
        super().__init__()
        self.title('Text to speech')
        self.geometry("300x150")

        self.user_choice_var = StringVar()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.text_var = StringVar()

        self.text_label = Label()
        self.warning_label = Label()

        self.create_widgets()

    def create_widgets(self):
        padding = {'padx':2, 'pady':2}

        self.warning_label.grid(column=0, row=0, columnspan=3, **padding)
        self.text_label.config(text='Text')
        self.text_label.grid(column=0, row=1, **padding)

        text = Entry(self, textvariable=self.text_var)
        text.grid(column=1, row=1, columnspan=2, **padding)

        Style().configure('TButton', foreground="red", background="white")
        Button(self, text='Play', command=self.play, style='TButton').grid(column=0, row=2, **padding)
        Button(self, text='Reset', command=self.reset, style='TButton').grid(column=1, row=2, **padding)
        Button(self, text='Close', command=self.close, style='TButton').grid(column=2, row=2, **padding)

    def play(self):
        input = self.text_var.get()
        if input == '':
            self.warning_label.config(text='Warning: the text is not given!!!')
            Style().configure('Error.TLabel', foreground='red')
            self.warning_label.config(style='Error.TLabel')
        else:
            # Language in which you want to convert
            language = 'vi'  # vietnamese

            # Passing the text and language to the engine,
            # here we have marked slow=False. Which tells
            # the module that the converted audio should
            # have a high speed
            myobj = gTTS(text=input, lang=language, slow=False)

            # Saving the converted audio in a mp3 file named
            myobj.save("output.mp3")

            # Playing the converted file
            playsound("output.mp3")

    def reset(self):
        self.text_var.config(text='')

    def close(self):
        self.destroy()

if __name__ == "__main__":
    app = Text2Speech()
    app.mainloop()
