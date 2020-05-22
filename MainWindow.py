import tkinter as tk
from CaptureModeUI import CaptureModeUI
from MainMenuUI import MainMenuUI
from SensorModeUI import SensorModeUI
from Gallery import Gallery
from Dashboard import Dashboard
from DiagnosticsUI import DiagnosticsUI
from Buttons import Col1Buttons, Col2Buttons
from imutils.video import VideoStream
import time
import socket

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

class diagnosticMode:
    def __init__(self, root,conn):
        self.page = DiagnosticsUI(root,conn)
        
    def returnDiagnosicsUI(self):
        return self.page.DiagnosticsView()

class sensorMode:
   def __init__(self, root, *args, **kwargs):
      # Page.__init__(self, *args, **kwargs)
       self.page = SensorModeUI(root)
    
   def returnPage(self):
       return self.page.initializeSensorMode()
    
   def getInstance(self):
       return self.page

class gallery:
   def __init__(self, root, *args, **kwargs):
     #  Page.__init__(self, *args, **kwargs)
       self.page = Gallery(root)
    
   def returnPage(self):
       return self.page.initializeGallery()
    
   def getInstance(self):
       return self.page

class dashboard:
    def __init__(self, root, conn, capture, sensor, gallery):
    #   Page.__init__(self, *args, **kwargs)
    # initialize the video stream and allow the camera sensor to warmup
       print("[INFO] warming up camera...")
       time.sleep(2.0)
       outputFolder = "Media/Images"
       # start the app
       vs = VideoStream(usePiCamera=False)
       self.page = Dashboard(outputFolder, root, vs,conn, capture, sensor, gallery)
       
    def returnPage(self):
       return self.page.initializeDashboard()
    
    def getInstance(self):
       return self.page

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
       # tk.Frame.__init__(self,*args, **kwargs)
        root = tk.Tk()
        root.geometry("%dx%d+0+0" % (820, 600))
        
       # captureMode_panel = captureMode(root)
        mainMenu_panel = mainMenu(root)
        
        self.host = '169.254.153.172'
        self.port = 2304
    
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
        
        captureMode_btn = tk.Button(panel2, text= "Capture Mode", width=10, height= 5, bg='#46637B', fg='white', font=("Courier", 10),
                                   )
        captureMode_btn.pack(side="left",fill="both", padx=70, pady=10)
        
        gallery_btn = tk.Button(panel2, text= "Gallery",bg='#46637B', width=10, height= 5, fg='white', font=("Courier", 10))
        gallery_btn.pack(side="left",fill="both", padx=70, pady=10)

        # ---------------- Third Panel ----------------------------------
        panel3 = tk.Frame(master_panel, bg='#84A1B9')
        panel3.pack(fill="both", padx=20, pady=20)
        
        sensorMode_btn = tk.Button(panel3, text= "Sensor Mode", width=10, height= 5,bg='#46637B', fg='white', font=("Courier", 10),
                                   )
        sensorMode_btn.pack(side="left",fill="both", padx=70, pady=10)
        
        diagnostics_btn = tk.Button(panel3, text= "Diagnostics", width=10, height= 5,bg='#46637B', fg='white', font=("Courier", 10))
        diagnostics_btn.pack(side="left",fill="both", padx=60, pady=10)
 #---------------------------------------------------------------------------------------------------------
        
        c = captureMode(root)
        captureMode_panel = c.returnPage()
        
        s = sensorMode(root)
        sensorMode_panel = s.returnPage()
        
        g = gallery(root)
        gallery_panel = g.returnPage()
        
        conn = self.establishCommunication()
        
        d = dashboard(root, conn, c.getInstance(), s.getInstance(), g.getInstance())
        dashboard_panel = d.returnPage()
        
        diag = diagnosticMode(root, conn)
        diagnostics_panel = diag.returnDiagnosicsUI()
        
        panelList = [ master_panel, captureMode_panel, sensorMode_panel, gallery_panel, dashboard_panel, diagnostics_panel]    
            
        #Control button set up  
        buttons_1 = Col1Buttons(root, panelList)    
        buttons_1.initializeButtonColumn1() 
        buttons_2 = Col2Buttons(root, master_panel, d.getInstance())    
        buttons_2.initializeButtonColumn2()
        
        buttonframe = tk.Frame(root)
        container = tk.Frame(root)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        master_panel.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        captureMode_panel.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        sensorMode_panel.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        gallery_panel.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        dashboard_panel.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        diagnostics_panel.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Main Menu", command=master_panel.lift, font=("Courier", 9))
        b2 = tk.Button(buttonframe, text="Capture Mode", command=captureMode_panel.lift, font=("Courier", 9))
        b3 = tk.Button(buttonframe, text="Sensor Mode", command=sensorMode_panel.lift, font=("Courier", 9))
        b4 = tk.Button(buttonframe, text="Gallery", command=gallery_panel.lift, font=("Courier", 9))
        b5 = tk.Button(buttonframe, text="Dashboard", command=dashboard_panel.lift, font=("Courier", 9))
        b6 = tk.Button(buttonframe, text="Diagnostics", command=diagnostics_panel.lift, font=("Courier", 9))

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
        b6.pack(side="left")

        master_panel.lift()
        root.mainloop()
    
        
    def establishCommunication(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        return s

if __name__ == "__main__":
#     root = tk.Tk()
    main = MainView()
#     main.pack(side="top", fill="both", expand=True)
#     root.geometry("%dx%d+0+0" % (680, 600))
   # dashboard(root)
#     root.mainloop()

