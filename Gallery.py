
import tkinter as tki

class Gallery:
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
        
        capMode_label = tki.Label(panel1, text= "Gallery ", bg='#46637B', fg='black', font=("Courier", 24))
        capMode_label.pack(side="left",fill="both", padx=20, pady=20)
        
        back_button = tki.Button(panel1, text= "Back")
        back_button.pack(side = "right", fill="both", padx=5, pady=5)
        
        fill_label = tki.Label(master_panel, text= "", height=1, bg="grey")
        fill_label.pack(fill="x", padx=5, pady=5)
        
        # ---------------- Second Panel ----------------------------------
        panel2 = tki.Frame(master_panel, bg='#84A1B9')
        panel2.pack(fill="both", padx=20, pady=20)
        
        panel2a = tki.Frame(panel2, bg='#84A1B9')
        panel2a.pack(side="left",fill="both", padx=20, pady=10)
        
        data_label = tki.Label(panel2a, text= "Data: ", bg='#84A1B9')
        data_label.pack(fill="x", padx=5, pady=5)
        
        sensor_button = tki.Button(panel2a, text= "Sensors")
        sensor_button.pack( fill="x", padx=5, pady=5)
        
        images_button = tki.Button(panel2a, text= "Images")
        images_button.pack(fill="x", padx=5, pady=5)
        
        save_button = tki.Button(panel2a, text= "Save To")
        save_button.pack( fill="x", padx=5, pady=5)
        
        panel2b = tki.Frame(panel2, bg='#84A1B9')
        panel2b.pack(side="left",fill="both", padx=20, pady=10)
        
#         
#         directory = os.fsencode(directory_in_str)
# 
#         for file in os.listdir(directory):
#              filename = os.fsdecode(file)
#              if filename.endswith(".asm") or filename.endswith(".py"): 
#                  # print(os.path.join(directory, filename))
#                  continue
#              else:
#                  continue
        
