
from tkinter import *
from tkinter import ttk

root = Tk()

tree = ttk.Treeview(root)

tree["columns"] = ("c1")

# format Columns
tree.column("#0", width=50)
tree.column("c1", width=300, minwidth=300)

# Define Column Headers
tree.heading("#0", text="#")
tree.heading("#1", text="Command")

row1 = tree.insert("","end",text="Æ", values=("My Command 1", "nope") )
row2 = tree.insert("","end",text="Æ", values=("My Command 2", "nope") )
tree.pack()
root.mainloop()