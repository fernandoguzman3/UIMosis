
import tkinter as tki

class SensorModeUI:
    def __init__(self, root):
        
         # initialize the root window and image panel
        self.root = root
        self.camRBVar = tki.IntVar()
        
        master_panel = tki.Frame(self.root, bg='#46637B',height=600, width=800)
        master_panel.pack(fill="both")
        
        ocusis_label = tki.Label(master_panel, text= "OCUSIS", bg='#46637B', fg='white', font=("Courier", 24))
        ocusis_label.pack(fill="both", padx=20, pady=20)
        
        #----------------- Firstmost panel -------------------------------
        panel1 = tki.Frame(master_panel, bg='#46637B')
        panel1.pack(fill="both", padx=10, pady=10)
        
        capMode_label = tki.Label(panel1, text= "Sensor Mode ", bg='#46637B', fg='black', font=("Courier", 24))
        capMode_label.pack(side="left",fill="both", padx=20, pady=20)
        
        back_button = tki.Button(panel1, text= "Back")
        back_button.pack(side = "right", fill="both", padx=5, pady=5)
        
        fill_label = tki.Label(master_panel, text= "", height=1, bg="grey")
        fill_label.pack(fill="x", padx=5, pady=5)
        
        # ---------------- Second Panel ----------------------------------
        panel2 = tki.Frame(master_panel, bg='#84A1B9')
        panel2.pack(fill="both", padx=20, pady=20)
        
        actCams_label = tki.Label(panel2, text= "Active Sensors: ",bg='#84A1B9', fg='white', font=("Courier", 14))
        actCams_label.pack(side="left",fill="both", padx=2, pady=10)
        
        R3 = tki.Radiobutton(panel2, text="PH", variable=self.camRBVar, value=3, bg='#46637B', fg='white', font=("Courier", 12))
        R3.pack(side="right",fill="both", padx=2, pady=10)
        
        R2 = tki.Radiobutton(panel2, text="Temp", variable=self.camRBVar, value=2, bg='#46637B', fg='white', font=("Courier", 12))
        R2.pack(side="right",fill="both", padx=2, pady=10)
        
        R1 = tki.Radiobutton(panel2, text="Press", variable=self.camRBVar, value=1, bg='#46637B', fg='white', font=("Courier", 12) )
        R1.pack(side="right",fill="both", padx=2, pady=10)
        
        R4 = tki.Radiobutton(panel2, text="Lumin", variable=self.camRBVar, value=1, bg='#46637B', fg='white', font=("Courier", 12) )
        R4.pack(side="right",fill="both", padx=2, pady=10)
        
        mode_label = tki.Label(master_panel, text= "Mode: ", bg='#46637B', height=2, fg='white', font=("Courier", 14))
        mode_label.pack(fill="x", padx=2, pady=2)
        
         # ---------------- Third Panel ----------------------------------
        panel3 = tki.Frame(master_panel, bg='#84A1B9')
        panel3.pack(side="top",fill="both", padx=20, pady=10)
        
        singleModeRB = tki.Radiobutton(panel3, text="Single", value=1, bg='#46637B', fg='white', font=("Courier", 12) )
        singleModeRB.pack(side="left", fill="both", padx=5, pady=10)
        
        # ---------------- Fourth Panel ----------------------------------
        
        panel5 = tki.Frame(master_panel, bg='#84A1B9')
        panel5.pack(side="top",fill="both", padx=20, pady=10)
        
        timeLapseRB = tki.Radiobutton(panel5, text="Time Lapse", value=3, bg='#46637B', fg='white', font=("Courier", 12) )
        timeLapseRB.pack(side="left", fill="both", padx=5, pady=10)
        
        intervalSB = tki.Spinbox(panel5, from_=0, to=5, bg='#46637B', width= 2, fg='white', font=("Courier", 12) )
        intervalSB.pack(side="right", fill="both", padx=10, pady=5)
        
        interval_label = tki.Label(panel5, text= "Interval:", bg='#84A1B9', height=2, fg='white', font=("Courier", 14))
        interval_label.pack(side="right",fill="x", padx=2, pady=2)
        
        stepSB = tki.Spinbox(panel5, from_=0, to=5, bg='#46637B', width= 2, fg='white', font=("Courier", 12) )
        stepSB.pack(side="right", fill="both", padx=10, pady=5)
        
        step_label = tki.Label(panel5, text= "Step:", bg='#84A1B9', fg='white', font=("Courier", 14))
        step_label.pack(side="right",fill="x", padx=2, pady=2)
        
        # ---------------- Sixth Panel ----------------------------------
        
        panel6 = tki.Frame(master_panel, bg='#84A1B9')
        panel6.pack(side="top",fill="both", padx=20, pady=10)
        
        imageStackingRB = tki.Radiobutton(panel6, text="Set Time Lapse as set in camera mode", value=4, bg='#46637B', fg='white', font=("Courier", 12) )
        imageStackingRB.pack(side="left", fill="both", padx=2, pady=10)
       
        fill_label2 = tki.Label(master_panel, bg='#46637B', height=2)
        fill_label2.pack(side="top",fill="both", padx=20, pady=10)
        
       # self.root.mainloop()

#CaptureModeUI()

        
# 
# 
# def tryf():
#     HEIGHT = 380
#     WIDTH = 600
# 
#     root = tk.Tk()
# 
# 
# 
#     canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
#     canvas.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.15, rely=.1)
#     title = tk.Label(frame, text="Sensor Mode")
#     title.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.65, rely=.1)
#     back_button = tk.Button(frame, text="Back", bg='purple')
#     back_button.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.1, rely=.17)
#     underline = tk.Label(frame, text="__________________________________________________________________________")
#     underline.pack()
# 
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.1, rely=.25)
#     title = tk.Label(frame, text="Active Sensors:")
#     title.pack()
# 
#     r = 0
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.3, rely=.25)
#     ph_button = tk.Radiobutton(frame,text="PH", variable=r ,value=1)
#     ph_button.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.41, rely=.25)
#     temp_button = tk.Radiobutton(frame,text="Temp")
#     temp_button.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.52, rely=.25)
#     press_button = tk.Radiobutton(frame,text="Press")
#     press_button.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.63, rely=.25)
#     lumin_button = tk.Radiobutton(frame,text="Lumin")
#     lumin_button.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.1, rely=.35)
#     title = tk.Label(frame, text="Modes:")
#     title.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.1, rely=.45)
#     single_button = tk.Radiobutton(frame,text="Single")
#     single_button.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.1, rely=.55)
#     timelapse_button = tk.Radiobutton(frame,text="Time Lapse")
#     timelapse_button.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.3, rely=.55)
#     title = tk.Label(frame, text="Step:")
#     title.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.37, rely=.53, relheight=.1, relwidth=.1)
#     step_entry = tk.Entry(frame)
#     step_entry.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.5, rely=.55)
#     title = tk.Label(frame, text="Interval:")
#     title.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.59, rely=.53, relheight=.1, relwidth=.1)
#     interval_entry = tk.Entry(frame)
#     interval_entry.pack()
# 
#     frame = tk.Frame(root)
#     frame.place(relx=.2, rely=.67)
#     default_button = tk.Radiobutton(frame,text="Same time lapse as set in camera")
#     default_button.pack()
# 
# 
#     root.mainloop()
# tryf()

