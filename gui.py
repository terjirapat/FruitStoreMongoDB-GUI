import pymongo
from tkinter import *
from tkinter import messagebox
from datetime import datetime

myclient = pymongo.MongoClient(
    'mongodb+srv://ter:ter@cluster0.zmoirlm.mongodb.net/?retryWrites=true&w=majority')
db = myclient['Store']
mycol = db['Product']

# function


def msgbox(msg, titlebar):
    result = messagebox.askokcancel(title=titlebar, message=msg)
    return result


def fruitprice(x):
    if x.get() == 'Apple':
        price = 10
    elif x.get() == 'Banana':
        price = 40
    elif x.get() == 'Coconut':
        price = 50
    elif x.get() == 'Mango':
        price = 40
    elif x.get() == 'Orange':
        price = 30
    return price


def save():
    r = msgbox('Save Record?', 'Record')
    if r == True:
        newid = mycol.count_documents({})
        if newid != 0:
            newid = mycol.find_one(sort=[{'tranid', -1}])['tranid']
        id = newid+1
        price = fruitprice(create_pd)
        mydict = {'tranid': id, 'day': int(datetime.now().strftime('%d')), 'month': int(datetime.now().strftime('%m')), 'year': int(datetime.now().strftime('%Y')), 'hour': int(datetime.now().strftime('%H')), 'product': create_pd.get(
        ), 'quality': int(create_qty.get()), 'price': price, 'Amount': int(create_qty.get())*price}
        x = mycol.insert_one(mydict)


def read():
    if search_pd.get() == '' and search_day.get() != '' and search_month.get() != '' and search_year.get() != '':
        myquery = {'day': int(search_day.get()), 'month': int(
            search_month.get()), 'year': int(search_year.get())}
    elif search_pd.get() == '' and search_day.get() == '' and search_month.get() != '' and search_year.get() != '':
        myquery = {'month': int(search_month.get()),
                   'year': int(search_year.get())}
    elif search_pd.get() != '' and search_day.get() != '' and search_month.get() != '' and search_year.get() != '':
        myquery = {'product': search_pd.get(), 'day': int(search_day.get()), 'month': int(
            search_month.get()), 'year': int(search_year.get())}
    elif search_pd.get() != '' and search_day.get() == '' and search_month.get() != '' and search_year.get() != '':
        myquery = {'product': search_pd.get(), 'month': int(
            search_month.get()), 'year': int(search_year.get())}
    doc = mycol.find(myquery)
    for x in doc:
        print(x)


def read_all():
    for x in mycol.find():
        print(x)


def update():
    r = msgbox('Update Record?', 'Record')
    price = fruitprice(update_pd)
    if r == True:
        query = {'tranid': int(update_id.get())}
        newvalue = {"$set": {'product': update_pd.get(
        ), 'price': price, 'Amount': int(create_qty.get())*price}}
        mycol.update_one(query, newvalue)


def delete():
    r = msgbox('Delete Record?', 'Record')
    if r == True:
        myquery = {"tranid": int(delete_id.get())}
        mycol.delete_one(myquery)


def delete_all():
    r = msgbox('Delete all data?', 'Record')
    if r == True:
        x = mycol.delete_many({})


def cal():
    x = int(create_qty.get())*fruitprice(create_pd)
    amt = Entry(app, width=20)
    amt.grid(row=3, column=2)
    amt.insert(0, x)
    amt.configure(state=DISABLED)


def plot():
    pass


######################################
fields = ['tranid', 'day', 'month', 'year', 'hour', 'product']
fruits = ['Apple', 'Banana', 'Coconut', 'Mango', 'Orange']
day = list(range(1, 32))
month = list(range(1, 13))
year = list(range(2020, int(datetime.now().strftime('%Y'))+1))

# GUI
app = Tk()
app.title('Fruit Store')
# app.geometry('1050x400')

#### Label ####

# Create
label = Label(app, text='Create')
label.grid(row=0, column=1)

label = Label(app, text='Product')
label.grid(row=1, column=1)
create_pd = StringVar()
drop = OptionMenu(app, create_pd, *fruits)
drop.config(width=14)
drop.grid(row=1, column=2)

label = Label(app, text='Quality')
label.grid(row=2, column=1)
create_qty = Entry(app, width=20)
create_qty.grid(row=2, column=2)

label = Label(app, text='Amount')
label.grid(row=3, column=1)
create_amt = Entry(app, width=20)
create_amt.grid(row=3, column=2)
create_amt.configure(state=DISABLED)

label = Label(app, text='')
label.grid(row=5, column=1)

# Retrieve
label = Label(app, text='Retrieve')
label.grid(row=6, column=1)

label = Label(app, text='Date')
label.grid(row=7, column=1)

search_day = StringVar()
drop = OptionMenu(app, search_day, *day)
drop.config(width=14)
drop.grid(row=7, column=2)

search_month = StringVar()
drop = OptionMenu(app, search_month, *month)
drop.config(width=14)
drop.grid(row=7, column=3)

search_year = StringVar()
drop = OptionMenu(app, search_year, *year)
drop.config(width=14)
drop.grid(row=7, column=4)

search_pd = StringVar()
drop = OptionMenu(app, search_pd, *fruits)
drop.config(width=14)
drop.grid(row=8, column=2)

label = Label(app, text='Product')
label.grid(row=8, column=1)

label = Label(app, text='')
label.grid(row=10, column=1)

# Update
label = Label(app, text='Update')
label.grid(row=12, column=1)

label = Label(app, text='ID')
label.grid(row=13, column=1)

update_id = Entry(app, width=20)
update_id.grid(row=13, column=2)

label = Label(app, text='Product')
label.grid(row=14, column=1)

update_pd = StringVar()
drop = OptionMenu(app, update_pd, *fruits)
drop.config(width=14)
drop.grid(row=14, column=2)

label = Label(app, text='')
label.grid(row=16, column=1)

# delete
label = Label(app, text='Delete')
label.grid(row=17, column=1)

label = Label(app, text='ID')
label.grid(row=18, column=1)

delete_id = Entry(app, width=20)
delete_id.grid(row=18, column=2)

#### Button ####

# Create
btn = Button(app, text='Save', command=save)
btn.grid(row=4, column=1)

btn = Button(app, text='Calculate', command=cal)
btn.grid(row=4, column=2)

# Retrieve
btn = Button(app, text='Read', command=read)
btn.grid(row=9, column=1)

btn = Button(app, text='Read All', command=read_all)
btn.grid(row=9, column=2)

# Update
btn = Button(app, text='Update', command=update)
btn.grid(row=15, column=1)

# Delete
btn = Button(app, text='Delete', command=delete)
btn.grid(column=1, row=19)

btn = Button(app, text='Delete All', command=delete_all)
btn.grid(column=2, row=19)

# Plot
btn = Button(app, text='Plot', command=plot)
btn.grid(column=7, row=20)


app.mainloop()
