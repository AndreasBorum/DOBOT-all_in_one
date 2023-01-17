import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.constants import *

from file_import import import_playback

class DobotStudio(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        import_btn = tk.Button(self, text="Import file", command= self.import_file). grid()



        self.table_frame = ScrollableFrame(self)
        self.rows_frame = tk.Frame(self.table_frame.interior)
        self.rows_frame.pack(expand=True)
        self.table_frame.grid()

        self.rows = [Row(self) for _ in range(10)]
        for row in self.rows:
            row.pack()

    def add_row(self, pos, row_data = None):
        for row in self.rows[pos:]:
            row.forget()
        self.rows.insert(pos, Row(self, row_data))
        for row in self.rows[pos:]:
            row.pack()
    
    def delete_row(self, pos):
        self.rows[pos].forget()
        self.rows.pop(pos)


    def import_file(self):
        filetypes = (
            ('DOBOT studio files', '*.playback'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            filetypes=filetypes)

        data = import_playback(filename)

        for i, row_data in enumerate(data):
            self.add_row(i, row_data)

        print(data)



class Row(tk.Frame):
    def __init__(self, container, data= None):
        super().__init__(container.rows_frame)

        self.container = container

        options = [
            "MOVj",
            "MOVL",
            "JUMP",
            "ARC ",]

        # datatype of menu text
        clicked = tk.StringVar()
        
        # initial menu text
        clicked.set( options[0] )

        self.name = tk.Entry(self)
        self.type = tk.OptionMenu(self,clicked, *options)
        self.y = tk.Entry(self, width= 10)
        self.x = tk.Entry(self, width= 10)
        self.z = tk.Entry(self, width= 10)
        self.r = tk.Entry(self, width= 10)

        self.add = tk.Button(self, width=5, text="Add", command= self.add)
        self.delete = tk.Button(self, width=5, text="Del", command= self.delete)


        self.name.grid(row=0, column=0)
        self.type.grid(row=0, column=1)
        self.x.grid(row=0, column=2)
        self.y.grid(row=0, column=3)
        self.z.grid(row=0, column=4)
        self.r.grid(row=0, column=5)
        self.add.grid(row=0, column=6)
        self.delete.grid(row=0, column=7)

        if data != None:
            self.insert_data(data)

    def insert_data(self, data):
        self.name.insert(0,data[0])
        #self.type.set
        self.x.insert(0,data[2])
        self.y.insert(0,data[3])
        self.z.insert(0,data[4])
        self.r.insert(0,data[5])
    
    def add(self):
        i = self.container.rows.index(self)
        self.container.add_row(i+1)

    def delete(self):
        i = self.container.rows.index(self)
        self.container.delete_row(i)






class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = ttk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)