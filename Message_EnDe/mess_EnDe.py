from tkinter import *
from tkinter.ttk import *
import base64

class Message_EnDe(Tk):
    def __init__(self):
        super().__init__()
        self.title("Message Encode and Decode")
        self.geometry("400x220")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.input_label = Label()
        self.output_label = Label()
        self.option_label = Label()
        self.key_label = Label()
        self.warning_label = Label()

        self.option_ED = StringVar()
        self.input_var = StringVar()
        self.option_var = StringVar()
        self.output_var = StringVar()
        self.key_var = StringVar()

        self.style = Style()
        self.style.configure('Error.TLabel', foreground='red')

        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 1, 'pady': 1}
        self.input_label.grid(column=0, row=0, **padding)
        self.input_label.config(text='Input:')

        self.key_label.grid(column=0, row=1, **padding)
        self.key_label.config(text='Key:')

        self.output_label.grid(column=0, row=2, **padding)
        self.output_label.config(text='Output')

        self.option_label.grid(column=0, row=3, **padding)
        self.option_label.config(text='Option:')

        self.warning_label.grid(column=0, row=5, columnspan=2, **padding)

        Style().configure("TButton", foreground="red", background="white")
        run_button = Button(self, text='Run', command=self.run, style="TButton")
        run_button.grid(column=0, row=4, **padding)

        reset_button = Button(self, text='Reset', command=self.reset, style="TButton")
        reset_button.grid(column=1, row=4, **padding)

        input_mess = Entry(self, textvariable=self.input_var)
        input_mess.grid(column=1, row=0, **padding)
        input_mess.focus()

        key = Entry(self, textvariable=self.key_var)
        key.grid(column=1, row=1, **padding)
        key.focus()

        result = Entry(self, textvariable=self.output_var)
        result.grid(column=1, row=2, **padding)
        result.focus()

        option_list = ["Encode", "Decode"]
        OptionMenu(self, self.option_var, option_list[0], *option_list).grid(column=1, row=3, **padding)

    def run(self):
        input_text = self.input_var.get()
        key_text = self.key_var.get()

        if input_text == '' or key_text == '':
            self.warning_label.config(text="Invalid !!! Input or(and) Key is(are) not given")
            self.warning_label.config(style='Error.TLabel')
        else:
            if self.option_var.get() == 'Encode':
                self.output_var.set(self.encode_mess(self.key_var.get(), input_text))
            else:
                self.output_var.set(self.decode_mess(self.key_var.get(), input_text))

    def encode_mess(self, key, message):
        enc = []
        for i in range(len(message)):
            key_c = key[i % len(key)]
            enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    def decode_mess(self, key, message):
        dec = []
        message = base64.urlsafe_b64decode(message).decode()
        for i in range(len(message)):
            key_c = key[i % len(key)]
            dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
        return "".join(dec)

    def reset(self):
        self.input_var.set('')
        self.output_var.set('')
        self.key_var.set('')


if __name__ == "__main__":
    app = Message_EnDe()
    app.mainloop()