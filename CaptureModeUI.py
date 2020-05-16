import tkinter as tki

class CaptureModeUI:
    def __init__(self):
        
         # initialize the root window and image panel
        self.root = tki.Tk()
        self.root.geometry("%dx%d+0+0" % (680, 600))
        
       # self.root = root
        self.camRBVar = tki.IntVar()
        
        master_panel = tki.Frame(self.root, bg='#46637B',height=600, width=800)
        master_panel.pack(fill="both")
        
        #----------------- Firstmost panel -------------------------------
        panel1 = tki.Frame(master_panel, bg='#84A1B9')
        panel1.pack(fill="both", padx=10, pady=10)
        
        capMode_label = tki.Label(panel1, text= "Capture Mode: ", bg='#84A1B9', fg='white', font=("Courier", 20))
        capMode_label.pack(side="left",fill="both", padx=20, pady=20)
        
        back_button = tki.Button(panel1, text= "Back")
        back_button.pack(side = "right", fill="both", padx=5, pady=5)
        
        fill_label = tki.Label(master_panel, text= "", height=2, bg="grey")
        fill_label.pack(fill="x", padx=5, pady=5)
        
        # ---------------- Second Panel ----------------------------------
        panel2 = tki.Frame(master_panel, bg='#84A1B9')
        panel2.pack(fill="both", padx=20, pady=20)
        
        actCams_label = tki.Label(panel2, text= "Active Cameras: ",bg='#84A1B9', fg='white', font=("Courier", 14))
        actCams_label.pack(side="left",fill="both", padx=2, pady=10)
        
        R3 = tki.Radiobutton(panel2, text="Both", variable=self.camRBVar, value=3, bg='#46637B', fg='white', font=("Courier", 12))
        R3.pack(side="right",fill="both", padx=2, pady=10)
        
        R2 = tki.Radiobutton(panel2, text="Right", variable=self.camRBVar, value=2, bg='#46637B', fg='white', font=("Courier", 12))
        R2.pack(side="right",fill="both", padx=2, pady=10)
        
        R1 = tki.Radiobutton(panel2, text="Left", variable=self.camRBVar, value=1, bg='#46637B', fg='white', font=("Courier", 12) )
        R1.pack(side="right",fill="both", padx=2, pady=10)
        
        R4 = tki.Radiobutton(panel2, text="None", variable=self.camRBVar, value=1, bg='#46637B', fg='white', font=("Courier", 12) )
        R4.pack(side="right",fill="both", padx=2, pady=10)
        
        mode_label = tki.Label(master_panel, text= "Mode: ", bg='#46637B', height=2, fg='white', font=("Courier", 14))
        mode_label.pack(fill="x", padx=2, pady=2)
        
         # ---------------- Third Panel ----------------------------------
        panel3 = tki.Frame(master_panel, bg='#84A1B9')
        panel3.pack(side="top",fill="both", padx=20, pady=10)
        
        singleModeRB = tki.Radiobutton(panel3, text="Single Mode", variable=self.camRBVar, value=1, bg='#46637B', fg='white', font=("Courier", 12) )
        singleModeRB.pack(side="left", fill="both", padx=5, pady=10)
        
        # ---------------- Fourth Panel ----------------------------------
        
        panel4 = tki.Frame(master_panel, bg='#84A1B9')
        panel4.pack(side="top",fill="both", padx=20, pady=10)
        
        burstModeRB = tki.Radiobutton(panel4, text="Burst Mode", value=2, bg='#46637B', fg='white', font=("Courier", 12) )
        burstModeRB.pack(side="left", fill="both", padx=5, pady=10)
        
        burstNumSB = tki.Spinbox(panel4, from_=0, to=5,width= 2, bg='#46637B', fg='white', font=("Courier", 12) )
        burstNumSB.pack(side="right", fill="both", padx=10, pady=5)
        
        burstMode_label = tki.Label(panel4, text= "Burst number: ", bg='#84A1B9', height=2, fg='white', font=("Courier", 14))
        burstMode_label.pack(side="right",fill="x", padx=2, pady=2)
        
         # ---------------- Fifth Panel ----------------------------------
        
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
        
        imageStackingRB = tki.Radiobutton(panel6, text="Image Stacking", value=4, bg='#46637B', fg='white', font=("Courier", 12) )
        imageStackingRB.pack(side="left", fill="both", padx=2, pady=10)
        
        op3RB = tki.Radiobutton(panel6, text="Option 3", value=1, bg='#46637B', fg='white', font=("Courier", 12) )
        op3RB.pack(side="right", fill="both", padx=2, pady=5)
        
        op2RB = tki.Radiobutton(panel6, text="Option 2", value=1, bg='#46637B', fg='white', font=("Courier", 12) )
        op2RB.pack(side="right", fill="both", padx=2, pady=5)
        
        op1RB = tki.Radiobutton(panel6, text="Option 1", value=1, bg='#46637B', fg='white', font=("Courier", 12) )
        op1RB.pack(side="right", fill="both", padx=2, pady=5)
        
        fill_label2 = tki.Label(master_panel, bg='#46637B', height=2)
        fill_label2.pack(side="top",fill="both", padx=20, pady=10)
        
        self.root.mainloop()

CaptureModeUI()

        