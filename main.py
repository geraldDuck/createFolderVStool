import tkinter as tk
import subprocess
import time

directory = ""

root = tk.Tk()
root.geometry("440x200")
root.title("Create File")


folder_name_var = tk.StringVar()
file_name_var = tk.StringVar()


def submit():
    folder = folder_name_var.get()
    file = file_name_var.get()

    folder_name_var.set("")
    file_name_var.set("")

    subprocess.run(f"mkdir {folder} && cd {folder} && type nul > {file} && code .")
    time.sleep(1)
    exit()

folder_label = tk.Label(root, text="Folder Name", font=("calibre", 10, "bold"))
folder_entry = tk.Entry(root, textvariable=folder_name_var,font=("calibre", 10, "normal"))

file_label = tk.Label(root, text="File Name", font=("calibre", 10, "bold"))
file_entry = tk.Entry(root, textvariable=file_name_var,font=("calibre", 10, "normal"))

sub_btn = tk.Button(root, text="Create", command=submit)


folder_label.grid(row=1, column=0)
folder_entry.grid(row=1, column=1)
file_label.grid(row=2, column=0)
file_entry.grid(row=2, column=1)
sub_btn.grid(row=3, column=1)

root.mainloop()