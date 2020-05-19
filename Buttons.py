
from tkinter import *


class Col1Buttons:
    objeto = None
    def __init__(self, root):

        # self.root.geometry("%dx%d+0+0" % (680, 600))

        # main_frame = Frame(root, bg='#46637B', height=680, width=600)
        # main_frame.pack(fill="both", expand=1)

        b_width = 5
        b_height = 2
        x_pad = 5
        y_pad = 50

        # Buttons on the First Column
        col1_frame = Frame(root, bg='#84A1B9')
        col1_frame.pack(side="left", fill="y")


        def up_com():
            print("UP")
            self.objeto.lift()
        def down_com():
            print("DOWN")
        def left_com():
            print("LEFT")
        def right_com():
            print("RIGHT")

        b1 = Button(col1_frame, text="UP", width=b_width, height= b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=up_com)
        b1.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b2 = Button(col1_frame, text="DOWN", width=b_width, height= b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=down_com)
        b2.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b3 = Button(col1_frame, text="LEFT", width=b_width, height= b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=left_com)
        b3.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b4 = Button(col1_frame, text="RIGHT", width=b_width, height= b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=right_com)
        b4.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

    def set_obj(self, obj):
        self.objeto = obj





class Col2Buttons:
    objeto = None
    def set_obj(self, obj):
        self.objeto = obj
    def __init__(self, root):
        self.root = root
        b_width = 5
        b_height = 2
        x_pad = 5
        y_pad = 50

        # Buttons on the Second Column
        col2_frame = Frame(root, bg='#84A1B9')
        col2_frame.pack(side="right", fill="y")

        def yes_com():
            print("YES")
        def no_com():
            print("NO")
        def menu_com():
            print("MENU")
            self.objeto.lift()
        def idk_com():
            print("IDK")

        b5 = Button(col2_frame, text="YES", width=b_width, height=b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=yes_com)
        b5.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b6 = Button(col2_frame, text="NO", width=b_width, height=b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=no_com)
        b6.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b7 = Button(col2_frame, text="MENU", width=b_width, height=b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=menu_com)
        b7.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

        b8 = Button(col2_frame, text="idk", width=b_width, height=b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=idk_com)
        b8.pack(side="top", fill="both", padx=x_pad, pady=y_pad)


# Buttons = Buttons()
# Buttons.root.mainloop()


