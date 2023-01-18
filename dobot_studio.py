import tkinter as tk
from tksheet import Sheet
from tkinter import filedialog as fd
from tkinter.constants import *

from file_import import import_playback


class DobotStudio(tk.Frame):
    def __init__(self, container):
        super().__init__(container, width=600)

        import_btn = tk.Button(self, text="Import file",
                               command=self.import_file). grid()

        self.table_frame = SheetFrame(self)
        self.table_frame.grid()

    def import_file(self):
        filetypes = (
            ('DOBOT studio files', '*.playback'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            filetypes=filetypes)

        data = import_playback(filename)

        self.table_frame.insert_data(data)


class SheetFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container, width=600)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame = tk.Frame(self, width=600)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)


    def show(self):
        self.frame.grid(row=0, column=0, sticky="nswe")
        self.sheet.grid(row=0, column=0, sticky="nswe")


    def insert_data(self, data):

        data_no_type=[]
        type_data=[]
        for row in data:
            data_no_type.append([row[1], None, round_int(row[2]), round_int(row[3]),round_int(row[4]),round_int(row[5])])
            type_data.append(row[0])

        self.sheet = Sheet(self.frame, data=data_no_type, width=600)
        self.sheet.enable_bindings()

        self.sheet.headers(newheaders = ["Name", "Type", "x", "y", "z", "r"], index = None, reset_col_positions = False, show_headers_if_not_sheet = True, redraw = False)


        for i, cell in enumerate(type_data):
            self.sheet.create_dropdown(r=i,
                            c=1,
                            values=types,
                            set_value=types[int(cell)],
                            state="readonly",
                            redraw=False,
                            selection_function=None,
                            modified_function=None)

        self.sheet.column_width(column =0, width = 150, only_set_if_too_small = False, redraw = True)
        self.sheet.column_width(column =1, width = 70, only_set_if_too_small = False, redraw = True)
        self.sheet.column_width(column =2, width = 50, only_set_if_too_small = False, redraw = True)
        self.sheet.column_width(column =3, width = 50, only_set_if_too_small = False, redraw = True)
        self.sheet.column_width(column =4, width = 50, only_set_if_too_small = False, redraw = True)
        self.sheet.column_width(column =5, width = 50, only_set_if_too_small = False, redraw = True)

        self.show()

        
types = ["MOVL", "MOVJ", "ERC"]
        
def round_int(decimal_string):
    return int(round(float(decimal_string)))