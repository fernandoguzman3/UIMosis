import tkinter as tk

def tryf():
    HEIGHT = 380
    WIDTH = 600

    root = tk.Tk()



    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root)
    frame.place(relx=.15, rely=.1)
    title = tk.Label(frame, text="Sensor Mode")
    title.pack()

    frame = tk.Frame(root)
    frame.place(relx=.65, rely=.1)
    back_button = tk.Button(frame, text="Back", bg='purple')
    back_button.pack()

    frame = tk.Frame(root)
    frame.place(relx=.1, rely=.17)
    underline = tk.Label(frame, text="__________________________________________________________________________")
    underline.pack()


    frame = tk.Frame(root)
    frame.place(relx=.1, rely=.25)
    title = tk.Label(frame, text="Active Sensors:")
    title.pack()

    r = 0

    frame = tk.Frame(root)
    frame.place(relx=.3, rely=.25)
    ph_button = tk.Radiobutton(frame,text="PH", variable=r ,value=1)
    ph_button.pack()

    frame = tk.Frame(root)
    frame.place(relx=.41, rely=.25)
    temp_button = tk.Radiobutton(frame,text="Temp")
    temp_button.pack()

    frame = tk.Frame(root)
    frame.place(relx=.52, rely=.25)
    press_button = tk.Radiobutton(frame,text="Press")
    press_button.pack()

    frame = tk.Frame(root)
    frame.place(relx=.63, rely=.25)
    lumin_button = tk.Radiobutton(frame,text="Lumin")
    lumin_button.pack()

    frame = tk.Frame(root)
    frame.place(relx=.1, rely=.35)
    title = tk.Label(frame, text="Modes:")
    title.pack()

    frame = tk.Frame(root)
    frame.place(relx=.1, rely=.45)
    single_button = tk.Radiobutton(frame,text="Single")
    single_button.pack()

    frame = tk.Frame(root)
    frame.place(relx=.1, rely=.55)
    timelapse_button = tk.Radiobutton(frame,text="Time Lapse")
    timelapse_button.pack()

    frame = tk.Frame(root)
    frame.place(relx=.3, rely=.55)
    title = tk.Label(frame, text="Step:")
    title.pack()

    frame = tk.Frame(root)
    frame.place(relx=.37, rely=.53, relheight=.1, relwidth=.1)
    step_entry = tk.Entry(frame)
    step_entry.pack()

    frame = tk.Frame(root)
    frame.place(relx=.5, rely=.55)
    title = tk.Label(frame, text="Interval:")
    title.pack()

    frame = tk.Frame(root)
    frame.place(relx=.59, rely=.53, relheight=.1, relwidth=.1)
    interval_entry = tk.Entry(frame)
    interval_entry.pack()

    frame = tk.Frame(root)
    frame.place(relx=.2, rely=.67)
    default_button = tk.Radiobutton(frame,text="Same time lapse as set in camera")
    default_button.pack()


    root.mainloop()


