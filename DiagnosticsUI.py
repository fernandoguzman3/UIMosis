import tkinter as tk

class DiagnosticsUI:

    def __init__(self, root):
        self.root = root

    def DiagnosticsView(self):

        self.master_panel = tk.Frame(self.root, bg='#46637B', height=600, width=800)
        self.master_panel.pack(fill="both")

        canvas = tk.Canvas(self.master_panel, height=600, width=600)
        canvas.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.1)
        title = tk.Label(frame, text="Diagnostics")
        title.pack()


        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.2)
        back_button = tk.Button(frame, text="Run Diagnostics", bg='blue')
        back_button.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.3)
        title = tk.Label(frame, text="Lumin Sensor")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.3)
        title = tk.Label(frame, text="OK")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.4)
        title = tk.Label(frame, text="Press Sensor")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.4)
        title = tk.Label(frame, text="OK")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.5)
        title = tk.Label(frame, text="Temp Sensor")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.5)
        title = tk.Label(frame, text="OK")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.6)
        title = tk.Label(frame, text="PH Sensor")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.6)
        title = tk.Label(frame, text="OK")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.7)
        title = tk.Label(frame, text="Leak Sensor")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.7)
        title = tk.Label(frame, text="OK")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.8)
        title = tk.Label(frame, text="Camera")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.8)
        title = tk.Label(frame, text="OK")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.9)
        title = tk.Label(frame, text="Communication")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.9)
        title = tk.Label(frame, text="OK")
        title.pack()

        return self.master_panel


