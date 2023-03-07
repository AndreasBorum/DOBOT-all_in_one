import tkinter as tk
from tksheet import Sheet
from instructions import real_time_inst


class RealTerm(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.root_app = container

        self.sheet_frame = Sheet(self)
        self.sheet_frame.pack()



    def update_lables(self):
        data = self.root_app.DS_frame.table_frame.sheet.get_sheet_data()
        realterm_daata = []
        for i, row in enumerate(data):
            instrunction = real_time_inst(row[1:])
            print(instrunction)
            realterm_daata.append([row[0], instrunction])
            
        self.sheet_frame.set_sheet_data(data = realterm_daata, redraw= False)
        self.sheet_frame.set_all_cell_sizes_to_text(redraw = True)
