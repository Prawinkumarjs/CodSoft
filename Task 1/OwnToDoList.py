from tkinter import *
from tkinter import messagebox


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END,task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def deleteTask():
    lb.delete(ANCHOR)


ws = Tk()
ws.geometry('500x440+500+200')        # width * height + x-position + y-position
ws.title('Own To Do List')
ws.config(bg='gray')               # background color
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='black',
    highlightthickness=0,
    selectbackground='blue',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Eat Apple',
    'Drink Water',
    'Go Gym',
    'Write Assignment',
    'Create a Documentation',
    'Take a nap',
    'Learn Something',
    'Paint Canvas'
]
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
    text='Add Task',
    font='times 14',
    bg='green',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font='times 14',
    bg='red',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
