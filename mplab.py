import tkinter as tk
from tksheet import Sheet
import convert_to_mplab


class MPLap(tk.Frame):
    def __init__(self, container):
        super().__init__(container, width=600)

        self.root_app = container

        self.sheet_frame = Sheet(self, width=600)
        self.sheet_frame.enable_bindings()
        self.sheet_frame.pack()

        tk.Button(self, text="All lookuptables", command=self.lookup_to_clipboard).pack()


    def update_lables(self):
        data = self.root_app.RT_frame.sheet_frame.get_sheet_data()
        self.mplab_data = []
        for i, row in enumerate(data):
            instrunction = convert_to_mplab.convert(row[1:])
            #print(instrunction)
            lookuptable = convert_to_mplab.make_lookuptable(instrunction, i)
            self.mplab_data.append([row[0], instrunction, lookuptable])
            
        self.sheet_frame.set_sheet_data(data = self.mplab_data, redraw= False)
        self.sheet_frame.set_all_cell_sizes_to_text(redraw = True)

    def lookup_to_clipboard(self):
        self.root_app.clipboard_clear()
        self.root_app.clipboard_append(convert_to_mplab.make_all_make_lookuptables(self.mplab_data))