import functools
from PySide6.QtWidgets import QMessageBox
from app import utils

def admin_access(slot_function):
    @functools.wraps(slot_function)
    def wrapper(self, *args, **kwargs):
        if self.state["user_type"] != "admin":
            utils.show_message("Access Denied", "Admin access required!")
            return
        return slot_function(self, *args, **kwargs)
    return wrapper


def restrict_page_change(slot_function):
    """
    To restrict the user from changing the page if they are in the middle
    of add/update/delete item from the inventory.
    """
    @functools.wraps(slot_function)
    def wrapper(self):
        page = self.state["inventory_page_func"]
        if page == "add":
            self.ui.item_manage.buttons()[0].setChecked(True)
        if page == "update":
            self.ui.item_manage.buttons()[1].setChecked(True)
        if page == "delete":
            self.ui.item_manage.buttons()[2].setChecked(True)
        if page != "search":
            utils.show_message("Error", "Press Cancel/Save before changing page")
            return
        return slot_function(self)
    return wrapper
