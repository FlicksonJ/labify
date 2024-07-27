from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit


class UppercaseLineEdit(QLineEdit):
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.text():
            new_text = event.text().upper()
            new_event = QKeyEvent(event.type(), event.key(), event.modifiers(), new_text)
            super().keyPressEvent(new_event)
        else:
            super().keyPressEvent(event)
