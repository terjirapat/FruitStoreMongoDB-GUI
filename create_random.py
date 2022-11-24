# Random 1000 document input to collection

import pymongo
import numpy as np

myclient = pymongo.MongoClient(
    'mongodb+srv://ter:ter@cluster0.pq4xvaw.mongodb.net/?retryWrites=true&w=majority')
db = myclient['Store']
mycol = db['Product']

year = list(map(int, list(np.repeat(2022, 1000))))
month = list(map(int, np.random.random_integers(12, size=1000)))
day = list(map(int, np.random.random_integers(30, size=1000)))
unit = list(map(int, np.random.random_integers(5, size=1000)))
prod = list(np.random.choice(
    ['Apple', 'Banana', 'Coconut', 'Mango', 'Orange'], size=1000))

hour = [int(i) for i in np.random.normal(12, 4, 1000)]
new_h = []
for i in hour:
    if i < 0 or i >= 24:
        new_h.append(int(np.random.randint(24)))
    else:
        new_h.append(i)


def fruitprice(x):
    if x == 'Apple':
        price = 10
    elif x == 'Banana':
        price = 40
    elif x == 'Coconut':
        price = 50
    elif x == 'Mango':
        price = 40
    elif x == 'Orange':
        price = 30
    return price


for i in range(1000):
    newid = mycol.count_documents({})
    if newid != 0:
        newid = mycol.find_one(sort=[{'_id', -1}])['_id']
    id = newid+1
    price = fruitprice(prod[i])
    mydict = {'_id': id, 'day': day[i], 'month': month[i], 'year': year[i], 'hour': new_h[i],
              'product': prod[i], 'unit': unit[i], 'price': price, 'sale': unit[i]*price}
    x = mycol.insert_one(mydict)
