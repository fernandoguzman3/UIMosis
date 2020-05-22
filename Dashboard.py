# import the necessary packages
from __future__ import print_function
import RPi.GPIO as GPIO  
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
import tkinter as tki
import threading
import logging
import datetime
import time
import imutils
import cv2
import numpy as np
import os
import socket
import csv

class Dashboard:
    def __init__(self, outputPath, root, vs, s, captureClass=None, sensorClass=None, galleryClass=None):
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
        self.root = root
        #self.root.geometry("%dx%d+0+0" % (680, 600))
        self.upper_panel = None
        self.master_panel = None
        self.image = None
        self.imageW = 640
        self.imageH = 480
        self.imageSize = 800
        self.processedImage = None
        
        self.captureInfo = captureClass
        self.sensorInfo = sensorClass
        self.galleryInfo = galleryClass
        
        # ------------Defining LEDs-------------------------------
        self.LedUV = 14                      # LED set to pin #10
        self.LedNIR = 15
        self.LedWhite = 18
        self.LedConnect = 5
        self.LedLeak = 6
        self.LedBattery = 13
        self.LedSpace = 19
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)      # Configure pin layout to board's physical layout
        
        GPIO.setup(self.LedUV,GPIO.OUT)      # Set LED pin to output
        GPIO.setup(self.LedNIR ,GPIO.OUT)
        GPIO.setup(self.LedWhite,GPIO.OUT)
        GPIO.setup(self.LedConnect,GPIO.OUT)
        GPIO.setup(self.LedLeak,GPIO.OUT)
        GPIO.setup(self.LedBattery,GPIO.OUT)
        GPIO.setup(self.LedSpace,GPIO.OUT)
        
        self.activeLED = self.LedWhite

        
        #--------- UI elements variables
        self.zoom = False
        self.zoomValue = 1
        self.saturationValue = float(1)
        self.exposureValue = float(1)
        self.brightValue = float(0.2)
        self.sysMode = tki.StringVar()
        self.ledMode = tki.StringVar()
        self.snapShotProgress = tki.StringVar()
        
        self.mode = None
        
        self.setLed = tki.IntVar()
                
        #-------- Sensor variables
        self.PH = tki.StringVar()
        self.Pressure = tki.StringVar()
        self.Lumin = tki.StringVar()
        self.Temp = tki.StringVar()
        self.activeSensorList = None
        
        #-------- Connection variables
        self.host = '169.254.153.172'
        self.port = 2304
        self.s = s
        
    def initializeDashboard(self):
        
        self.master_panel = tki.Frame(self.root, bg='#46637B',height=600, width=800)
        self.master_panel.pack(fill="both")
        
        #---------------- LOWER PANEL----------------------------------#
        
         #lower panel to house the picture scales, led, mode and sensor info
        lower_panel = tki.Frame(self.master_panel, bg='#46637B')
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
        modeConfig_panelU.pack(side="top", fill="x",padx=5, pady=5)
        
        modeConfig_panelL = tki.Frame(modeConfig_panel, bg='#004000',width=25, height=50)
        modeConfig_panelL.pack(side="top", fill="x", padx=5, pady=5)
        
         # create a button, that when pressed, will take the current
        # frame and save it to file
        btn = tki.Button(modeConfig_panel, text="Snapshot!", command=self.checkMode)
        btn.pack(side="bottom", fill="none", padx=2, pady=2)
        
        mode1_label = tki.Label(modeConfig_panel, text= "", textvariable=self.snapShotProgress, bg='#46637B', fg='white', width= 5,font=("Courier", 9))
        mode1_label.pack(side = "bottom",fill="x", padx=2, pady=2)
        
        mode_label = tki.Label(modeConfig_panelU, text= "Mode: ", width= 10)
        mode_label.pack(side = "left",fill="both", padx=2, pady=2)
        
        mode_var_label = tki.Label(modeConfig_panelU, textvariable = self.sysMode, bg='#46637B', fg='white', width = 10)
        mode_var_label.pack(side = "left", fill="both", padx=2, pady=2)
        
        selected_LED = tki.Label(modeConfig_panelL, text="LED: ", bg="#84A1B9", width = 10,font=("Courier", 7))
        selected_LED.pack(side = "left", fill="both", padx=2, pady=2)
        
        R1 = tki.Radiobutton(modeConfig_panelL, text="UV" , bg='#46637B',selectcolor='red', variable=self.setLed, value=int(1),
                             fg='white', font=("Courier", 8), command=self.changeLED)
        R1.pack(side="left",fill="both", padx=5, pady=10)
        
        R2 = tki.Radiobutton(modeConfig_panelL, text="NIR" , bg='#46637B',selectcolor='red', variable=self.setLed, value=int(2),
                             fg='white', font=("Courier", 8), command=self.changeLED)
        R2.pack(side="left",fill="both", padx=5, pady=10)
        
        R3 = tki.Radiobutton(modeConfig_panelL, text="FS_White" , bg='#46637B',selectcolor='red', variable=self.setLed, value=int(3),
                             fg='white', font=("Courier", 8), command=self.changeLED)
        R3.pack(side="left",fill="both", padx=5, pady=10)
        
        GPIO.output(self.LedWhite, GPIO.LOW)
        GPIO.output(self.LedUV, GPIO.LOW)
        GPIO.output(self.LedNIR, GPIO.LOW)
        R3.invoke()
        
        GPIO.output(self.LedConnect, GPIO.LOW)
        GPIO.output(self.LedLeak, GPIO.HIGH)
        GPIO.output(self.LedBattery, GPIO.HIGH)
        GPIO.output(self.LedSpace, GPIO.HIGH)
        
        
#         LED_mode_label = tki.Label(modeConfig_panelU, text= "LED mode: ")
#         LED_mode_label.pack(side = "left",fill="both", padx=2, pady=2)
#         
#         LED_var_label = tki.Label(modeConfig_panelL, textvariable = self.ledMode, bg="#84A1B9", width = 10)
#         LED_var_label.pack(side = "left",fill="both", padx=2, pady=2)
        
        #---------------- Sensor PANEL----------------------------------#
        
        #panel for the activated sensors
        sensor_panel = tki.Frame(lower_panel, bg='#004000', width=50, height=100)
        sensor_panel.pack(side="left", fill="both", padx=2, pady=2)
        
        act_sensor_label = tki.Label(sensor_panel, text= "Active Sensors", font=("Courier", 10))
        act_sensor_label.pack(side="top", fill="both", padx=5, pady=5)
        
        sensor_panelU = tki.Frame(sensor_panel, bg='#004000', width=25)
        sensor_panelU.pack(side="left", fill="both", padx=5, pady=5)
        
        sensor_panelR = tki.Frame(sensor_panel, bg='#004000',width=25)
        sensor_panelR.pack(side="left", fill="both", padx=5, pady=5)
        
        PH_label = tki.Label(sensor_panelU, text= "PH",  bg='#84A1B9')
        PH_label.pack(side="top", fill="both", padx=5, pady=5)
        
        PH_labelvar = tki.Label(sensor_panelU, textvariable=self.PH, text= "", bg='white',width = 5, font=("Courier", 9) )
        PH_labelvar.pack(side="top", fill="both", padx=5, pady=5)
        
        Pressure_label = tki.Label(sensor_panelU, text= 'Pressure', bg='#84A1B9')
        Pressure_label.pack(side="top", fill="both", padx=5, pady=5)
        
        Pressure_labelvar = tki.Label(sensor_panelU, textvariable=self.Pressure, text= "", bg='white',width = 5,font=("Courier", 9) )
        Pressure_labelvar.pack(side="top", fill="both", padx=5, pady=5)
        
        Temp_label = tki.Label(sensor_panelR, text= "Temp", bg='#84A1B9')
        Temp_label.pack(side="top", fill="both", padx=5, pady=5)
        
        Temp_labelvar = tki.Label(sensor_panelR, textvariable=self.Temp, text= "", bg='white',width = 5, font=("Courier", 9))
        Temp_labelvar.pack(side="top", fill="both", padx=5, pady=5)
        
        Lumin_label = tki.Label(sensor_panelR, text="Lumin", bg='#84A1B9')
        Lumin_label.pack(side="top", fill="both", padx=5, pady=5)
        
        Lumin_labelvar = tki.Label(sensor_panelR, textvariable=self.Lumin, text= "", bg='white',width = 5,font=("Courier", 9))
        Lumin_labelvar.pack(side="top", fill="both", padx=5, pady=5)
        
        # start a thread that constantly pools the video sensor for
        # the most recently read frame
        self.stopEvent = threading.Event()
        self.thread = threading.Thread(name='self_loop thread',target=self.videoLoop)
        self.thread.start()
        
        # set a callback to handle when the window is closed
       # self.root.wm_title("PyImageSearch PhotoBooth")
       # self.root.rotocol("WM_DELETE_WINDOW", self.onClose)
        
        return self.master_panel
        
       # self.root.mainloop()

    def videoLoop(self):
        self.vs.start()
        
     #   self.establishCommunication() #establish communication
        
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
                
                self.sysMode.set(self.getsystemMode())
                
                self.updateSensorLabels()
                
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
                
                self.processedImage = self.image
                
                self.image = ImageTk.PhotoImage(self.image)
        
                # if the panel is not None, we need to initialize it
                if self.upper_panel is None:
                    self.upper_panel = tki.Label(self.master_panel,image=self.image)
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
    
    def checkMode(self):
        pics = None
        self.snapShotProgress.set("taking pic...")
        print(self.snapShotProgress.get())
        time.sleep(0.5)
        if(self.mode == 1):
            self.takeSnapshot(self.outputPath)
            self.snapShotProgress.set("done!")
        elif(self.mode == 2):
          #  t1 = threading.Thread(name='t2',target=self.takeBurstSnapshot, args=(self.captureInfo.getBurstModeValues()))
          #  t1.start()
          #  t1.join()
            self.takeBurstSnapshot(self.captureInfo.getBurstModeValues())
          #  logging.debug('joined burst mode thread')
            self.snapShotProgress.set("done!")
                
        elif(self.mode == 3):
            t1 = threading.Thread(name='t2',target=self.takeTimeIntervalSnapshot,
                                  args=(self.captureInfo.getStepsValues(), self.captureInfo.getIntervalValues()))
            logging.debug('start Tinterval mode thread')
            t1.start()
            t1.join()
            logging.debug('joined Tinterval mode thread')
            self.snapShotProgress.set("done!")
    
    def takeBurstSnapshot(self,pics):
        logging.debug('start burst mode thread')
        ts = datetime.datetime.now()
        logging.debug('1')
        picsRage = int(pics)
#         pics = int(self.captureInfo.getBurstModeValues())
        logging.debug('2')
   #     foldername = "{}".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
        outputPath = "Media/Images"
      #  logging.debug('3')
     #   p = os.path.sep.join((outputPath, foldername))
        logging.debug('4')
     #   os.makedirs(p)
        logging.debug('into forloop')
        for pic in range(picsRage):
            self.takeSnapshot(outputPath)
            time.sleep(0.5)
       # self.snapShotProgress.set("done!")
        logging.debug('done')
        return

    def takeTimeIntervalSnapshot(self,stepsVal,intervalVal):
        logging.debug('start burst mode thread')
       # steps = int(self.captureInfo.getStepsValues())
       # interval = int(self.captureInfo.getIntervalValues())
        steps = int(stepsVal)
        interval = int(intervalVal)
        
        ts = datetime.datetime.now()
        foldername = "{}".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
        outputPath = "Media/Images"
        p = os.path.sep.join((outputPath, foldername))
        os.makedirs(p)
        
        timeLimit = datetime.timedelta(minutes=interval)
     #   print("timeLimit", timeLimit)
        stepsLimit = datetime.timedelta(seconds= steps)
      #  print("stepsLimit", stepsLimit)
        startTimeInt = datetime.datetime.now()
        startTimeSteps = None
        
        while((datetime.datetime.now()-startTimeInt) < timeLimit):
           startTimeSteps = datetime.datetime.now()
          # print("now", datetime.datetime.now(), " startTimeInt:",startTimeInt)
          # print("difference:", (datetime.datetime.now()-startTimeInt))
           logging.debug("outer")
           logging.debug(datetime.datetime.now()-startTimeSteps)
           # stop if the time limit is reached :
           while True:
               if((datetime.datetime.now()-startTimeSteps) > stepsLimit):
#                    print("now2", datetime.datetime.now(), " startTimeSteps:",startTimeSteps)
#                    print("difference2", (datetime.datetime.now()-startTimeSteps))
                   logging.debug("inner")
                   logging.debug(datetime.datetime.now()-startTimeSteps)
                   self.takeSnapshot(p)
                   break
        logging.debug('done')
        return
        
    def takeSnapshot(self,outputPath):
            # grab the current timestamp and use it to construct the
            # output path
            if(self.processedImage is None):
                return
            ts = datetime.datetime.now()
            filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S-%f"))
            p = os.path.sep.join((outputPath, filename))
            image = self.processedImage.convert('RGB')
            # save the file
            image.save(p)
            #cv2.imwrite(p, image)
            print("[INFO] saved {}".format(filename))
            self.galleryInfo.getListOfFiles()
    
    def onClose(self):
            # set the stop event, cleanup the camera, and allow the rest of
            # the quit process to continue
            print("[INFO] closing...")
            self.stopEvent.set()
            self.vs.stop()
            self.root.quit()
    
    def changeLED(self):
        previousLed = self.activeLED
        if(self.setLed.get() == 1):
            self.activeLED = self.LedWhite
        elif(self.setLed.get() == 2):
            self.activeLED = self.LedUV
        elif(self.setLed.get() == 3):
            self.activeLED = self.LedNIR
        
        GPIO.output(previousLed, GPIO.LOW)
        GPIO.output(self.activeLED, GPIO.HIGH)
            
    
    def getsystemMode(self):
        self.mode = self.captureInfo.getCaptureModeValues()
        if(self.mode == int(1)):
            return "single"
        elif(self.mode == int(2)):
            return "burst"
        elif(self.mode == int(3)):
            return "Time Lapse"
        elif(self.mode == int(4)):
            return "Image Stack"
        
#     def establishCommunication(self):
#         self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.s.connect((self.host, self.port))
    
    def getActiveSensors(self):
        self.activeSensorList = self.sensorInfo.getActiveSensors()
    
    def updateSensorLabels(self):
        activeSensorList = self.sensorInfo.getActiveSensors()
        sensorString = ""
        for sensor in activeSensorList:
            if(activeSensorList[sensor] != 0):
                sensorString += " " + sensor
        command = "GET"+sensorString
     #   print(command)
        self.s.send(str.encode(command))
        reply = self.s.recv(1024)
        reply = reply.decode('utf-8')
        splitReply = [x.strip() for x in reply.split(',')]
        self.Temp.set(splitReply[0])
        self.PH.set(splitReply[1])
        self.Lumin.set(splitReply[2])
        self.Pressure.set(splitReply[3])
        
        
        
        
        

