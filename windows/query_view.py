# windows/query.py

import tkinter as tk
from tkinter import ttk

class QueryWindow(tk.Toplevel):
    """
    A window to query and display books and users.
    """

    def __init__(self, master, data_manager):
        """
        Initializes the query window.
        :param master: main window or parent
        :param data_manager: instance of DataManager
        """
        super().__init__(master)
        self.title("Consultas")
        self.geometry("600x400")
        self.data_manager = data_manager

        # === Widgets ===
        self.label_options = tk.Label(self, text="Seleccione la seccion a consultar:")
        self.combo_options = ttk.Combobox(self, values=["libros", "Usuarios", "Prestamos"])
        self.combo_options.current(0)

        self.button_show = tk.Button(self, text="Consultar", command=self.show_data)

        self.text_area = tk.Text(self, width=70, height=20)

        # === Layout ===
        self.label_options.pack(pady=5)
        self.combo_options.pack(pady=5)
        self.button_show.pack(pady=10)
        self.text_area.pack(pady=5)

    def show_data(self):
        selected_option = self.combo_options.get()
        self.text_area.delete("1.0", tk.END)

        if selected_option == "libros":
            books = self.data_manager.books
            for book in books:
                status = "Loaned" if book.is_loaned else "Available"
                self.text_area.insert(tk.END, f"ISBN: {book.isbn}, Title: {book.title}, Status: {status}\n")

        elif selected_option == "Usuarios":
            users = self.data_manager.users
            for user in users:
                self.text_area.insert(tk.END, f"ID: {user.user_id}, Name: {user.name}\n")

        elif selected_option == "Prestamos":
            loaned_books = self.data_manager.get_loaned_books()
            if loaned_books:
                for book in loaned_books:
                    self.text_area.insert(tk.END, f"ISBN: {book.isbn}, Title: {book.title}, Status: Loaned\n")
        else:
            self.text_area.insert(tk.END, "No books are currently loaned.\n")
