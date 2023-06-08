import tkinter as tk
from tkinter import ttk, filedialog


class App:
    def __init__(self, root):
        self.root = root

        self.folder_button = ttk.Button(root, text="选择文件夹", command=self.select_folder)
        self.folder_button.pack()

        # A label to show the selected folder
        self.folder_label = ttk.Label(root, text="")
        self.folder_label.pack()

        self.model_var = tk.StringVar()
        self.model_dropdown = ttk.Combobox(root, textvariable=self.model_var)
        self.model_dropdown['values'] = ('Model 1', 'Model 2', 'Model 3')  # add your models here
        self.model_dropdown.pack()

        self.recognize_button = ttk.Button(root, text="开始识别", command=self.recognize)
        self.recognize_button.pack()

        # Image will be put here, adjust accordingly
        self.image_label = ttk.Label(root)
        self.image_label.pack()

        # Create treeview
        self.tree = ttk.Treeview(root, columns=('id', 'action'))
        self.tree.pack()
        self.tree.heading('id', text='ID')
        self.tree.heading('action', text='Action')

        # Bind treeview row click event to delete method
        self.tree.bind("<Double-1>", self.delete_mask)

        self.prev_button = ttk.Button(root, text="上一张", command=self.previous_image)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = ttk.Button(root, text="下一张", command=self.next_image)
        self.next_button.pack(side=tk.RIGHT)

        self.save_button = ttk.Button(root, text="保存", command=self.save)
        self.save_button.pack()

    def select_folder(self):
        self.folder_selected = filedialog.askdirectory()
        # Update the label with the selected folder name
        self.folder_label.config(text=self.folder_selected)

    def recognize(self):
        pass  # implement the recognition process here

    def delete_mask(self, event):
        selected_item = self.tree.selection()[0]  # get selected item
        self.tree.delete(selected_item)  # delete from treeview
        # implement further mask deletion process here

    def previous_image(self):
        pass  # implement image navigation here

    def next_image(self):
        pass  # implement image navigation here

    def save(self):
        pass  # implement save function here

    def update_table(self, ids):
        # Clear current items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Populate with new items
        for id in ids:
            self.tree.insert('', 'end', id, values=(id, 'Delete (Double click)'))


root = tk.Tk()
app = App(root)
root.mainloop()
