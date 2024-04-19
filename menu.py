import pandas as pd
import datetime
from tabulate import tabulate

df = pd.read_csv('data.csv');

def show_all_data():
    print()
    print(tabulate(df, headers='keys', tablefmt='pretty' ,  showindex=False))
    print()

def date_format(date_string):
    parsed_date = datetime.datetime.strptime(date_string, "%d-%m-%Y").date()
    formatted_date = parsed_date.strftime("%d-%m-%Y")
    return formatted_date

def add_data(cname, oname , price, quantity):
    global df
    new_id = len(df) + 1 
    date = datetime.date.today()
    date = date.strftime("%d-%m-%Y")
    time = datetime.datetime.now().time()
    time = time.strftime("%I:%M %p")
    new_row = pd.DataFrame({'id': [new_id], 'cname': [cname], 'oname': [oname], 'price': [price], 'time': [time], 'date': [date], 'quantity': [quantity]})
    df = pd.concat([df, new_row], ignore_index=True)
    print("Done!!\n")
    df.to_csv('data.csv', index=False)

def search_row_by_id(row_id):
    global df
    print()
    row = df[df['id'] == row_id]
    if not row.empty:
        print(tabulate(row, headers='keys', tablefmt='pretty' , showindex=False))
    else:
        print("Row with ID {} not found.".format(row_id))
    print()

def update_value_by_id(id_to_update, column_name, new_value):
    global df
    df.loc[df['id'] == id_to_update, column_name] = new_value
    df.to_csv('data.csv', index=False)
    print("Done\n")
    
def delete_row_by_id(row_id):
    global df 
    print()
    row = df[df['id'] == row_id]
    if not row.empty:
        print(tabulate(row, headers='keys', tablefmt='pretty' , showindex=False))
        df = df[df['id'] != row_id]
        df.to_csv('data.csv', index=False)   
    else:
        print("Row with ID {} not found.".format(row_id))
    print()

while True:
    print("1. Add Data\n2. Search Data By Id\n3. Update Data\n4. Show All Data\n5. Delete Data by ID")
    c = int(input('=> '))
    if c == 4:
        show_all_data()
    elif c == 1:
        print()
        cname = input("Enter customer name: ")
        oname = input("Enter order name: ")
        price = float(input("Enter price: "))
        q = int(input("Enter quantity: "))
        add_data(cname , oname ,price , q)
    elif c == 2:
        print()
        id = int(input("Enter ID to search: "))
        search_row_by_id(id)
    elif c == 3:
        print()
        id = int(input("Enter order id to update: "))
        what = input("What to update (cname,oname,quantity): ")
        newval = input("Enter new {}: ".format(what))
        update_value_by_id(id , what , newval)
    elif c == 5:
        id = int(input("Enter order id to delete: "))
        delete_row_by_id(id)
    else:
        exit()