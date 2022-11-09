import pymongo
import tkinter as tk
from tkinter import messagebox

client = pymongo.MongoClient('mongodb+srv://ter:ter@cluster0.zmoirlm.mongodb.net/?retryWrites=true&w=majority')
db = client['Store']
col = db['Transaction']

def msgbox(msg, titlebar):
    result = messagebox.askokcancel(title=titlebar, message=msg)
    return result

def save():
    r=msgbox('save record?', 'record')
    if r==True:
        newid = col.count_documents(())
        if newid!=0:
            newid = col.find_one(sort=[('studid', -1)])['studid']
        id = newid+1
        cid.set(id)
        mydict = {'stuid': int(custid.get()), 'studname': custname.get(), 'studemail': custmail.get(), 'studcourse': custcourse.get()}
        x = col.insert_one(mydict)

def delete():
    pass

def update():
    pass

app = tk.Tk()
app.title('POS')
app.geometry('1050x400')
app.configure(bg='black')

#Label
label = tk.Label(app, text='Students Form', width=30, height=1, bg='white')
label.config(font=('Courier',10))
label.grid(column=2, row=1)

label = tk.Label(app, text='Student ID:', width=10, height=1, bg='white')
label.grid(column=1, row=2)
cid=tk.StringVar()
custid = tk.Entry(app, textvariable=cid)
custid.grid(column=2, row=2)
custid.configure(state=tk.DISABLED)

label = tk.Label(app, text='Student name:', width=10, height=1, bg='white')
label.grid(column=1, row=3)
cid=tk.StringVar()
custname = tk.Entry(app, textvariable=cid)
custname.grid(column=2, row=3)

label = tk.Label(app, text='Student Email:', width=10, height=1, bg='white')
label.grid(column=1, row=4)
cid=tk.StringVar()
custmail = tk.Entry(app, textvariable=cid)
custmail.grid(column=2, row=4)

label = tk.Label(app, text='Student Course:', width=10, height=1, bg='white')
label.grid(column=1, row=5)
cid=tk.StringVar()
custcourse = tk.Entry(app, textvariable=cid)
custcourse.grid(column=2, row=5)

#Button
btn = tk.Button(text='Save', command=save)
btn.grid(column=1, row=6)

btn = tk.Button(text='Delete', command=delete)
btn.grid(column=2, row=6)

btn = tk.Button(text='Update', command=update)
btn.grid(column=3, row=6)

app.mainloop()
 