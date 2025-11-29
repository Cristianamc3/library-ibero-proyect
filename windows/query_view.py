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
        # Filter input
        self.label_filter = tk.Label(self, text="Filter:")
        self.entry_filter = tk.Entry(self)
        self.label_filter.pack(pady=(5, 0))
        self.entry_filter.pack(pady=2)
        # Available only checkbox (applies to Books)
        self.available_only_var = tk.BooleanVar(value=False)
        self.check_available = tk.Checkbutton(self, text="Available Only", variable=self.available_only_var)
        self.check_available.pack(pady=(2, 5))
        self.button_show.pack(pady=10)
        self.text_area.pack(pady=5)

    def show_data(self):
        selected_option = self.combo_options.get()
        self.text_area.delete("1.0", tk.END)

        # prepare filter
        query = self.entry_filter.get().strip().lower()

        if selected_option == "libros":
            books = self.data_manager.books
            results = []
            for book in books:
                # If 'Available Only' is checked, skip loaned books
                if self.available_only_var.get() and book.is_loaned:
                    continue
                hay = False
                if not query:
                    hay = True
                else:
                    if query in (book.title or "").lower() or query in (book.author or "").lower() or query in (str(book.isbn) or "").lower():
                        hay = True
                if hay:
                    status = "Loaned" if book.is_loaned else "Available"
                    results.append(f"ISBN: {book.isbn}, Title: {book.title}, Status: {status}\n")
            if results:
                for line in results:
                    self.text_area.insert(tk.END, line)
            else:
                self.text_area.insert(tk.END, "No results found.\n")

        elif selected_option == "Usuarios":
            users = self.data_manager.users
            results = []
            for user in users:
                if not query or query in (user.name or "").lower() or query in str(user.user_id).lower():
                    results.append(f"ID: {user.user_id}, Name: {user.name}\n")
            if results:
                for line in results:
                    self.text_area.insert(tk.END, line)
            else:
                self.text_area.insert(tk.END, "No results found.\n")

        elif selected_option == "Prestamos":
            loaned_books = self.data_manager.get_loaned_books()
            results = []
            for book in loaned_books:
                if not query or query in (book.title or "").lower() or query in str(book.isbn).lower():
                    results.append(f"ISBN: {book.isbn}, Title: {book.title}, Status: Loaned\n")
            if results:
                for line in results:
                    self.text_area.insert(tk.END, line)
            else:
                self.text_area.insert(tk.END, "No results found.\n")
        else:
            self.text_area.insert(tk.END, "No results found.\n")
