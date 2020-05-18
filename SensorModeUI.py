import tkinter as tki

class SensorModeUI:
    def __init__(self, root):
        
         # initialize the root window and image panel
        self.root = root
        self.sensorModeRBVar = tki.IntVar()
        self.actSensorRBVar = tki.IntVar()
        self.master_panel = None
        
    def initializeSensorMode(self):  
        self.master_panel = tki.Frame(self.root, bg='#46637B',height=600, width=800)
        self.master_panel.pack(fill="both")
        
        ocusis_label = tki.Label(self.master_panel, text= "OCUSIS", bg='#46637B', fg='white', font=("Courier", 24))
        ocusis_label.pack(fill="both", padx=20, pady=20)
        
        #----------------- Firstmost panel -------------------------------
        panel1 = tki.Frame(self.master_panel, bg='#46637B')
        panel1.pack(fill="both", padx=10, pady=10)
        
        capMode_label = tki.Label(panel1, text= "Sensor Mode ", bg='#46637B', fg='black', font=("Courier", 24))
        capMode_label.pack(side="left",fill="both", padx=20, pady=20)
        
        back_button = tki.Button(panel1, text= "Back")
        back_button.pack(side = "right", fill="both", padx=5, pady=5)
        
        fill_label = tki.Label(self.master_panel, text= "", height=1, bg="grey")
        fill_label.pack(fill="x", padx=5, pady=5)
        
        # ---------------- Second Panel ----------------------------------
        panel2 = tki.Frame(self.master_panel, bg='#84A1B9')
        panel2.pack(fill="both", padx=20, pady=20)
        
        actCams_label = tki.Label(panel2, text= "Active Sensors: ", bg='#84A1B9', fg='white', font=("Courier", 14))
        actCams_label.pack(side="left",fill="both", padx=2, pady=10)
        
        R3 = tki.Radiobutton(panel2, text="PH" , bg='#46637B', variable=self.actSensorRBVar, value=int(1),
                             fg='white', font=("Courier", 12))
        R3.pack(side="right",fill="both", padx=2, pady=10)
        
        R2 = tki.Radiobutton(panel2, text="Temp", bg='#46637B', variable=self.actSensorRBVar, value=int(2),
                             fg='white', font=("Courier", 12))
        R2.pack(side="right",fill="both", padx=2, pady=10)
        
        R1 = tki.Radiobutton(panel2, text="Press", bg='#46637B', variable=self.actSensorRBVar, value=int(3),
                             fg='white', font=("Courier", 12) )
        R1.pack(side="right",fill="both", padx=2, pady=10)
        
        R4 = tki.Radiobutton(panel2, text="Lumin", bg='#46637B', variable=self.actSensorRBVar, value=int(4),
                             fg='white', font=("Courier", 12) )
        R4.pack(side="right",fill="both", padx=2, pady=10)
        
        mode_label = tki.Label(self.master_panel, text= "Mode: ", bg='#46637B', height=2, fg='white', font=("Courier", 14))
        mode_label.pack(fill="x", padx=2, pady=2)
        
         # ---------------- Third Panel ----------------------------------
        panel3 = tki.Frame(self.master_panel, bg='#84A1B9')
        panel3.pack(side="top",fill="both", padx=20, pady=10)
        
        singleModeRB = tki.Radiobutton(panel3, text="Single", bg='#46637B', variable=self.sensorModeRBVar, value=int(1),
                                       fg='white', font=("Courier", 12) )
        singleModeRB.pack(side="left", fill="both", padx=5, pady=10)
        
        # ---------------- Fourth Panel ----------------------------------
        
        panel5 = tki.Frame(self.master_panel, bg='#84A1B9')
        panel5.pack(side="top",fill="both", padx=20, pady=10)
        
        timeLapseRB = tki.Radiobutton(panel5, text="Time Lapse", bg='#46637B', variable=self.sensorModeRBVar, value=int(2),
                                      fg='white', font=("Courier", 12) )
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
        
        panel6 = tki.Frame(self.master_panel, bg='#84A1B9')
        panel6.pack(side="top",fill="both", padx=20, pady=10)
        
        imageStackingRB = tki.Radiobutton(panel6, text="Set Time Lapse as set in camera mode",
                                          variable=self.sensorModeRBVar, value=int(3), bg='#46637B', fg='white', font=("Courier", 12) )
        imageStackingRB.pack(side="left", fill="both", padx=2, pady=10)
       
        fill_label2 = tki.Label(self.master_panel, bg='#46637B', height=2)
        fill_label2.pack(side="top",fill="both", padx=20, pady=10)
        
        return self.master_panel
    
    def getTimeIntervalValues(self):
        return self.sensorModeRBVar.get()