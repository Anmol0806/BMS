import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox

class DeleteFrame:
    def __init__(self, master):
        self.master = master
        self.df = pd.read_csv('data.csv')

        self.frame = ttk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.frame, columns=list(self.df.columns), show="headings")
        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=125, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.yscrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.yscrollbar.pack(side=tk.RIGHT, fill='y')
        self.tree.configure(yscrollcommand=self.yscrollbar.set)

        self.xscrollbar = ttk.Scrollbar(self.frame, orient="horizontal", command=self.tree.xview)
        self.xscrollbar.pack(side=tk.BOTTOM, fill='x')
        self.tree.configure(xscrollcommand=self.xscrollbar.set)

        self.display_data()

        self.tree.bind("<Delete>", self.delete_row)

    def display_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for i, row in self.df.iterrows():
            self.tree.insert("", "end", values=row.tolist())

    def delete_row(self, event):
        try:
            selected_item = self.tree.selection()[0]
            self.df = self.df.drop(selected_item)
            self.df.to_csv('data.csv', index=False)
            self.display_data()
            messagebox.showinfo("Success", "Row deleted successfully!")
        except IndexError:
            messagebox.showerror("Error", "Please select a row to delete.")

    def destroy(self):
        self.frame.destroy()
