from tkinter import *



def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        from tkinter.messagebox import showwarning
        showwarning("Wrong")


def deleteTask():
    lb.delete(ANCHOR)


ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To_Do')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,

)
lb.pack(side=LEFT, fill=BOTH)

task_list = [ 'Play video games' , 'Eat chips']

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add',
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame, text='Delete ',command=deleteTask )
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
