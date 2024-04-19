
import tkinter as tk
from tkinter import ttk
import pandas as pd
import datetime

class AddFrame:
    def __init__(self , main_frame):
        self.top_frame = tk.Frame(main_frame, bg="#151515")
        
    def on_button_click(self):
        cname = self.entry_customer_name.get()
        oname = self.entry_ordername_name.get()
        total = self.entry_total.get()
        quantity = self.entry_quantity.get()
        if cname == "" or oname == "":
            return 
        self.add_data(cname , oname , total , quantity)
        self.button.config(text="Successful", bg="green")
        
    def add_data(self , cname, oname , total, quantity):
        df = pd.read_csv('data.csv')
        new_id = len(df) + 1 
        date = datetime.date.today()
        date = date.strftime("%d-%m-%Y")
        time = datetime.datetime.now().time()
        time = time.strftime("%I:%M %p")
        new_row = pd.DataFrame({'id': [new_id], 'cname': [cname], 'oname': [oname], 'total': [total], 'time': [time], 'date': [date], 'quantity': [quantity]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv('data.csv', index=False)
            
    def destroy(self):
        self.top_frame.destroy()
        
    def start(self , main_frame):
        # self.top_frame.place(x= 0, y= 0 , width=650)
        self.top_frame.pack(fill=tk.BOTH, expand=True)
        self.label_customer_name = tk.Label(self.top_frame, text="Customer Name:", bg="black", font=("Arial", 20), fg="white")
        self.label_customer_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_customer_name = tk.Entry(self.top_frame, font=("Arial", 20), fg="black")
        self.entry_customer_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_ordername_name = tk.Label(self.top_frame, text="Order Name:", bg="#151515", font=("Arial", 20), fg="white")
        self.label_ordername_name.grid(row=1, column=0, padx=10, pady=10)
        self.entry_ordername_name = tk.Entry(self.top_frame, font=("Arial", 20), fg="black")
        self.entry_ordername_name.grid(row=1, column=1, padx=10, pady=20)

        self.label_total = tk.Label(self.top_frame, text="Total Price:", bg="black", font=("Arial", 20), fg="white")
        self.label_total.grid(row=2, column=0, padx=10, pady=10)
        self.entry_total = tk.Entry(self.top_frame, font=("Arial", 20), fg="black")
        self.entry_total.grid(row=2, column=1, padx=10, pady=20)

        self.label_quantity = tk.Label(self.top_frame, text="Quantity:", bg="black", font=("Arial", 20), fg="white")
        self.label_quantity.grid(row=3, column=0, padx=10, pady=10)
        self.entry_quantity = tk.Entry(self.top_frame, font=("Arial", 20), fg="black")
        self.entry_quantity.grid(row=3, column=1, padx=10, pady=20)
    
        self.button = tk.Button(self.top_frame, text="Submit", command=self.on_button_click, font=("Arial", 20), fg="black", bg="white" , width=30)
        self.button.grid(row=4, columnspan=2, padx=10, pady=10)  # Adjust the row and column as needed

        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.columnconfigure(1, weight=1)
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_rowconfigure(1, weight=1)
        self.top_frame.grid_rowconfigure(2, weight=1)
        self.top_frame.grid_rowconfigure(3, weight=1)
        self.top_frame.grid_rowconfigure(4, weight=1)
        







