# 
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog as fd

class Pdf_Tool(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        self.file_path = ""
        self.options = ["Text", "Docx", "Picture", "Pdf"]