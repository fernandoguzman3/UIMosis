import tkinter as tk
from SensorModeUI import tryf
HEIGHT = 380
WIDTH = 600

def test_function():
    print("works")


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx=.15, rely=.1)
capture_mode_button = tk.Button(frame, text="Capture Mode", width=18, bg='orange')
capture_mode_button.pack()

frame = tk.Frame(root)
frame.place(relx=.6, rely=.1)
gallery_button = tk.Button(frame, text="Gallery", width=18, bg='green')
gallery_button.pack()

frame = tk.Frame(root)
frame.place(relx=.15, rely=.6)
sensor_mode_button = tk.Button(frame, text="Sensor Mode", width=18, bg='blue', command=tryf)
sensor_mode_button.pack()

frame = tk.Frame(root)
frame.place(relx=.6, rely=.6)
diagnostics_button = tk.Button(frame, text="Diagnostics", width=18, bg='red')
diagnostics_button.pack()

frame = tk.Frame(root)
frame.place(relx=.8, rely=.8)
back_button = tk.Button(frame, text="Back", width=10, bg='purple')
back_button.pack()


root.mainloop()

