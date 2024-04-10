import functools
from PySide6.QtWidgets import QMessageBox

def admin_access(slot_function):
    @functools.wraps(slot_function)
    def wrapper(self, *args, **kwargs):
        if self.state["user_type"] != "admin":
            self.show_message("Access Denied", "Admin access required!")
            return
        return slot_function(self, *args, **kwargs)
    return wrapper
