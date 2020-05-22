
from tkinter import *


class Col1Buttons:
    panel_list = None
    menu_state = None
    menu_index = 0
    col2_buttons = None

    def set_col2_buttons(self, col2):
        self.col2_buttons = col2

    def set_panel_list(self, panels):
        self.panel_list = panels


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

        def down_com():
            self.menu_state = not self.menu_state
            print("Menu_state " + str(self.menu_state))

        def left_com():
            if self.col2_buttons.get_menu_state() and self.menu_index != 0:
                self.menu_index -= 1
                self.panel_list[self.menu_index].lift()

            print("LEFT Menu_index: " + str(self.menu_index))

        def right_com():
            if self.col2_buttons.get_menu_state() and self.menu_index != len(self.panel_list) - 1:
                self.menu_index += 1
                self.panel_list[self.menu_index].lift()
            print("RIGHT Menu_index: " + str(self.menu_index))

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







class Col2Buttons:
    col1_buttons = None
    menu_state = False
    dashboard = None

    def set_dashboard(self, dash):
        self.dashboard = dash

    def set_col1_buttons(self, col1):
        self.col1_buttons = col1

    def get_menu_state(self):
        return self.menu_state

    def __init__(self, root):
        self.root = root
        b_width = 5
        b_height = 2
        x_pad = 5
        y_pad = 50

    def yes_com():
        print("YES")
    def no_com():
        print("NO")
    def menu_com():
        self.menu_state = not self.menu_state
        if self.menu_state:
            b7.configure(bg="white", fg='#46637B')
        else:
            b7.configure(bg='#46637B', fg="white")
        print("Menu_state " + str(self.menu_state))
    def capture_com():
        self.dashboard.takeSnapshot()
        print("SNAP")

    # Buttons on the Second Column
    col2_frame = Frame(self.root, bg='#84A1B9')
    col2_frame.pack(side="right", fill="y")

    b5 = Button(col2_frame, text="YES", width=b_width, height=b_height, bg='#46637B', fg='white',
                font=("Courier", 10), command=yes_com)
    b5.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

    b6 = Button(col2_frame, text="NO", width=b_width, height=b_height, bg='#46637B', fg='white',
                font=("Courier", 10), command=no_com)
    b6.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

    b7 = Button(col2_frame, text="MENU", width=b_width, height=b_height, bg='#46637B', fg='white',
                font=("Courier", 10), command=menu_com)
    b7.pack(side="top", fill="both", padx=x_pad, pady=y_pad)

    b8 = Button(col2_frame, text="SNAP", width=b_width, height=b_height, bg='#46637B', fg='white',
                font=("Courier", 10), command=capture_com)
    b8.pack(side="top", fill="both", padx=x_pad, pady=y_pad)


# Buttons = Buttons()
# Buttons.root.mainloop()


