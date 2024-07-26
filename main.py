#!/usr/bin/python3
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCoreApplication

from app.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    QCoreApplication.setApplicationName("Labify")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
