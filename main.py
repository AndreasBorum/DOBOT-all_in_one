import tkinter as tk
from tkinter import ttk

import dobot_studio as ds
import realterm as rt
import mplab as mp


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('DOBOT instruction calculeter')
        self.geometry('700x500')

        notebook = ttk.Notebook(self, width=700, height=450)
        notebook.pack(pady=10, expand=True)

        self.DS_frame = ds.DobotStudio(self)
        self.RT_frame = rt.RealTerm(self)
        self.MP_frame = mp.MPLap(self)

        self.DS_frame.pack(fill='both', expand=True)
        self.RT_frame.pack(fill='both', expand=True)

        notebook.add(self.DS_frame, text='DobotStudio')
        notebook.add(self.RT_frame, text='RealTerm')
        notebook.bind('<<NotebookTabChanged>>', self.on_tab_change)

    def on_tab_change(self, event):
        tab = event.widget.tab('current')['text']
        if tab == 'DobotStudio':
            pass
        elif tab == 'RealTerm':
            self.RT_frame.update_lables()


if __name__ == '__main__':
    app = App()
    app.mainloop()
