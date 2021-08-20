# 
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog as fd

class Pdf_Tool (object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        self.file_path = ""
        self.options = ["Text", "Docx", "Picture", "Pdf"]

        self.selection_frame = LabelFrame(root, text,="PDF Convertion Tool", heignt=100, width=100)
        self.selection_frame_grid(column=0, row=0, padx=10, pady=10)

        self.file_label = Label(self, selection_frame, text="File: ")
        self.
        self.
        self.
        self.
        self.

        self.
        self.
        self.
        self.
        self.
        self.
        self.

        self.result_label = Label(self. selection_frame, text="")
        self.result_label.grid(column=0, row=2, columnspan=3)

if __name__ == '__main__':
    root = Tk()
    root.title("PDF Tool")
    Pdf_Tool(root)
    root.mainloop()
