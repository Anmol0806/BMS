import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox

class UpdateFrame:
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

        self.tree.bind("<Double-1>", self.edit_row)

    def display_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for i, row in self.df.iterrows():
            self.tree.insert("", "end", values=row.tolist())

    def edit_row(self, event):
        try:
            selected_item = self.tree.selection()[0]
            selected_row = self.df.iloc[selected_item]
            edit_window = tk.Toplevel(self.master)
            edit_window.title("Edit Row")

            for i, (col, value) in enumerate(selected_row.items()):
                tk.Label(edit_window, text=col).grid(row=i, column=0)
                entry = tk.Entry(edit_window)
                entry.insert(0, value)
                entry.grid(row=i, column=1)

            def update_row():
                new_values = [entry.get() for entry in edit_window.winfo_children() if isinstance(entry, tk.Entry)]
                self.df.iloc[selected_item] = new_values
                self.df.to_csv('data.csv', index=False)
                self.display_data()
                edit_window.destroy()
                messagebox.showinfo("Success", "Row updated successfully!")

            tk.Button(edit_window, text="Update", command=update_row).grid(row=len(selected_row), columnspan=2)
        except IndexError:
            messagebox.showerror("Error", "Please select a row to edit.")

    def destroy(self):
        self.frame.destroy()
