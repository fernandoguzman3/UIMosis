import tkinter as tki
from tkinter.filedialog import asksaveasfile, askdirectory
import os
from PIL import ImageTk
from PIL import Image
import cv2

class Gallery:
    def __init__(self, root):
        
        self.image = None
         # initialize the root window and image panel
        self.root = root
        self.camRBVar = tki.IntVar()
        self.count = 0
        self.panel2b2 = None
        self.dirName = 'Media/Images'
        self.master_panel = None
        self.listOfFile = list()
        
    def initializeGallery(self):
        self.master_panel = tki.Frame(self.root, bg='#46637B',height=600, width=800)
        self.master_panel.pack(fill="both")
        
        ocusis_label = tki.Label(self.master_panel, text= "OCUSIS", bg='#46637B', fg='white', font=("Courier", 24))
        ocusis_label.pack(fill="both", padx=20, pady=5)
        
        #----------------- Firstmost panel -------------------------------
        panel1 = tki.Frame(self.master_panel, bg='#46637B')
        panel1.pack(fill="both", padx=10, pady=10)
        
        capMode_label = tki.Label(panel1, text= "Gallery ", bg='#46637B', fg='black', font=("Courier", 24))
        capMode_label.pack(side="left",fill="both", padx=20, pady=20)
        
        back_button = tki.Button(panel1, text= "Back")
        back_button.pack(side = "right", fill="both", padx=5, pady=5)
        
        fill_label = tki.Label(self.master_panel, text= "", height=1, bg="grey")
        fill_label.pack(fill="x", padx=5, pady=5)
        
        # ---------------- Second Panel ----------------------------------
        panel2 = tki.Frame(self.master_panel, bg='#84A1B9')
        panel2.pack(fill="both", padx=5, pady=5)
        
        panel2a = tki.Frame(panel2, bg='#84A1B9', height= 300)
        panel2a.pack(side="left",fill="both", padx=20, pady=10)
        
        data_label = tki.Label(panel2a, text= "Data: ", bg='#84A1B9')
        data_label.pack(fill="x", padx=5, pady=5)
        
        sensor_button = tki.Button(panel2a, text= "Sensors")
        sensor_button.pack( fill="x", padx=5, pady=5)
        
        images_button = tki.Button(panel2a, text= "Images")
        images_button.pack(fill="x", padx=5, pady=5)
        
        fill_label2 = tki.Label(panel2a, text= "", bg='#84A1B9', height=11)
        fill_label2.pack(fill="both", padx=5, pady=5)
        
#         save_button = tki.Button(panel2a, text= "Save To", command=self.saveTo)
#         save_button.pack( side= "bottom", fill="x", padx=5, pady=5)
#         
        panel2b = tki.Frame(panel2, bg='#004000', width=300)
        panel2b.pack(side="left",fill="both", padx=20, pady=2)
        
        panel2b1 = tki.Frame(panel2b, bg='#84A1B9')
        panel2b1.pack(side="top",fill="x", padx=5, pady=5)
        
        fill_label3 = tki.Label(panel2b1, text= "Preview", bg='#84A1B9', width=300)
        fill_label3.pack(fill="x", padx=5, pady=5)
        
        self.panel2b2 = tki.Frame(panel2b, bg='#004000')
        self.panel2b2.pack(side="top",fill="both", padx=2, pady=2)
        
        self.getListOfFiles()
        
        return self.master_panel
        
    def getListOfFiles(self):
        # create a list of file and sub directories 
        # names in the given directory 
        self.listOfFile = os.listdir(self.dirName)
        self.allFiles = list()
        
        for widget in self.panel2b2.winfo_children():
            widget.destroy()
        
        self.count = 0
        pic_frame = tki.Frame(self.panel2b2, bg='#004000')
        pic_frame.pack(side="top",fill="both", padx=2, pady=2)
        # Iterate over all the entries
        for entry in self.listOfFile:
            if(self.count > 4):
                pic_frame = tki.Frame(self.panel2b2, bg='#004000')
                pic_frame.pack(side="top",fill="both", padx=2, pady=2)
                self.count = 0
    
            # Create full path
            fullPath = os.path.join(self.dirName, entry)
            
            width = 80
            height = 80
            img = Image.open(fullPath)
            img = img.resize((width,height), Image.ANTIALIAS)
            self.img =  ImageTk.PhotoImage(img)
            
            pic = tki.Button(pic_frame, image=self.img, height=60, compound='bottom', font=("Courier", 8))
            pic.image = self.img
            pic.pack(side="left", padx=5, pady=5)
            
            self.count += 1
            
    def saveTo(self):
        filename = askdirectory()
        if not filename:
            return
        for entry in self.listOfFile:
            fullPath = os.path.join(self.dirName, entry)
            print(fullPath)
            img = cv2.imread(fullPath)
            edge = Image.fromarray(img)
            edge.save(filename)
        
        
        
