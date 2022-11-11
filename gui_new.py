import pymongo
from tkinter import *
from tkinter import messagebox
from datetime import datetime

myclient = pymongo.MongoClient(
    'mongodb+srv://ter:ter@cluster0.zmoirlm.mongodb.net/?retryWrites=true&w=majority')
db = myclient['Library']
mycol = db['Book']

# function

def msgbox(msg, titlebar):
    result = messagebox.askokcancel(title=titlebar, message=msg)
    return result


def save():
    r = msgbox('Save Record?', 'Record')
    if r == True:
        mydict = {'Date': d.get(), 'Time': t.get(), 'Product': pdname.get(
        ), 'Quality': int(qty.get()), 'Price': int(price.get())}
        x = mycol.insert_one(mydict)


def delete():
    r = msgbox('Delete?', 'Record')
    if r == True:
        myquery = {"Title": "C# Programming"}
        mycol.delete_one(myquery)


def update():
    pass


def retrieve():
    for x in mycol.find():
        print(x)


def clear():
    x = mycol.delete_many({})


def cal():
    x = int(qty.get())*int(price.get())
    amt = Entry(app, width=20)
    amt.grid(row=7, column=2)
    amt.insert(0, x)
    amt.configure(state=DISABLED)


def plot():
    print(int(qty.get())*int(price.get()))

######################################

# GUI


app = Tk()
app.title('Test')
# app.geometry('1050x400')

#### Label ####
label = Label(app, text='Hello world')
label.grid(row=1, column=2)

# Date
label = Label(app, text='Date')
label.grid(row=2, column=1)
cur_date = datetime.now().strftime('%d/%m/%Y')
d = Entry(app, width=20)
d.grid(row=2, column=2)
d.insert(0, cur_date)
d.configure(state=DISABLED)

# Time
label = Label(app, text='Time')
label.grid(row=3, column=1)
cur_time = datetime.now().strftime('%H:%M:%S')
t = Entry(app, width=20)
t.grid(row=3, column=2)
t.insert(0, cur_time)
t.configure(state=DISABLED)

# Product
label = Label(app, text='Product')
label.grid(row=4, column=1)
pdname = Entry(app, width=20)
pdname.grid(row=4, column=2)

# Quality
label = Label(app, text='Quality')
label.grid(row=5, column=1)
qty = Entry(app, width=20)
qty.grid(row=5, column=2)

# Price
label = Label(app, text='Price')
label.grid(row=6, column=1)
price = Entry(app, width=20)
price.grid(row=6, column=2)

# Amount
label = Label(app, text='Amount')
label.grid(row=7, column=1)
amt = Entry(app, width=20)
amt.grid(row=7, column=2)
amt.configure(state=DISABLED)

#### Button ####
btn = Button(app, text='Save', command=save)
btn.grid(column=1, row=20)

btn = Button(app, text='Delete', command=delete)
btn.grid(column=2, row=20)

btn = Button(app, text='Update', command=update)
btn.grid(column=3, row=20)

btn = Button(app, text='Retrieve', command=retrieve)
btn.grid(column=4, row=20)

btn = Button(app, text='Clear', command=clear)
btn.grid(column=5, row=20)

btn = Button(app, text='Calculate', command=cal)
btn.grid(column=6, row=20)

btn = Button(app, text='Plot', command=plot)
btn.grid(column=7, row=20)


app.mainloop()
