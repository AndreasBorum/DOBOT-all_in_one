import tkinter as tk
from tksheet import Sheet

class MPLap(tk.Frame):
    def __init__(self, container):
        super().__init__(container, width=600)

        self.root_app = container

        self.sheet_frame = Sheet(self, width=600)
        self.sheet_frame.enable_bindings()
        self.sheet_frame.pack()


    def update_lables(self):
        data = self.root_app.RT_frame.sheet_frame.get_sheet_data()
        mplab_data = []
        for row in data:
            instrunction = row[1:]
            print(instrunction)
            mplab_data.append([row[0], instrunction])
            
        self.sheet_frame.set_sheet_data(data = mplab_data, redraw= False)
        self.sheet_frame.set_all_cell_sizes_to_text(redraw = True)
