# import the necessary packages
from __future__ import print_function
from PIL import Image
from PIL import ImageTk
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
        self.root.geometry("%dx%d+0+0" % (600, 600))
        self.upper_panel = None
        self.image = None
        self.imageW = 800
        self.imageH = 500
        self.imageSize = 800
        
        lower_panel = tki.Frame(self.root, width=200, height= 400, bg='grey')
        lower_panel.pack(side="bottom", fill="none", padx=10, pady=10)
        
        zoomScale = tki.Scale(lower_panel, from_=1, to=10, orient=tki.HORIZONTAL, label = "Zoom", command = self.setZoom)
        zoomScale.pack(side="left", fill="none", padx=10, pady=10)
        
        self.zoom = False
        self.zoomValue = 1
        
        # create a button, that when pressed, will take the current
        # frame and save it to file
        
        btn = tki.Button(lower_panel, text="Snapshot!", command=self.takeSnapshot)
        btn.pack(side="left", fill="none", padx=10, pady=10)
        
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
                
                #print(self.zoomValue)
              #  if self.zoomValue == int(1):
              #      self.frame = imutils.resize(self.frame, width=self.imageW, height=self.imageH)
                  #  print('original preview')
                
              #  else:
                self.frame = self.Zoom(self.frame)
                   #  print('zoomed preview')
                
                self.image = cv2.cvtColor(self.frame,cv2.COLOR_BGR2HSV)

                #multiple by a factor to change the saturation
                self.image[...,1] = self.image[...,1]*2.5

                #multiple by a factor of less than 1 to reduce the brightness 
                self.image[...,2] = self.image[...,2]*1

                self.image=cv2.cvtColor(self.image,cv2.COLOR_HSV2RGB)
                
              #  self.frame = imutils.resize(self.frame, width=self.imageSize)
                # OpenCV represents images in BGR order; however PIL
                # represents images in RGB order, so we need to swap
                # the channels, then convert to PIL and ImageTk format
               # self.image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
               # self.image = cv2.addWeighted(self.frame, 1, np.zeros(self.frame.shape, self.frame.dtype), 0, 10)
                self.image = Image.fromarray(self.image)
                self.image = ImageTk.PhotoImage(self.image)
        
                # if the panel is not None, we need to initialize it
                if self.upper_panel is None:
                    self.upper_panel = tki.Label(image=self.image )
                    self.upper_panel.image = self.image
                    self.upper_panel.pack(side="top", padx=10, pady=10)
        
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
            # center is simply half of the height & width (y/2,x/2)
            center = (cv2Object.shape[0]/2,cv2Object.shape[1]/2)
            # cropScale represents the top left corner of the cropped frame (y/x)
            cropScale = (int(center[0]/2), int(center[1]/2))
            # The image/video frame is cropped to the center with a size of the original picture
            # image[y1:y2,x1:x2] is used to iterate and grab a portion of an image
            # (y1,x1) is the top left corner and (y2,x1) is the bottom right corner of new cropped frame.
            cv2Object = cv2Object[int(cropScale[0]):int((center[0] + cropScale[0])), int(cropScale[1]):int((center[1] + cropScale[1]))]
        
       # cv2Object = imutils.resize(cv2Object, width=zoomedWidth, height=zoomedHeight)
        return cv2Object

    def setZoom(self, var):
        self.zoomValue = int(var)
        #print("zoom Value: ", self.zoomValue)

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
