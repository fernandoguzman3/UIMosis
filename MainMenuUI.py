import tkinter as tki

class MainMenuUI:
    def __init__(self, root):
        
        # initialize the root window and image panel
        self.root = root
       # self.root.geometry("%dx%d+0+0" % (680, 600))
        
        master_panel = tki.Frame(self.root, bg='#46637B',height=600, width=800)
        master_panel.pack(anchor="w", fill="both", expand=False, side="left")
        
        #----------------- Firstmost panel -------------------------------
        ocusis_label = tki.Label(master_panel, text= "OCUSIS", bg='#46637B', fg='white', font=("Courier", 24))
        ocusis_label.pack(fill="both", padx=20, pady=20)
        
        panel1 = tki.Frame(master_panel, bg='#84A1B9')
        panel1.pack(fill="both", padx=10, pady=10)
        
        mainMenu_label = tki.Label(panel1, text= "Main Menu ", bg='#84A1B9', fg='white', font=("Courier", 24))
        mainMenu_label.pack(side="left",fill="both", padx=20, pady=20)
        
        back_button = tki.Button(panel1, text= "Back")
        back_button.pack(side = "right", fill="both", padx=5, pady=5)
        
        fill_label = tki.Label(master_panel, text= "", height=1, bg="grey")
        fill_label.pack(fill="x", padx=5, pady=5)
        
        # ---------------- Second Panel ----------------------------------
        panel2 = tki.Frame(master_panel, bg='#84A1B9')
        panel2.pack(fill="both", padx=20, pady=20)
        
        captureMode_btn = tki.Button(panel2, text= "Capture Mode", width=10, height= 5, bg='#46637B', fg='white', font=("Courier", 14))
        captureMode_btn.pack(side="left",fill="both", padx=90, pady=10)
        
        gallery_btn = tki.Button(panel2, text= "Gallery",bg='#46637B', width=10, height= 5, fg='white', font=("Courier", 14))
        gallery_btn.pack(side="left",fill="both", padx=100, pady=10)

        # ---------------- Third Panel ----------------------------------
        panel3 = tki.Frame(master_panel, bg='#84A1B9')
        panel3.pack(fill="both", padx=20, pady=20)
        
        sensorMode_btn = tki.Button(panel3, text= "Sensor Mode", width=10, height= 5,bg='#46637B', fg='white', font=("Courier", 14))
        sensorMode_btn.pack(side="left",fill="both", padx=90, pady=10)
        
        diagnostics_btn = tki.Button(panel3, text= "Diagnostics", width=10, height= 5,bg='#46637B', fg='white', font=("Courier", 14))
        diagnostics_btn.pack(side="left",fill="both", padx=100, pady=10)
