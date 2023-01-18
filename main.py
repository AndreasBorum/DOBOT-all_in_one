import tkinter as tk 
from tkinter import ttk

import dobot_studio as ds
import realterm as rt


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('DOBOT instruction calculeter')
        self.geometry('700x500')

        notebook = ttk.Notebook(self, width=700, height=450)
        notebook.pack(pady=10, expand=True)

        DS_frame = ds.DobotStudio(self)
        RT_frame = rt.RealTerm(self)


        DS_frame.pack(fill='both', expand=True)


        notebook.add(DS_frame, text='DobotStudio')




if __name__ == '__main__':
    app = App()
    app.mainloop()