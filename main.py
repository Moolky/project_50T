from tkinter import *
from tkinter import filedialog
import json

root = Tk()
root.title("Text Editor")

text = Text(root)
text.pack()

location_list = []
selected_text_list = []

location_listbox = Listbox(root)
location_listbox.pack()

selected_text_listbox = Listbox(root)
selected_text_listbox.pack()

def open_con_file():
    global location_list
    global selected_text_list
    location_list.clear()
    selected_text_list.clear()
    text.tag_remove("highlight", "1.0", END)
    location_listbox.delete(0, END)
    selected_text_listbox.delete(0, END)
    text.config(state=NORMAL)
    filepath = filedialog.askopenfilename(filetypes=[("json files", "*.json")])

    with open(filepath, "r") as file:
        location_list = json.load(file)
    with open(filepath.replace("_location_list.json",""), 'r') as file:
        content = file.read()
        text.insert("1.0", content)
    for start, end in location_list:
        text.tag_add("highlight", start, end)
        selected_text = text.get(start, end)
        selected_text_list.append(selected_text)
        selected_text_listbox.insert(END, selected_text)
        location_listbox.insert(END, f"{start} - {end}")
    text.config(state=DISABLED)
    print("location_list:", location_list)
    print("selected_text_list:", selected_text_list)


def save_con_file():
    global location_list
    filepath = filedialog.asksaveasfilename()
    if not filepath.endswith('.json'):
        filepath += '.json'
    with open(filepath, "w") as file:
        json.dump(location_list, file)
    file.close()

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("res files", "*.res")])
    with open(filepath, 'r') as file:
        content = file.read()
        text.insert("1.0", content)
    text.config(state=DISABLED)

def save_location(event=None):
    global location_list
    global selected_text_list
    start = text.index("sel.first")
    end = text.index("sel.last")
    if (start, end) in location_list:
        index = location_list.index((start, end))
        location_list.remove((start, end))
        selected_text_list.pop(index)
        text.tag_remove("highlight", start, end)
        location_listbox.delete(index)
        selected_text_listbox.delete(index)
    else:
        location_list.append((start, end))
        selected_text = text.get(start, end)
        selected_text_list.append(selected_text)
        text.tag_add("highlight", start, end)
        location_listbox.insert(END, f"{start} - {end}")
        selected_text_listbox.insert(END, selected_text)
    print("location_list:", location_list)
    print("selected_text_list:", selected_text_list)

open_button = Button(root, text="打开文件", command=open_file)
open_button.pack()

save_location_button = Button(root, text="保存文本位置(T)", command=save_location)
save_location_button.pack()

open_con_file_button = Button(root, text="应用配置文件", command=open_con_file)
open_con_file_button.pack()

save_con_file_button = Button(root, text="保存配置文件", command=save_con_file)
save_con_file_button.pack()

root.bind("<KeyPress-t>", save_location)
text.tag_config("highlight", background="yellow")

is_editable = False

root.mainloop()

