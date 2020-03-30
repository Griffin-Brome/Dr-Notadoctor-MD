from tkinter import *
from tkinter import ttk

# initialize root widget & grid geometry manager
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
scroll.grid(column=0, row=0, sticky=(N,S))

convo['yscrollcommand'] = scroll.set
# active sizing settings
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
# show tk window(s)
root.mainloop()