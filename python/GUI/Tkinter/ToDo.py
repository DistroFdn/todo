# Used libraries
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from datetime import datetime
from db import Database
import re

db = Database('ToDo')
# Current time
now = datetime.now()

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    if descriptions_text.get() == '' or cal.get_date() == '' or min_sb.get() == '' or sec_hour.get() == '' or sec.get() == '' or labels_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    m = min_sb.get()
    h = sec_hour.get()
    s = sec.get()
    
    end_at_time = f'{m}:{h}:{s}'
    db.insert(cal.get_date(),end_at_time,labels_text.get(),descriptions_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (cal.get_date(),end_at_time,labels_text.get(),descriptions_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        x=re.findall(r"'\s*(\w*\s*\w*\s*\w*)'",selected_item)

        descriptions_entry.delete(0, END)
        descriptions_entry.insert(END, x[0])
        labels_entry.delete(0, END)
        labels_entry.insert(END, x[1])
        
    except IndexError:
        pass


def remove_item():
    index = re.match("[(](\d*),",selected_item)[1]
    db.remove(index)
    clear_text()
    populate_list()


def update_item():
    m = min_sb.get()
    h = sec_hour.get()
    s = sec.get()
    end_at_time = f'{m}:{h}:{s}' 

    index = re.match("[(](\d*),",selected_item)[1]
    db.update(index,cal.get_date(),end_at_time,labels_text.get(),descriptions_text.get())
    populate_list()


def clear_text():
    descriptions_entry.delete(0, END)
    labels_entry.delete(0, END)


# Create window object

app = Tk()

hour_string=StringVar()
min_string=StringVar()
last_value_sec = ""
last_value = ""        
f = ('Times', 20)

if last_value == "59" and min_string.get() == "0":
    hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)   
    last_value = min_string.get()

if last_value_sec == "59" and sec_hour.get() == "0":
    min_string.set(int(min_string.get())+1 if min_string.get() !="59" else 0)
if last_value == "59":
    hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)            
    last_value_sec = sec_hour.get()



# Descriptions
descriptions_text = StringVar()
descriptions_label = Label(app, text='Descriptions', font=('bold', 14), pady=20)
descriptions_label.grid(row=0, column=0, sticky=W)
descriptions_entry = Entry(app, textvariable=descriptions_text)
descriptions_entry.grid(row=0, column=1)

# Labels
labels_text = StringVar()
labels_label = Label(app, text='Labels', font=('bold', 14))
labels_label.grid(row=1, column=0, sticky=W)
labels_entry = Entry(app, textvariable=labels_text)
labels_entry.grid(row=1, column=1)


cal = Calendar(app, selectmode="day", year=now.year, month=now.month,day=now.day)
cal.grid(row=0, column=2)

min_sb = Spinbox(app,from_=0,to=23,wrap=True,textvariable=hour_string,width=2,state="readonly",font=f,justify=CENTER)
sec_hour = Spinbox(app,from_=0,to=59,wrap=True,textvariable=min_string,font=f,width=2,justify=CENTER)
sec = Spinbox(app,from_=0,to=59,wrap=True,textvariable=sec_hour,width=2,font=f,justify=CENTER)

min_sb.grid(row=0, column=3)
sec_hour.grid(row=0, column=4)
sec.grid(row=0, column=5)


# Parts List (Listbox)
parts_list = Listbox(app, height=8, width=100, border=0)
parts_list.grid(row=5, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=5, column=3)

# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Part', width=12, command=add_item)
add_btn.grid(row=4, column=0, pady=20)

remove_btn = Button(app, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=4, column=1)

update_btn = Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=4, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=4, column=3)

app.title('To Do')
app.geometry('900x500')

# Populate data
populate_list()

# Start program
app.mainloop()