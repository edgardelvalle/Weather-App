from tkinter import *
from query import query
import os
from dotenv import load_dotenv

class gui:

    def __init__(self):  
        self.query = query() 
        self.query.print_info()

        self.master = Tk()
        self.master.geometry('700x425')
        self.master.title("Check the weather")


        self.frame_1 = Frame(self.master)
        #self.frame_2 = Frame(self.master)
        #self.frame_3 = Frame(self.master)
        #self.frame_4 = Frame(self.master)
        #self.frame_5 = Frame(self.master)
        #self.frame_6 = Frame(self.master)

        # Labels here
        self.zip_code_label = Label(self.frame_1, text="Input Zip-Code: ")
        self.zip_code_entry = Entry(self.frame_1) 
        self.zip_code_label.grid(row=0, column=0)
        self.zip_code_entry.grid(row=0, column=1)

        self.frame_1.grid(row=0)
        #self.frame_2.grid(row=1, column=0)
        #self.frame_3.grid(row=2)
        #self.frame_4.grid(row=3)
        #self.frame_5.grid(row=4)
        #self.frame_6.grid(row=5)

        #self.master.mainloop()
    
    def run_master(self):
        self.master.mainloop()


    def create_frame(self):
        self.top_frame = Frame(self.master, height=50, width=500, bg='blue').pack()
        
 
 

'''
if __name__ == '__main__':
  tk_root = Tk()
  my_gui = my_first_GUI(tk_root)
  tk_root.mainloop()
'''