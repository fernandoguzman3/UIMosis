# import the necessary packages
from __future__ import print_function
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
import tkinter as tki
import threading
import logging
import datetime
import imutils
import cv2
import numpy as np
import os

class PhotoBoothApp:
    def __init__(self, vs, outputPath):
        logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )
        
        # store the video stream object and output path, then initialize
        # the most recently read frame, thread for reading frames, and
        # the thread stop event
        self.vs = vs
        self.outputPath = outputPath
        self.frame = None
        self.thread = None
        self.stopEvent = None
        
        # initialize the root window and image panel
        self.root = tki.Tk()
    #    self.root.maxsize(900, 600)
    #    self.root.minsize(900, 600)
        self.root.geometry("%dx%d+0+0" % (680, 600))
        self.upper_panel = None
        self.image = None
        self.imageW = 640
        self.imageH = 480
        self.imageSize = 800
        
        #--------- UI elements variables
        self.zoom = False
        self.zoomValue = 1
        self.saturationValue = float(1)
        self.exposureValue = float(1)
        self.brightValue = float(0.2)
        self.sysMode = tki.StringVar()
        self.ledMode = tki.StringVar()
        
        #---------------- LOWER PANEL----------------------------------#
        
         #lower panel to house the picture scales, led, mode and sensor info
        lower_panel = tki.Frame(self.root, bg='#46637B')
        lower_panel.pack(side="bottom", fill="both", padx=2, pady=2)
        
        #---------------- Scales PANEL----------------------------------#
        
        #panel for the scales
        scale_panel = tki.Frame(lower_panel, bg='#004000')
        scale_panel.pack(side="left", fill="both", padx=2, pady=2)        
        
        params_label = tki.Label(scale_panel, text= "Camera Frame params: ")
        params_label.pack(side="top",fill="x", padx=5, pady=5)
        
        #panel for the scales
        sub_scale_panelL = tki.Frame(scale_panel, bg='#004000')
        sub_scale_panelL.pack(side="left", fill="both", padx=5, pady=5)
        
        #panel for the scales
        sub_scale_panelR = tki.Frame(scale_panel, bg='#004000')
        sub_scale_panelR.pack(side="left", fill="both", padx=5, pady=5)
        
        zoomScale = tki.Scale(sub_scale_panelL, from_=1, to=5, orient=tki.HORIZONTAL, width= 5, troughcolor= "#004000", bg='#84A1B9',label = "Zoom", command = self.setZoom)
        zoomScale.pack(side="top", fill="none", padx=2, pady=2)
        
        exposureScale = tki.Scale(sub_scale_panelL, from_=0.2, to=3.0, resolution=0.20, orient=tki.HORIZONTAL, width= 5, troughcolor= "#004000", bg='#84A1B9',label = "Exposure", command = self.setExposure)
        exposureScale.pack(side="top", fill="none", padx=2, pady=2)
        
        saturationScale = tki.Scale(sub_scale_panelR, from_=0.2, to=8, resolution=0.20, orient=tki.HORIZONTAL, width= 5,troughcolor= "#004000", bg='#84A1B9',label = "Saturation", command = self.setSaturation)
        saturationScale.pack(side="top", fill="none", padx=2, pady=2)
        
        brightnessScale = tki.Scale(sub_scale_panelR, from_=1, to=120, orient=tki.HORIZONTAL, width= 5,troughcolor= "#004000", bg='#84A1B9',label = "Brightness", command = self.setBrightness)
        brightnessScale.pack(side="top", fill="none", padx=2, pady=2)
        
        #---------------- Mode configuration PANEL----------------------------------#
        
        #panel for led / mode info
        modeConfig_panel = tki.Frame(lower_panel, bg='#004000', width=50, height=50)
        modeConfig_panel.pack(side="left", fill="both", padx=2, pady=2) 
        
        modeConfig_panelU = tki.Frame(modeConfig_panel, bg='#004000',width=25, height=50)
        modeConfig_panelU.pack(side="left", fill="both",padx=5, pady=5)
        
        modeConfig_panelR = tki.Frame(modeConfig_panel, bg='#004000',width=25, height=50)
        modeConfig_panelR.pack(side="left", fill="both", padx=5, pady=5)
        
        mode_label = tki.Label(modeConfig_panelU, text= "Mode: ", width= 10)
        mode_label.pack( fill="both", padx=2, pady=2)
        
        mode_var_label = tki.Label(modeConfig_panelU, textvariable = self.sysMode, bg="#84A1B9")
        mode_var_label.pack( fill="both", padx=2, pady=2)
        
        LED_mode_label = tki.Label(modeConfig_panelR, text= "LED light selected: ")
        LED_mode_label.pack(fill="both", padx=2, pady=2)
        
        LED_var_label = tki.Label(modeConfig_panelR, textvariable = self.ledMode, bg="#84A1B9")
        LED_var_label.pack( fill="both", padx=2, pady=2)
        
        #---------------- Sensor PANEL----------------------------------#
        
        #panel for the activated sensors
        sensor_panel = tki.Frame(lower_panel, bg='#004000', width=200, height=100)
        sensor_panel.pack(side="left", fill="both", padx=2, pady=2)
        
        act_sensor_label = tki.Label(sensor_panel, text= "Active Sensors")
        act_sensor_label.pack(side="top", fill="both", padx=5, pady=5)
        
        sensor_panelU = tki.Frame(sensor_panel, bg='#004000',width=90)
        sensor_panelU.pack(side="left", fill="both", padx=5, pady=5)
        
        sensor_panelR = tki.Frame(sensor_panel, bg='#004000', width=100)
        sensor_panelR.pack(side="left", fill="both", padx=5, pady=5)
        
        PH_label = tki.Button(sensor_panelU, text= "PH",  bg='#84A1B9')
        PH_label.pack(side="top", fill="both", padx=5, pady=5)
        
        Pressure_label = tki.Button(sensor_panelU, text= 'Pressure', bg='#84A1B9')
        Pressure_label.pack(side="top", fill="both", padx=5, pady=5)
        
        Temp_label = tki.Button(sensor_panelR, text= "Temp", bg='#84A1B9')
        Temp_label.pack(side="top", fill="both", padx=5, pady=5)
        
        Lumin_label = tki.Button(sensor_panelR, text="Lumin", bg='#84A1B9')
        Lumin_label.pack(side="top", fill="both", padx=5, pady=5)
#         
        # create a button, that when pressed, will take the current
        # frame and save it to file
        
        btn = tki.Button(lower_panel, text="Snapshot!", command=self.takeSnapshot)
        btn.pack(side="left", fill="none", padx=2, pady=2)
        
        # start a thread that constantly pools the video sensor for
        # the most recently read frame
        self.stopEvent = threading.Event()
        self.thread = threading.Thread(name='self_loop thread',target=self.videoLoop)
        self.thread.start()
        
        # set a callback to handle when the window is closed
        self.root.wm_title("PyImageSearch PhotoBooth")
        self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)
        
        self.root.mainloop()

    def videoLoop(self):
        logging.debug('starting')
        # DISCLAIMER:
        # I'm not a GUI developer, nor do I even pretend to be. This
        # try/except statement is a pretty ugly hack to get around
        # a RunTime error that Tkinter throws due to threading

        try:
            # keep looping over frames until we are instructed to stop
            while not self.stopEvent.is_set():
                # grab the frame from the video stream and resize it to
                # have a maximum width of 300 pixels
                
                self.frame = self.vs.read()
                
                self.frame = self.Zoom(self.frame)
                
              #  self.frame = imutils.resize(self.frame, width=self.imageSize)
                # OpenCV represents images in BGR order; however PIL
                # represents images in RGB order, so we need to swap
                # the channels, then convert to PIL and ImageTk format
                self.image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
              
                #set saturation and exposure values
               # self.image = self.setSaturationAndExposure(self.image)
                self.image = self.ImageExposureandBrightness(self.image)
              
                self.image = Image.fromarray(self.image)
                
                self.image = self.ImageSaturation(self.image)
                
                self.image = ImageTk.PhotoImage(self.image)
        
                # if the panel is not None, we need to initialize it
                if self.upper_panel is None:
                    self.upper_panel = tki.Label(image=self.image)
                    self.upper_panel.image = self.image
                    self.upper_panel.pack(side="top", padx=2, pady=2)
        
                # otherwise, simply update the panel
                else:
                    self.upper_panel.configure(image=self.image)
                    self.upper_panel.image = self.image
        except RuntimeError:
            print("[INFO] caught a RuntimeError")
    
    def multiply(self, num1, num2):
        return int(num2)*int(num1)
    
    def Zoom(self, cv2Object):
        # Resizes the image/video frame to the specified amount of "zoomSize".
        # A zoomSize of "2", for example, will double the canvas size
        #print('zoom value', self.multiply(self.zoomValue, cv2Object.shape[1]))
        zoomedWidth = self.multiply(self.zoomValue, cv2Object.shape[1])
        zoomedHeight = self.multiply(self.zoomValue, cv2Object.shape[0])
        
        if zoomedWidth < self.imageW:
            zoomedWidth = self.imageW
            zoomedHeight = self.imageH
            
        cv2Object = imutils.resize(cv2Object, width=zoomedWidth, height=zoomedHeight)
        if(self.zoomValue != 1):
          #  print('cv2objsize_in:', cv2Object.shape[0], " ", cv2Object.shape[1])
            # center is simply half of the height & width (y/2,x/2)
            center = (cv2Object.shape[0]/2,cv2Object.shape[1]/2)
            # cropScale represents the top left corner of the cropped frame (y/x)
            cropScale = (int(center[0]/2), int(center[1]/2))
            # The image/video frame is cropped to the center with a size of the original picture
            # image[y1:y2,x1:x2] is used to iterate and grab a portion of an image
            # (y1,x1) is the top left corner and (y2,x1) is the bottom right corner of new cropped frame.
            cv2Object = cv2Object[int(cropScale[0]):int((center[0] + cropScale[0])), int(cropScale[1]):int((center[1] + cropScale[1]))]
          #  cv2Object = imutils.resize(cv2Object, width=zoomedWidth, height=zoomedHeight)
           
            #its a pretty bad hack, but it aint working otherwise
            if(int(cv2Object.shape[1]) < int(self.imageW)):
                 cv2Object = imutils.resize(cv2Object, width=self.imageW, height=self.imageH)

        return cv2Object

    def setZoom(self, var):
        self.zoomValue = int(var)

    def setSaturation(self, var):
        self.saturationValue = float(var)

    def setExposure(self, var):
        self.exposureValue = float(var)
     
    def setBrightness(self, var):
        self.brightValue = float(var)
        
    def ImageSaturation(self, frame):
        converter = ImageEnhance.Color(frame)
        image = converter.enhance(self.saturationValue)
        return image
        
    def ImageExposureandBrightness(self,frame):
        image = cv2.addWeighted(frame, self.exposureValue, np.zeros(self.frame.shape, self.frame.dtype), 0, self.brightValue)
        
        return image

    def takeSnapshot(self):
            # grab the current timestamp and use it to construct the
            # output path
            ts = datetime.datetime.now()
            filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
            p = os.path.sep.join((self.outputPath, filename))
            # save the file
            cv2.imwrite(p, self.frame.copy())
            print("[INFO] saved {}".format(filename))       
    
    def onClose(self):
            # set the stop event, cleanup the camera, and allow the rest of
            # the quit process to continue
            print("[INFO] closing...")
            self.stopEvent.set()
            self.vs.stop()
            self.root.quit()

