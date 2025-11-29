# windows/register_user.py

import tkinter as tk
from tkinter import messagebox
from utils.utils import validate_empty

class RegisterUserWindow(tk.Toplevel):
    """
    A window for registering new users in the system.
    """

    def __init__(self, master, data_manager):
        """
        Initializes the register user window.
        :param master: main window or parent
        :param data_manager: instance of DataManager
        """
        super().__init__(master)
        self.title("Registrar usuario")
        self.geometry("300x200")
        self.data_manager = data_manager

        # === Widgets ===
        self.label_name = tk.Label(self, text="Usuario:")
        self.entry_name = tk.Entry(self)

        self.label_id = tk.Label(self, text="ID:")
        self.entry_id = tk.Entry(self)

        self.button_register = tk.Button(self, text="Añadir usuario", command=self.register_user)

        # === Layout ===
        self.label_name.pack(pady=5)
        self.entry_name.pack(pady=5)
        self.label_id.pack(pady=5)
        self.entry_id.pack(pady=5)
        self.button_register.pack(pady=15)

    def register_user(self):
        """
        Gets the data from input fields and adds a user to the system.
        """
        name = self.entry_name.get()
        user_id = self.entry_id.get()

        is_valid, msg = validate_empty({"Name": name, "ID": user_id})
        if not is_valid:
            messagebox.showerror("Validation Error", msg)
            return

        if self.data_manager.find_user_by_id(user_id):
            messagebox.showerror("Error", "Ya existe un un usuario registrado con ese ID")
        else:
            self.data_manager.add_user(name, user_id)
            # Log activity
            try:
                self.data_manager.add_log(f"User registered: {name} (ID: {user_id})")
            except Exception:
                pass
            messagebox.showinfo("Success", "Se registro satisfactoriamente el usuario")
            self.destroy()
