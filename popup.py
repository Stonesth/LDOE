import tkinter as tk

root = tk.Tk()

# create a label with some text
label = tk.Label(root, text="Hello, world!")

# add the label to the window
label.place(relx=0.5, rely=0.5, anchor="center")

# create a function to show the popup
def show_popup():
    popup = tk.Toplevel()
    popup.title("Popup")
    label = tk.Label(popup, text="This is a popup!")
    label.pack()
    popup.geometry("+%d+%d" % (root.winfo_rootx()+50, root.winfo_rooty()+50))
    
# create a button to show the popup
button = tk.Button(root, text="Show popup", command=show_popup)
button.place(relx=0.5, rely=0.7, anchor="center")

# set the size of the root window
root.geometry("300x200")

# start the main event loop
root.mainloop()
