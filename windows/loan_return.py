# windows/loans.py

import tkinter as tk
from tkinter import messagebox

class LoansWindow(tk.Toplevel):
    """
    A window for handling book loans and returns.
    """

    def __init__(self, master, data_manager):
        """
        Initializes the loans window.
        :param master: main window or parent
        :param data_manager: instance of DataManager
        """
        super().__init__(master)
        self.title("Prestamos y devoluciones")
        self.geometry("350x250")
        self.data_manager = data_manager

        # === Widgets ===
        self.label_user_id = tk.Label(self, text="ID del usuario:")
        self.entry_user_id = tk.Entry(self)

        self.label_book_id = tk.Label(self, text="ID del libro:")
        self.entry_book_id = tk.Entry(self)

        self.button_loan = tk.Button(self, text="Solicitar prestamo de libros", command=self.loan_book)
        self.button_return = tk.Button(self, text="Regresar prestamo de libros", command=self.return_book)

        # === Layout ===
        self.label_user_id.pack(pady=5)
        self.entry_user_id.pack(pady=5)
        self.label_book_id.pack(pady=5)
        self.entry_book_id.pack(pady=5)
        self.button_loan.pack(pady=10)
        self.button_return.pack(pady=5)

    def loan_book(self):
        """
        Loans a book to a user if available.
        """
        isbn = self.entry_book_id.get()

        success = self.data_manager.loan_book(isbn)
        if success:
            messagebox.showinfo("Success", "Se realizo el prestamo correctamente")
        else:
            messagebox.showerror("Error", "No encotramos el libro, puede estar ya en solicitud de prestamo")
            

    def return_book(self):
        """
        Returns a book from a user.
        """
        user_id = self.entry_user_id.get()
        book_id = self.entry_book_id.get()

        if self.data_manager.return_book(user_id, book_id):
            messagebox.showinfo("Success", "Se relizado entrega del libro")
        else:
            messagebox.showerror("Error", "No se ha encontrado prestamos a tu nombre de id, revisa que los campos correspondan")
        

