import tkinter as tk
import RPi.GPIO as GPIO  

class DiagnosticsUI:

    def __init__(self, root, s):
        self.root = root
        self.LuminStat = tk.StringVar()
        self.PressStat = tk.StringVar()
        self.TempStat = tk.StringVar()
        self.PHStat = tk.StringVar()
        self.LeakStat = tk.StringVar()
        self.CameraStat = tk.StringVar()
        self.CommStat = tk.StringVar()
        self.s = s

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
        back_button = tk.Button(frame, text="Run Diagnostics", bg='blue', command=self.getStats)
        back_button.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.3)
        title = tk.Label(frame, text="Lumin Sensor")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.3)
        title = tk.Label(frame, text="", textvariable=self.LuminStat)
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.4)
        title = tk.Label(frame, text="Press Sensor")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.4)
        title = tk.Label(frame, text="",textvariable=self.PressStat)
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.5)
        title = tk.Label(frame, text="Temp Sensor")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.5)
        title = tk.Label(frame, text="",textvariable=self.TempStat)
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.6)
        title = tk.Label(frame, text="PH Sensor")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.6)
        title = tk.Label(frame, text="", textvariable=self.PHStat)
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.15, rely=.7)
        title = tk.Label(frame, text="Leak Sensor")
        title.pack()

        frame = tk.Frame(self.master_panel)
        frame.place(relx=.35, rely=.7)
        title = tk.Label(frame, text="OK",textvariable=self.LeakStat)
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
    
    def getStats(self):
        self.s.send(str.encode("STATUS ALL"))
        reply = self.s.recv(1024)
        reply = reply.decode('utf-8')
        rlist =reply.split(',')
        self.TempStat.set(rlist[0])
        self.PHStat.set(rlist[1])
        self.LuminStat.set(rlist[2])
        self.PressStat.set(rlist[3])
        print(rlist[4])
        if(rlist[4] == "WARNING"):
            self.LeakStat.set("WARNING")
            GPIO.output(6,GPIO.LOW)
        else:
            GPIO.output(6,GPIO.HIGH)
            self.LeakStat.set("OK")
        


