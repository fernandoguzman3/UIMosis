from tkinter import *

WIDTH = 600
HEIGHT = 380

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Setup Menu
        MainMenu(self)
        self.geometry('{}x{}'.format(WIDTH, HEIGHT))
        # Setup Frame

        container = Frame(self).grid(row=0, column=1)
        # container.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.frames = {}
        print(self.grid_size())
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=1)

        self.show_frame(StartPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Start Page").grid(row=0, column=0)
        #label.pack(padx=10, pady=10)
        page_one = Button(self, text="Page One", command=lambda: controller.show_frame(PageOne)).grid(row=1, column=0)
        #page_one.pack()
        page_two = Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo)).grid(row=2, column=0)
        #page_two.pack()


class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Page One").grid(row=0, column=0)
        #label.pack(padx=10, pady=10)
        start_page = Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage)).grid(row=1, column=0)
        #start_page.pack()
        page_two = Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo)).grid(row=2, column=0)
        #page_two.pack()


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Page Two").grid(row=0, column=0)
        #label.pack(padx=10, pady=10)
        start_page = Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage)).grid(row=1, column=0)
        #start_page.pack()
        page_one = Button(self, text="Page One", command=lambda: controller.show_frame(PageOne)).grid(row=2, column=0)
        #page_one.pack()


class MainMenu:
    def __init__(self, master):
        b1 = Button(master, text="B1", padx=10).grid(row=0, column=0, sticky="w", padx=10)
        b2 = Button(master, text="B2", padx=10).grid(row=1, column=0, sticky="w", padx=10)
        b3 = Button(master, text="B3", padx=10).grid(row=2, column=0, sticky="w", padx=10)
        b4 = Button(master, text="B4", padx=10).grid(row=3, column=0, sticky="w", padx=10)
        b5 = Button(master, text="B5", padx=10).grid(row=0, column=2, sticky="e", padx=10)
        b6 = Button(master, text="B6", padx=10).grid(row=1, column=2, sticky="e", padx=10)
        b7 = Button(master, text="B7", padx=10).grid(row=2, column=2, sticky="e", padx=10)
        b8 = Button(master, text="B8", padx=10).grid(row=3, column=2, sticky="e", padx=10)


app = App()
app.mainloop()
