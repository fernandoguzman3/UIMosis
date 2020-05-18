
from tkinter import *


class Buttons:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("%dx%d+0+0" % (680, 600))
        main_frame = Frame(self.root, bg='#46637B', height=600, width=400)
        main_frame.pack(fill="both", expand=1)

        b_width = 5
        b_height = 2
        x_pad = 5
        y_pad = 50

        # Buttons on the First Column
        col1_frame = Frame(main_frame, bg='#84A1B9')
        col1_frame.pack(side="left", fill="y")

        b1 = Button(col1_frame, text="b1", width=b_width, height= b_height, bg='#46637B', fg='white', font=("Courier", 10))
        b1.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b2 = Button(col1_frame, text="b2", width=b_width, height= b_height, bg='#46637B', fg='white', font=("Courier", 10))
        b2.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b3 = Button(col1_frame, text="b3", width=b_width, height= b_height, bg='#46637B', fg='white', font=("Courier", 10))
        b3.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b4 = Button(col1_frame, text="b4", width=b_width, height= b_height, bg='#46637B', fg='white', font=("Courier", 10))
        b4.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        #Buttons on the Second Column
        col2_frame = Frame(main_frame, bg='#84A1B9')
        col2_frame.pack(side="right", fill="y")

        b5 = Button(col2_frame, text="b5", width=b_width, height= b_height, bg='#46637B', fg='white', font=("Courier", 10))
        b5.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b6 = Button(col2_frame, text="b6", width=b_width, height= b_height, bg='#46637B', fg='white', font=("Courier", 10))
        b6.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b7 = Button(col2_frame, text="b7", width=b_width, height= b_height, bg='#46637B', fg='white', font=("Courier", 10))
        b7.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b8 = Button(col2_frame, text="b8", width=b_width, height= b_height, bg='#46637B', fg='white', font=("Courier", 10))
        b8.pack(side="top", fill="both", padx=x_pad, pady=y_pad)


Buttons = Buttons()
Buttons.root.mainloop()


