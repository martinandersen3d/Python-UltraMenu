
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

text1 = Text(root, height=1, font="Helvetica 12")
text1.tag_configure("bold", font="Helvetica 12 bold")

text1.insert("end", "Hello, ") 
text1.insert("end", "world", "bold") 
text1.configure(state="disabled")

row1 = tree.insert("","end",text="Æ", values=("My _Command 1", "nope"))
row2 = tree.insert("","end",text="Æ", values=(text1, "nope") )

tree.pack()

button=Button(root,text="Click Me", underline=6)
button.pack()
root.mainloop()