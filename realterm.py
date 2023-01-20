import tkinter as tk
from instructions import real_time_inst


class RealTerm(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.root_app = container

        self.list_frame = tk.Frame(self).pack()



    def update_lables(self):
        for row in self.root_app.DS_frame.table_frame.sheet.get_sheet_data():
            name_lable = tk.Label(self.list_frame, text=f"{row[0]}:").pack()
            instrunction = real_time_inst(row[1:])
            print(instrunction)
            instrunction_lable = tk.Label(self.list_frame, text= instrunction).pack()