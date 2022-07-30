import tkinter as tk
import turtle
from tkinter import ttk
from write_window import Write_window
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("apka")
        self.app_on = True
        self.time_left=15
        self.geometry("1000x500")
        self.app_frame = Write_window(self)
        self.app_frame.grid(row=0,column=0,sticky="NSEW")
        self.intro_label = tk.Label(self.app_frame,text=f"After {self.time_left} second text will disapear",
                                    font=("Arial",18))
        self.intro_label.grid(row=0,column=0,columnspan=1)
        self.text_space = tk.Text(self.app_frame,background="white",)
        self.text_space.grid(row=1,column=0)
        self.text_space.insert(tk.END,"Wjezdzam jak rekin")
        self.text_space.delete("1.0", "end-1c") #removes all text
        self.right_label = tk.Label(self, text=f"Time left:{self.time_left}",
                                    font=("Arial", 50))
        self.right_label.grid(row=0, column=1)
        self.time_count()

    def start_writing(self):
        self.time_left = 15

    def key_press(self,event): #restart timer if key is pressed
        key = event.char #listening for key
        print(f"'{key}' is pressed") #shows which key is pressed
        self.start_writing()


    def time_count(self):
        if self.time_left >0:
            self.right_label.config(text=f"{self.time_left}")
            self.time_left -= 1
            self.right_label.after(1000,self.time_count)
        else:
            self.right_label.config(text=f"Czas minal wariacie")
            self.text_space.delete("1.0", "end-1c")
            time.sleep(1)
            self.start_writing()
            self.time_count()






#initialization

app=App()
app.bind('<Key>',app.key_press)

#while app.app_on == True:

app.mainloop()