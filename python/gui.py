from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

# writes a message to the conversation text box
def writeToConvo(text):
    # set to normal in order to write
    convo["state"] = "normal" 
    convo.insert("end", text)
    # disable when we're done writing
    convo["state"] = "disabled" 

def submitInput():
    if (len(text.get()) > 0):
        writeToConvo(text.get()+"\n")
        text.delete(0,"end")

if __name__ == "__main__":   
    # initialize root element & grid geometry manager
    root = Tk()
    root.title("Dr. Notadoctor, MD")
    content = ttk.Frame(root)
    content.grid(column=0, row=0, sticky=(N,S,E,W))

    # initialize slave widgets
    # button is disabled until user inputs text
    submit = ttk.Button(content, text="Submit", command=submitInput)
    text = ttk.Entry(content)
    convo = scrolledtext.ScrolledText(content, state="disabled")

    # lock slaves to grid 
    submit.grid(column=1, row=2, sticky=(N,S,E,W))
    text.grid(column=0, row=1, rowspan=2, pady=(0,1), sticky=(S,E,W))
    convo.grid(column=0, row=0, rowspan=2, columnspan=2, sticky=(N,S,E,W))

    # active sizing settings
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.columnconfigure(0, weight=3) # text entry box
    content.columnconfigure(1, weight=1) # submit button
    content.rowconfigure(0, weight=1) # conversation window
    content.rowconfigure(1, weight=1) # text entry & submit

    # show tk window(s)
    root.mainloop()