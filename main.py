# main.py

import tkinter as tk
from data_manager import DataManager
from windows.book_registration import RegisterBookWindow
from windows.user_registration import RegisterUserWindow
from windows.loan_return import LoansWindow
from windows.query_view import QueryWindow

class LibraryApp(tk.Tk):
    """
    Main window of the library system.
    """

    def __init__(self):
        super().__init__()
        self.title("Biblioteca Julio Mario Santo Domingo")
        self.geometry("400x350")
        self.configure(bg="#b5caff")

        # Initialize the data manager
        self.data_manager = DataManager()

        # === Title Label ===
        self.label_title = tk.Label(self, text="Julio Mario Santo Domingo", font=("Arial", 16))
        self.label_title.configure(bg="#b5caff")
        self.label_title.pack(pady=20)

        # === Buttons ===
        self.btn_register_book = tk.Button(self, text="Registar Libro", width=30, command=self.open_register_book)
        self.btn_register_user = tk.Button(self, text="Registrar Usuario", width=30, command=self.open_register_user)
        self.btn_loan = tk.Button(self, text="Prestamo/Devolución libro", width=30, command=self.open_loan)
        self.btn_query = tk.Button(self, text="Consultas", width=30, command=self.open_query)
        self.btn_exit = tk.Button(self, text="Salida", width=30, command=self.quit)

        # === Layout ===
        self.btn_register_book.pack(pady=5)
        self.btn_register_user.pack(pady=5)
        self.btn_loan.pack(pady=5)
        self.btn_query.pack(pady=5)
        self.btn_exit.pack(pady=20)

    # === Navigation Methods ===

    def open_register_book(self):
        RegisterBookWindow(self, self.data_manager)

    def open_register_user(self):
        RegisterUserWindow(self, self.data_manager)

    def open_loan(self):
        LoansWindow(self, self.data_manager)

    def open_query(self):
        QueryWindow(self, self.data_manager)


if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
