from tkinter import *
import file_report, os

start_path = os.getcwd()

root = Tk()
root.wm_title("Filesize Location Report")

def submit_action(size_check=5368709120, path="."):
    status['text'] = "Processing..."
    status.update_idletasks()
    list_of_dir, curr_dir_size = file_report.get_big_dir(size_check=size_check, directory=path)  # 5GB
    for dir in list_of_dir:
        listbox.insert(END, str(round(file_report.b_to_gb(dir.dir_size),1)) + "GB at " + dir.dir_path)
    os.chdir(start_path)
    status['text'] = "Processing complete."

path_label = Label(root, text="Path:")
path_label.grid(row=0, column=0,sticky=W)
size_label = Label(root, text="Size (in bytes):")
size_label.grid(row=1, column=0,sticky=W)

path_entry = Entry(root)
path_entry.grid(row=0,column=1,sticky=W)
path_entry.insert(END, "C:")
size_entry = Entry(root)
size_entry.grid(row=1,column=1,sticky=W)
size_entry.insert(END, 5368709120)

submit = Button(root, text="Submit", width=10, command=lambda:submit_action(int(size_entry.get()),path_entry.get()))
submit.grid(row=2)

listbox_y_scroll = Scrollbar(root, orient=VERTICAL)
listbox_y_scroll.grid(row=3,column=1,sticky=N+S)
listbox_x_scroll = Scrollbar(root, orient=HORIZONTAL)
listbox_x_scroll.grid(row=4,column=0,sticky=E+W)
listbox = Listbox(root, xscrollcommand=listbox_x_scroll.set, yscrollcommand=listbox_y_scroll.set, width=60)
listbox.grid(row=3,column=0)
listbox_x_scroll.config(command=listbox.xview)
listbox_y_scroll.config(command=listbox.yview)

status = Label(root, text="Waiting for input", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=5, columnspan=2, sticky=E+W)

root.mainloop()