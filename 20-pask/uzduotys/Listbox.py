import tkinter as T
window = T.Tk()
window.geometry("250x200")
label1 = T.Label(window,text = "A list of favourite languages...")
listbox = T.Listbox(window)
listbox.insert(1,"1")
listbox.insert(2, "2")
listbox.insert(3, "3")
label1.pack()
listbox.pack()
window.mainloop()
