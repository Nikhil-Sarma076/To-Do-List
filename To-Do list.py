from tkinter import messagebox, Tk, Label, Entry, Button, Listbox, Scrollbar, END

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("400x400")

        self.tasks = []

        # Custom style
        self.button_style = {"bg": "#4CAF50", "fg": "white", "font": ("Arial", 12)}

        # Labels and Entry
        self.task_label = Label(master, text="Task:", font=("Arial", 12))
        self.task_label.pack(pady=10)

        self.task_entry = Entry(master, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_button = Button(master, text="Add Task", command=self.add_task, **self.button_style)
        self.add_button.pack(pady=10)

        self.delete_button = Button(master, text="Delete Task", command=self.delete_task, **self.button_style)
        self.delete_button.pack(pady=10)

        # Listbox with Scrollbar
        self.task_listbox = Listbox(master, width=50, height=10, selectbackground="yellow", selectmode="SINGLE", font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side="right", fill="y")

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Load existing tasks
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.save_tasks()
            self.task_entry.delete(0, END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_list()
            self.save_tasks()

    def update_task_list(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            self.task_listbox.insert(END, task)

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_task_list()
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = Tk()
    todo_app = TodoApp(root)
    root.mainloop()
