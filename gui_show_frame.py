import tkinter as tk
from tkinter import ttk
import pandas as pd

class ShowFrame:
    def __init__(self , main_frame):
        self.df = pd.read_csv('data.csv')
        self.frame = ttk.Frame(main_frame)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.frame2 = ttk.Frame(main_frame)
        self.frame2.pack(side=tk.TOP , fill=tk.BOTH)
    
    def start(self):

        self.style = ttk.Style()
        self.style.configure("TEntry", foreground="black", background="white", font=("Arial", 20) , width=30)
        self.style.configure("TButton", foreground="black", background="white", font=("Arial", 15)) 
        self.style.configure("Treeview", font=("Arial", 12))
        self.style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        self.style.configure("Treeview", rowheight=30)
        self.style.configure("Treeview", background="lightGray", foreground="black", fieldbackground="black")
        
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.frame2, textvariable=self.search_var , style="TEntry")
        self.search_entry.pack(side=tk.LEFT, padx=5, pady=5)
        self.search_button = ttk.Button(self.frame2, text="Search", command=self.search_id , style="TButton")
        self.search_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.tree = ttk.Treeview(self.frame, columns=list(self.df.columns), show="headings", style="Treeview")

        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=125)  # Set a default width for columns (you can adjust this)
            self.tree.column(col, anchor=tk.CENTER)  # Center align column headers
            self.tree.column(col, stretch=False)  # Prevent column from stretching
            
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Create a horizontal scrollbar
        self.xscrollbar = ttk.Scrollbar(self.frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(xscrollcommand=self.xscrollbar.set)

        # Display all data initially
        self.display_data(self.df)
        
    def destroy(self):
        self.frame.destroy()
        self.frame2.destroy()
    
    def search(self):
        search_term = self.search_var.get().lower()
        if search_term:
            filtered_df = self.df[self.df.astype(str).apply(lambda x: x.str.lower()).apply(lambda x: x.str.contains(search_term, na=False)).any(axis=1)]
            self.display_data(filtered_df)
        else:
            self.display_data(self.df)
            
    def search_id(self):
        self.search_term = self.search_var.get().lower()
        if self.search_term:
            filtered_df = self.df[self.df['id'].astype(str).str.lower().str.contains(self.search_term, na=False)]
            self.display_data(filtered_df)
        else:
            self.display_data(self.df)

    def display_data(self , data):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for i, row in data.iterrows():
            self.tree.insert("", "end", values=row.tolist()) 
