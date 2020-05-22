import tkinter as tk

class Col1Buttons:
    def __init__(self, root, panel_list):
        self.root = root
        self.b_width = 5
        self.b_height = 2
        self.x_pad = 5
        self.y_pad = 50
        self.panel_traversal_list = panel_list
        self.activePanel = None
        self.panelIndex = 0
        self.panelListLength = len(panel_list)
        
    def initializeButtonColumn1(self):
         # Buttons on the Second Column
        col2_frame = tk.Frame(self.root, bg='#84A1B9')
        col2_frame.pack(side="left", fill="y")

        b5 = tk.Button(col2_frame, text="UP", width=self.b_width, height=self.b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=self.up_com)
        b5.pack(side="top", fill="both", padx=self.x_pad, pady=self.y_pad)

        b6 = tk.Button(col2_frame, text="DOWN", width=self.b_width, height=self.b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=self.down_com)
        b6.pack(side="top", fill="both", padx=self.x_pad, pady=self.y_pad)

        b7 = tk.Button(col2_frame, text="LEFT", width=self.b_width, height=self.b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=self.left_com)
        b7.pack(side="top", fill="both", padx=self.x_pad, pady=self.y_pad)

        b8 = tk.Button(col2_frame, text="RIGHT", width=self.b_width, height=self.b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=self.right_com)
        b8.pack(side="top", fill="both", padx=self.x_pad, pady=self.y_pad)
        
        self.panelIndex = 0
        self.activePanel = self.panel_traversal_list[self.panelIndex]
        #self.updateCurrentPanel(0)
    
    def updateCurrentPanel(self, panel):
        self.panel_traversal_list[panel].lift()
        self.activePanel = self.panel_traversal_list[panel]
       # self.activePanel = panel
    
    def up_com(self):
        
        print("UP")

    def down_com(self):
        
        print("DOWN")

    def left_com(self):
        self.panelIndex = self.panelIndex-1
        if(self.panelIndex < 0):
            self.panelIndex = self.panelListLength-1
        print(self.panelIndex)
        self.updateCurrentPanel(self.panelIndex)
        
#         if self.col2_buttons.get_menu_state() and self.menu_index != 0:
#             self.menu_index -= 1
#             self.panel_list[self.menu_index].lift()
# 
#         print("LEFT Menu_index: " + str(self.menu_index))

    def right_com(self):
        self.panelIndex = self.panelIndex+1
        
        if(self.panelIndex > self.panelListLength-1):
            self.panelIndex = 0
        print(self.panelIndex)
        self.updateCurrentPanel(self.panelIndex)
        
        
#         if self.col2_buttons.get_menu_state() and self.menu_index != len(self.panel_list) - 1:
#             self.menu_index += 1
#             self.panel_list[self.menu_index].lift()
      #  print("RIGHT Menu_index: " + str(self.menu_index))
            
class Col2Buttons:
    def __init__(self, root, menu_panel, dashboard):
        self.root = root
        self.b_width = 5
        self.b_height = 2
        self.x_pad = 5
        self.y_pad = 50
        self.dashboard = dashboard
        self.menu_panel = menu_panel

    def initializeButtonColumn2(self):
          # Buttons on the Second Column
        col2_frame = tk.Frame(self.root, bg='#84A1B9')
        col2_frame.pack(side="right", fill="y")
        
        b5 = tk.Button(col2_frame, text="YES", width=self.b_width, height=self.b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=self.yes_com)
        b5.pack(side="top", fill="both", padx=self.x_pad, pady=self.y_pad)

        b6 = tk.Button(col2_frame, text="NO", width=self.b_width, height=self.b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=self.no_com)
        b6.pack(side="top", fill="both", padx=self.x_pad, pady=self.y_pad)

        b7 = tk.Button(col2_frame, text="MENU", width=self.b_width, height=self.b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=self.menu_com)
        b7.pack(side="top", fill="both", padx=self.x_pad, pady=self.y_pad)

        b8 = tk.Button(col2_frame, text="SNAP", width=self.b_width, height=self.b_height, bg='#46637B', fg='white',
                    font=("Courier", 10), command=self.capture_com)
        b8.pack(side="top", fill="both", padx=self.x_pad, pady=self.y_pad)
    
    def yes_com(self):
        print("YES")
    def no_com(self):
        print("NO")
    def menu_com(self):
        self.menu_panel.lift()
#         self.menu_state = not self.menu_state
#         if self.menu_state:
#             b7.configure(bg="white", fg='#46637B')
#         else:
#             b7.configure(bg='#46637B', fg="white")
#         print("Menu_state " + str(self.menu_state))
    def capture_com(self):
        self.dashboard.takeSnapshot()
        print("SNAP")
        
