import tkinter as tk

class ActivityLogWindow(tk.Toplevel):
    """
    Simple window that displays the activity log from DataManager.
    """
    def __init__(self, master, data_manager):
        super().__init__(master)
        self.title("Activity Log")
        self.geometry("600x400")
        self.data_manager = data_manager

        self.text_area = tk.Text(self, width=80, height=24)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        # populate log
        self._refresh()

    def _refresh(self):
        self.text_area.delete("1.0", tk.END)
        for msg in self.data_manager.activity_log:
            self.text_area.insert(tk.END, msg + "\n")
