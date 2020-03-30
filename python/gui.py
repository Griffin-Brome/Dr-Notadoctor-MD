from tkinter import *
from tkinter import ttk

# initialize root element & grid geometry manager
root = Tk()
root.title("Dr. Notadoctor, MD")
content = ttk.Frame(root)
content.grid(column=0, row=0, sticky=(N,S,E,W))

# initialize slave widgets
submit = ttk.Button(content, text="Submit")
text = ttk.Entry(content)
convo = Text(content, state="disabled", width=80, height=80)
scroll = ttk.Scrollbar(convo, orient=VERTICAL, command=convo.yview)

# lock slaves to grid 
submit.grid(column=1, row=2, sticky=(N,S,E,W))
text.grid(column=0, row=1, rowspan=2, sticky=(S,E,W))
convo.grid(column=0, row=0, rowspan=2, columnspan=2, sticky=(N,S,E,W))
scroll.grid(column=1, row=0, sticky=(N,S))

convo['yscrollcommand'] = scroll.set
convo.configure(yscrollcommand=scroll.set)

# active sizing settings
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3, minsize=300) # text entry box
content.columnconfigure(1, weight=1, minsize=300) # submit button
content.rowconfigure(0, weight=1, minsize=500) # conversation window
content.rowconfigure(1, weight=1) # text entry & submit

# show tk window(s)
root.mainloop()