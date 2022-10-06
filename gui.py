from tkinter import *
from query import query
import re

class gui:

    def __init__(self):  
        self.query = query() 
        self.master = Tk() 
        self.zip_code_pattern = re.compile('^[0-9]{5}$')
        # Create error label

        self.query.test_query()

        #self.query.print_info()
        self.master.geometry('700x425')
        self.master.title("Check the weather")
        self.master.columnconfigure(0, weight=1)
        self.master.configure(bg='white')
        #self.zip_code

        self.frame_1 = Frame(self.master)
        self.frame_2 = Frame(self.master)
        #self.frame_3 = Frame(self.master)
        #self.frame_4 = Frame(self.master)
        #self.frame_5 = Frame(self.master)
        #self.frame_6 = Frame(self.master)

        # Labels here
        self.zip_code_label = Label(self.frame_1, text="Input Zip-Code: ", width=15, height=2)
        self.zip_code_entry = Entry(self.frame_1, width=10, bd=2)  
        self.zip_code_label.grid(row=0, column=0, ipadx=15)
        self.zip_code_entry.grid(row=0, column=1, padx=5)

        # 
        self.location_label = Label(self.frame_2, text='San Marcos', bg='red')
        self.location_label.grid(row=0, column=3, sticky=E)

        #button
        self.submit_zip = Button(self.frame_1, text='Submit', command=self.submit, width=15, bd=8, relief='sunken')
        #self.submit_zip.config(highlightthickness=0) 
        self.submit_zip.grid(row=0, column=3, padx=15)

        self.frame_1.grid(row=0, sticky='ew')
        self.frame_2.grid(row=1, column=0)
        #self.frame_3.grid(row=2)
        #self.frame_4.grid(row=3)
        #self.frame_5.grid(row=4)
        #self.frame_6.grid(row=5)

        #self.master.mainloop()
    
    def submit(self):
        test_zip = self.zip_code_entry.get()
        result = re.match(self.zip_code_pattern, test_zip)

        #better way to test this?
        if result:
            print("Works")
            print(result.group(0))
            self.query.set_zip_code(str(result.group(0)))
        else:
            print("It dont work")
        #self.query.set_zip_code(self.zip_code_entry.get())
        #self.query.requests()
        #self.query.print_info()


    
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