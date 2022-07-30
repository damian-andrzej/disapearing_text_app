import tkinter as tk
from tkinter import ttk
import time

class Right_label(tk.Canvas):
    def __init__(self, container):
        super().__init__(container)
        self.time_left2 = 10

        self.right_label = ttk.Frame(self)
        self.right_label2 = tk.Label(self, text=f"Time left:{self.time_left2}", background="blue",
                                    font=("Arial", 50))
        self.right_label2.grid(row=0, column=1)


    def change_label(self):
        self.right_label['text'] = self.time_left2

    def time_count(self):
        for i in range(10):
            self.after(1000)
            self.time_left2 -= 1
            print(self.time_left2)
            if self.time_left2 == 0:
                print("koniec czasu")