# windows/register_book.py

import tkinter as tk
from tkinter import messagebox
from utils.utils import validate_empty

class RegisterBookWindow(tk.Toplevel):
    """
    A window for registering new books in the system.
    """

    def __init__(self, master, data_manager):
        """
        Initializes the register book window.
        :param master: main window or parent
        :param data_manager: instance of DataManager
        """
        super().__init__(master)
        self.title("Registrar libro")
        self.geometry("300x250")
        self.data_manager = data_manager

        # === Widgets ===
        self.label_title = tk.Label(self, text="Titulo del libro:")
        self.entry_title = tk.Entry(self)

        self.label_author = tk.Label(self, text="Autor")
        self.entry_author = tk.Entry(self)

        self.label_isbn = tk.Label(self, text="ISBN:")
        self.entry_isbn = tk.Entry(self)

        self.button_register = tk.Button(self, text="Añadir libro", command=self.register_book)

        # === Layout ===
        self.label_title.pack(pady=5)
        self.entry_title.pack(pady=5)
        self.label_author.pack(pady=5)
        self.entry_author.pack(pady=5)
        self.label_isbn.pack(pady=5)
        self.entry_isbn.pack(pady=5)
        self.button_register.pack(pady=15)

    def register_book(self):
        """
        Gets the data from input fields and adds a book to the system.
        """
        title = self.entry_title.get()
        author = self.entry_author.get()
        isbn = self.entry_isbn.get()

        is_valid, msg = validate_empty({"Title": title, "Author": author, "ISBN": isbn})
        if not is_valid:
            messagebox.showerror("Validation Error", msg)
            return

        if self.data_manager.find_book_by_isbn(isbn):
            messagebox.showerror("Error", "El libro con el codigo ISBN ya existe")
        else:
            self.data_manager.add_book(title, author, isbn)
            messagebox.showinfo("Success", "El libro fue registrado satisfactoriamente")
            self.destroy()
