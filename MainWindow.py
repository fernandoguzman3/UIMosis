import tkinter as tk
from CaptureModeUI import CaptureModeUI
from MainMenuUI import MainMenuUI
from SensorModeUI import SensorModeUI
from Gallery import Gallery
from Dashboard import Dashboard
from imutils.video import VideoStream
import time

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class mainMenu(Page):
   def __init__(self,*args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       MainMenuUI(self)

class captureMode:
   def __init__(self, root, *args, **kwargs):
      # Page.__init__(self, *args, **kwargs)
       self.page = CaptureModeUI(root)

   def returnPage(self):
       return self.page.initializeCaptureMode()
    
   def getInstance(self):
       return self.page

class sensorMode:
   def __init__(self, root, *args, **kwargs):
      # Page.__init__(self, *args, **kwargs)
       self.page = SensorModeUI(root)
    
   def returnPage(self):
       return self.page.initializeSensorMode()
    
   def getInstance(self):
       return self.page

class gallery(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       Gallery(self)

class dashboard:
    def __init__(self, root, capture, sensor):
    #   Page.__init__(self, *args, **kwargs)
    # initialize the video stream and allow the camera sensor to warmup
       print("[INFO] warming up camera...")
       time.sleep(2.0)
       outputFolder = "Media/Images"
       # start the app
       vs = VideoStream(usePiCamera=False)
       self.page = Dashboard(outputFolder, root, vs, capture, sensor)
       
    def returnPage(self):
        return self.page.initializeDashboard()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
       # tk.Frame.__init__(self,*args, **kwargs)
        root = tk.Tk()
        root.geometry("%dx%d+0+0" % (670, 600))
        gallery_panel = gallery(root)
       # captureMode_panel = captureMode(root)
        mainMenu_panel = mainMenu(root)
    
         # initialize the root window and image panel
        #self.root = root
       # self.root.geometry("%dx%d+0+0" % (680, 600))
        
        master_panel = tk.Frame(root, bg='#46637B',height=600, width=800)
        master_panel.pack(anchor="w", fill="both", expand=False, side="left")
        
        #----------------- Firstmost panel -------------------------------
        ocusis_label = tk.Label(master_panel, text= "OCUSIS", bg='#46637B', fg='white', font=("Courier", 24))
        ocusis_label.pack(fill="both", padx=20, pady=20)
        
        panel1 = tk.Frame(master_panel, bg='#84A1B9')
        panel1.pack(fill="both", padx=10, pady=10)
        
        mainMenu_label = tk.Label(panel1, text= "Main Menu ", bg='#84A1B9', fg='white', font=("Courier", 24))
        mainMenu_label.pack(side="left",fill="both", padx=20, pady=20)
        
        back_button = tk.Button(panel1, text= "Back")
        back_button.pack(side = "right", fill="both", padx=5, pady=5)
        
        fill_label = tk.Label(master_panel, text= "", height=1, bg="grey")
        fill_label.pack(fill="x", padx=5, pady=5)
        
        # ---------------- Second Panel ----------------------------------
        panel2 = tk.Frame(master_panel, bg='#84A1B9')
        panel2.pack(fill="both", padx=20, pady=20)
        
        captureMode_btn = tk.Button(panel2, text= "Capture Mode", width=10, height= 5, bg='#46637B', fg='white', font=("Courier", 14),
                                   )
        captureMode_btn.pack(side="left",fill="both", padx=90, pady=10)
        
        gallery_btn = tk.Button(panel2, text= "Gallery",bg='#46637B', width=10, height= 5, fg='white', font=("Courier", 14))
        gallery_btn.pack(side="left",fill="both", padx=100, pady=10)

        # ---------------- Third Panel ----------------------------------
        panel3 = tk.Frame(master_panel, bg='#84A1B9')
        panel3.pack(fill="both", padx=20, pady=20)
        
        sensorMode_btn = tk.Button(panel3, text= "Sensor Mode", width=10, height= 5,bg='#46637B', fg='white', font=("Courier", 14),
                                   )
        sensorMode_btn.pack(side="left",fill="both", padx=90, pady=10)
        
        diagnostics_btn = tk.Button(panel3, text= "Diagnostics", width=10, height= 5,bg='#46637B', fg='white', font=("Courier", 14))
        diagnostics_btn.pack(side="left",fill="both", padx=100, pady=10)
 #---------------------------------------------------------------------------------------------------------
        
        c = captureMode(root)
        captureMode_panel = c.returnPage()
        
        s = sensorMode(root)
        sensorMode_panel = s.returnPage()
        
        d = dashboard(root, c.getInstance(), s.getInstance())
        dashboard_panel = d.returnPage()
        
        buttonframe = tk.Frame(root)
        container = tk.Frame(root)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        master_panel.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        captureMode_panel.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        sensorMode_panel.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        gallery_panel.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        dashboard_panel.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Main Menu", command=master_panel.lift)
        b2 = tk.Button(buttonframe, text="Capture Mode", command=captureMode_panel.lift)
        b3 = tk.Button(buttonframe, text="Sensor Mode", command=sensorMode_panel.lift)
        b4 = tk.Button(buttonframe, text="Gallery", command=gallery_panel.lift)
        b5 = tk.Button(buttonframe, text="Dashboard", command=dashboard_panel.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")

        master_panel.lift()
        root.mainloop()

if __name__ == "__main__":
#     root = tk.Tk()
    main = MainView()
#     main.pack(side="top", fill="both", expand=True)
#     root.geometry("%dx%d+0+0" % (680, 600))
   # dashboard(root)
#     root.mainloop()

