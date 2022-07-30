import tkinter as tk
from tkinter import ttk
import time


class Write_window(tk.Canvas):
    def __init__(self, container):
        super().__init__(container)

        self.write_frame = ttk.Frame(self)
