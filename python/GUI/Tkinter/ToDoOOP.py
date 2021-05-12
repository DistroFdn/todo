import tkinter as tk
from tkinter import messagebox
from tkcalendar import *
from datetime import datetime
from db import Database
import re

# Instanciate databse object
db = Database('ToDo')

# Current time
now = datetime.now()

# Main Application/GUI class


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('To Do ')
        # tk.Width height
        master.geometry("900x500")
        # Create widgets/grid
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        # Populate initial list
        self.populate_list()

    def create_widgets(self):
        self.hour_string=tk.StringVar()
        self.min_string=tk.StringVar()
        self.last_value_sec = ""
        self.last_value = ""        
        f = ('Times', 20)

        if self.last_value == "59" and self.min_string.get() == "0":
            self.hour_string.set(int(self.hour_string.get())+1 if self.hour_string.get() !="23" else 0)   
            self.last_value = self.min_string.get()

        if self.last_value_sec == "59" and self.sec_hour.get() == "0":
            self.min_string.set(int(self.min_string.get())+1 if self.min_string.get() !="59" else 0)
        if self.last_value == "59":
            self.hour_string.set(int(self.hour_string.get())+1 if self.hour_string.get() !="23" else 0)            
            self.last_value_sec = self.sec_hour.get()



        # Descriptions
        self.descriptions_text = tk.StringVar()
        self.descriptions_label = tk.Label(self.master, text='Descriptions', font=('bold', 14), pady=20)
        self.descriptions_label.grid(row=0, column=0, sticky=tk.W)
        self.descriptions_entry = tk.Entry(self.master, textvariable=self.descriptions_text)
        self.descriptions_entry.grid(row=0, column=1)

        # Labels
        self.labels_text = tk.StringVar()
        self.labels_label = tk.Label(self.master, text='Labels', font=('bold', 14))
        self.labels_label.grid(row=1, column=0, sticky=tk.W)
        self.labels_entry = tk.Entry(self.master, textvariable=self.labels_text)
        self.labels_entry.grid(row=1, column=1)


        self.cal = Calendar(self.master, selectmode="day", year=now.year, month=now.month,day=now.day)
        self.cal.grid(row=0, column=2)

        self.min_sb = tk.Spinbox(self.master,from_=0,to=23,wrap=True,textvariable=self.hour_string,width=2,state="readonly",font=f,justify=tk.CENTER)
        self.sec_hour = tk.Spinbox(self.master,from_=0,to=59,wrap=True,textvariable=self.min_string,font=f,width=2,justify=tk.CENTER)
        self.sec = tk.Spinbox(self.master,from_=0,to=59,wrap=True,textvariable=self.sec_hour,width=2,font=f,justify=tk.CENTER)

        self.min_sb.grid(row=0, column=3)
        self.sec_hour.grid(row=0, column=4)
        self.sec.grid(row=0, column=5)


        # Parts List (Listbox)
        self.parts_list = tk.Listbox(self.master, height=8, width=100, border=0)
        self.parts_list.grid(row=5, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=5, column=3)

        # Set scroll to listbox
        self.parts_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.parts_list.yview)

        # Bind select
        self.parts_list.bind('<<ListboxSelect>>', self.select_item)

        # Buttons
        self.add_btn = tk.Button(self.master, text='Add Part', width=12, command=self.add_item)
        self.add_btn.grid(row=4, column=0, pady=20)

        self.remove_btn = tk.Button(self.master, text='Remove Part', width=12, command=self.remove_item)
        self.remove_btn.grid(row=4, column=1)

        self.update_btn = tk.Button(self.master, text='Update Part', width=12, command=self.update_item)
        self.update_btn.grid(row=4, column=2)

        self.clear_btn = tk.Button(self.master, text='Clear Input', width=12, command=self.clear_text)
        self.clear_btn.grid(row=4, column=3)

    def populate_list(self):
        # Delete items before update. So when you keep pressing it doesnt keep getting (show example by calling this twice)
        self.parts_list.delete(0, tk.END)
        # Loop through records
        for row in db.fetch():
            # Insert into list
            self.parts_list.insert(tk.END, row)

    # Add new item
    def add_item(self):
        if self.descriptions_text.get() == '' or self.cal.get_date() == '' or self.labels_text.get() == '':
            messagebox.showerror(
                "Required Fields", "Please include all fields")
            return
        self.m = self.min_sb.get()
        self.h = self.sec_hour.get()
        self.s = self.sec.get()

        self.end_at_time = f'{self.h}:{self.m}:{self.s}'

        # Insert into DB
        db.insert(self.cal.get_date(),self.end_at_time,
                  self.labels_text.get(),self.descriptions_text.get())
        # Clear list
        self.parts_list.delete(0, tk.END)
        # Insert into list
        self.parts_list.insert(tk.END, (self.cal.get_date(),self.end_at_time,self.labels_text.get(),self.descriptions_text.get()))
        
        self.clear_text()
        self.populate_list()

    # Runs when item is selected
    def select_item(self, event):
        # # Create global selected item to use in other functions
        # global self.selected_item
        try:
            # Get index
            index = self.parts_list.curselection()[0]
            # Get selected item
            self.selected_item = self.parts_list.get(index)
            # print(selected_item) # Print tuple
            self.x=re.findall(r"'\s*(\w*\s*\w*\s*\w*)'",self.selected_item)
            

            # Add text to entries
            self.descriptions_entry.delete(0, tk.END)
            self.descriptions_entry.insert(tk.END, self.x[0])
            self.labels_entry.delete(0, tk.END)
            self.labels_entry.insert(tk.END, self.x[1])
        except IndexError:
            pass

    # Remove item
    def remove_item(self):
        self.index = re.match("[(](\d*),",self.selected_item)[1]
        db.remove(self.index)
        self.clear_text()
        self.populate_list()

    # Update item
    def update_item(self):
        self.m = self.min_sb.get()
        self.h = self.sec_hour.get()
        self.s = self.sec.get()
        self.end_at_time = f'{self.h}:{self.m}:{self.s}'

        self.index = re.match("[(](\d*),",self.selected_item)[1]

        db.update(self.index,self.cal.get_date(),self.end_at_time,self.labels_text.get(),self.descriptions_text.get())
        self.populate_list()

    # Clear all text fields
    def clear_text(self):
        self.descriptions_entry.delete(0, tk.END)
        self.labels_entry.delete(0, tk.END)


root = tk.Tk()
app = Application(master=root)
app.master.mainloop()