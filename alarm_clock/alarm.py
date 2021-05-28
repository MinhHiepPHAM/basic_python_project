from tkinter import *
from tkinter.ttk import *
import datetime
import time

try:
    import winsound
except ImportError:
    import os

    def play(frequency, duration):
        print('abc')
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, frequency))
else:
    def play(frequency, duration):
        winsound.Beep(frequency, duration)


class Alarm_clock(Tk):
    def __init__(self):
        super().__init__()

        self.title('Alarm clock')
        self.geometry("300x200")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.hour_var = StringVar()
        self.minute_var = StringVar()
        self.second_var = StringVar()

        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 2, 'pady': 2}
        Style().configure("TButton", foreground="red", background="white")
        Button(self, text='Alarm', command=self.set_alarm, style="TButton").grid(column=1, row=1, **padding)

        hour_list = ['00', '01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12', '13', '14', '15',
                     '16', '17', '18', '19', '20', '21', '22', '23']
        mi_se_list = ['00', '01', '02', '03', '04', '05', '06', '07',
                      '08', '09', '10', '11', '12', '13', '14', '15',
                      '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '31',
                      '32', '33', '34', '35', '36', '37', '38', '39',
                      '40', '41', '42', '43', '44', '45', '46', '47',
                      '48', '49', '50', '51', '52', '53', '54', '55',
                      '56', '57', '58', '59', '60']

        OptionMenu(self, self.hour_var, hour_list[0], *hour_list).grid(column=0, row=0, **padding)
        OptionMenu(self, self.minute_var, hour_list[0], *mi_se_list).grid(column=1, row=0, **padding)
        OptionMenu(self, self.second_var, hour_list[0], *mi_se_list).grid(column=2, row=0, **padding)

    def set_alarm(self):

        alarm_time = f'{self.hour_var.get()}:{self.minute_var.get()}:{self.second_var.get()}'
        while True:
            time.sleep(1)
            if alarm_time == datetime.datetime.now().strftime("%H:%M:%S"):
                play(500, 10)
                break


if __name__ == "__main__":
    app = Alarm_clock()
    app.mainloop()
