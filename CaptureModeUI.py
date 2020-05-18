import tkinter as tki

class CaptureModeUI:
    def __init__(self, root):
        
         # initialize the root window and image panel
        self.root = root
      #  self.root.geometry("%dx%d+0+0" % (680, 600))
        
       # self.root = root
        self.modeRBVar = tki.IntVar()
        self.camRBVar = tki.IntVar()
        
        self.stepSB = None
        self.intervalSB = None
        self.burstSB = None
        
        self.master_panel = None
        
    def initializeCaptureMode(self):    
        self.master_panel = tki.Frame(self.root, bg='#46637B',height=600, width=800)
        self.master_panel.pack(fill="both")
        
        ocusis_label = tki.Label(self.master_panel, text= "OCUSIS", bg='#46637B', fg='white', font=("Courier", 24))
        ocusis_label.pack(fill="both", padx=20, pady=20)
        
        #----------------- Firstmost panel -------------------------------
        panel1 = tki.Frame(self.master_panel, bg='#46637B')
        panel1.pack(fill="both", padx=10, pady=5)
        
        capMode_label = tki.Label(panel1, text= "Capture Mode ", bg='#46637B', fg='black', font=("Courier", 24))
        capMode_label.pack(side="left",fill="both", padx=20, pady=20)
        
        back_button = tki.Button(panel1, text= "Back")
        back_button.pack(side = "right", fill="both", padx=5, pady=5)
        
        fill_label = tki.Label(self.master_panel, text= "", height=1, bg="grey")
        fill_label.pack(fill="x", padx=5, pady=5)
        
        # ---------------- Second Panel ----------------------------------
        panel2 = tki.Frame(self.master_panel, bg='#84A1B9')
        panel2.pack(fill="both", padx=20, pady=5)
        
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
        
        mode_label = tki.Label(self.master_panel, text= "Mode: ", bg='#46637B', height=2, fg='white', font=("Courier", 14))
        mode_label.pack(fill="x", padx=2, pady=2)
        
         # ---------------- Third Panel ----------------------------------
        panel3 = tki.Frame(self.master_panel, bg='#84A1B9')
        panel3.pack(side="top",fill="both", padx=20, pady=5)
        
        singleModeRB = tki.Radiobutton(panel3, text="Single Mode", variable=self.modeRBVar, value=int(1),selectcolor='red', bg='#46637B',
                                       fg='white', font=("Courier", 12))
        singleModeRB.pack(side="left", fill="both", padx=5, pady=10)
        
        # ---------------- Fourth Panel ----------------------------------
        
        panel4 = tki.Frame(self.master_panel, bg='#84A1B9')
        panel4.pack(side="top",fill="both", padx=20, pady=5)
        
        burstModeRB = tki.Radiobutton(panel4, text="Burst Mode", variable=self.modeRBVar,value=int(2), selectcolor='red',bg='#46637B',
                                      fg='white', font=("Courier", 12) )
        burstModeRB.pack(side="left", fill="both", padx=5, pady=10)
        
        burstNumSB = tki.Spinbox(panel4, from_=2, to=5,width= 2, bg='#46637B', fg='white', font=("Courier", 12) )
        burstNumSB.pack(side="right", fill="both", padx=10, pady=5)
        self.burstSB = burstNumSB
        
        burstMode_label = tki.Label(panel4, text= "Burst number: ", bg='#84A1B9', height=2, fg='white', font=("Courier", 14))
        burstMode_label.pack(side="right",fill="x", padx=2, pady=2)
        
         # ---------------- Fifth Panel ----------------------------------
        
        panel5 = tki.Frame(self.master_panel, bg='#84A1B9')
        panel5.pack(side="top",fill="both", padx=20, pady=5)
        
        timeLapseRB = tki.Radiobutton(panel5, text="Time Lapse", variable=self.modeRBVar, value=int(3), selectcolor='red',bg='#46637B',
                                      fg='white', font=("Courier", 12))
        timeLapseRB.pack(side="left", fill="both", padx=5, pady=10)
        
        intervalSB = tki.Spinbox(panel5, from_=1, to=5, bg='#46637B', width= 2, fg='white', font=("Courier", 12) )
        intervalSB.pack(side="right", fill="both", padx=10, pady=5)
        self.intervalSB = intervalSB
        
        interval_label = tki.Label(panel5, text= "Interval (min):", bg='#84A1B9', height=2, fg='white', font=("Courier", 14))
        interval_label.pack(side="right",fill="x", padx=2, pady=2)
        
        stepSB = tki.Spinbox(panel5, from_=10, to=60, increment=10, bg='#46637B', width= 2, fg='white', font=("Courier", 12) )
        stepSB.pack(side="right", fill="both", padx=10, pady=5)
        self.stepSB = stepSB
        
        step_label = tki.Label(panel5, text= "Step (sec):", bg='#84A1B9', fg='white', font=("Courier", 14))
        step_label.pack(side="right",fill="x", padx=2, pady=2)
        
        # ---------------- Sixth Panel ----------------------------------
        
        panel6 = tki.Frame(self.master_panel, bg='#84A1B9')
        panel6.pack(side="top",fill="both", padx=20, pady=5)
        
        imageStackingRB = tki.Radiobutton(panel6, text="Image Stacking", variable=self.modeRBVar, value=int(4),selectcolor='red', bg='#46637B',
                                          fg='white', font=("Courier", 12) )
        imageStackingRB.pack(side="left", fill="both", padx=2, pady=10)
        
        op3RB = tki.Radiobutton(panel6, text="Option 3", value=1, bg='#46637B', fg='white', font=("Courier", 12) )
        op3RB.pack(side="right", fill="both", padx=2, pady=5)
        
        op2RB = tki.Radiobutton(panel6, text="Option 2", value=2, bg='#46637B', fg='white', font=("Courier", 12) )
        op2RB.pack(side="right", fill="both", padx=2, pady=5)
        
        op1RB = tki.Radiobutton(panel6, text="Option 1", value=3, bg='#46637B', fg='white', font=("Courier", 12) )
        op1RB.pack(side="right", fill="both", padx=2, pady=5)
        
        fill_label2 = tki.Label(self.master_panel, bg='#46637B', height=2)
        fill_label2.pack(side="top",fill="both", padx=20, pady=10)
        
        imageStackingRB.deselect()
        timeLapseRB.deselect()
        burstModeRB.deselect()
        singleModeRB.select()
        
       # self.root.mainloop()
        return self.master_panel
       
    def getCaptureModeValues(self):
        return self.modeRBVar.get()
    
    def getBurstModeValues(self):
        return self.burstSB.get()
    
    def getStepsValues(self):
        return self.stepSB.get()
    
    def getIntervalValues(self):
        return self.intervalSB.get()

#CaptureModeUI()

        