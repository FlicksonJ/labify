from PySide6.QtCore import QAbstractTableModel, QSortFilterProxyModel, Qt
from PySide6.QtGui import QValidator
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtWidgets import QMessageBox, QLineEdit

import sys
from datetime import datetime
from thefuzz import fuzz
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle



# Check whether the input is upper case or digits
class UpperCaseNumValidator(QValidator):
    def validate(self, arg__1: str, arg__2: int) -> object:
        if arg__1.isupper() or arg__1.isdigit():
            return QValidator.Acceptable, arg__1, arg__2
        elif arg__1 == "":
            return QValidator.Intermediate, arg__1, arg__2
        else:
            return QValidator.Invalid, arg__1, arg__2


def get_time() -> str:
    current_time = datetime.now().strftime("%I:%M %p")
    return current_time

def get_date() -> str:
    current_date = datetime.now().strftime("%d %b, %Y")
    return current_date

def show_message(title: str, message: str):
    message_box = QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setText(message)
    message_box.exec()

def show_dialog(title: str, message: str):
    message_box = QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setText(message)
    message_box.setIcon(QMessageBox.Question)
    message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    return message_box.exec()

def validate_line_edit(line_edit: QLineEdit, error_message: str = "") -> bool:
    # custom style sheets
    error_stylesheet = "QLineEdit:focus {border: 1px solid red;}"
    normal_stylesheet = ""
        
    text = line_edit.text()
    if not text:
        if error_message != "":
            show_message("Error", error_message)

        line_edit.setStyleSheet(error_stylesheet)
        line_edit.setFocus()
        return False
    else:
        line_edit.setStyleSheet(normal_stylesheet)
    return True

def fuzzy_search(model: QAbstractTableModel, search_term: str) -> QSortFilterProxyModel | None:
    proxy_model = QSortFilterProxyModel()
    proxy_model.setSourceModel(model)

    filtered_rows = []
    for row in range(proxy_model.rowCount()):
        name_index = model.index(row, 1)
        name = model.data(name_index)
        similiarity = fuzz.partial_token_sort_ratio(search_term.lower(), name.lower())
        if similiarity > 70:
            # value of row starts from 0 but cid of table starts from 1
            filtered_rows.append(row+1)

    if len(filtered_rows) < 1:
        return None
    proxy_model.setFilterKeyColumn(0)
    proxy_model.setFilterFixedString("")
    proxy_model.setFilterRegularExpression("")
    regex_pattern = "|".join(map(str, filtered_rows))
    proxy_model.setFilterRegularExpression(f"^(?:{regex_pattern})$")

    return proxy_model

def create_pdf(title: str, file_path: str, model: QSqlQueryModel) -> None:
    if not file_path.endswith('.pdf'):
        file_path = file_path + '.pdf'
    pdf = canvas.Canvas(file_path, pagesize=A4)
    pdf.setTitle(title)
    width, height = A4
    margin = 50
    line_height = 20
    table_start_y = height - margin
    max_rows_per_page = int((table_start_y - margin) / line_height) - 1

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])
    
    headers = [model.headerData(i, Qt.Horizontal) for i in range(model.columnCount())]
    data = []
    for row in range(model.rowCount()):
        row_data = [model.index(row, col).data() for col in range(model.columnCount())]
        data.append(row_data)

    for i in range(0, len(data), max_rows_per_page):
        chunk = [headers] + data[i:i + max_rows_per_page]
        table = Table(chunk)
        table.setStyle(table_style)
        table_width, table_height = table.wrap(0, 0)
        x_position = (width - table_width) / 2

        table.drawOn(pdf, x_position, table_start_y - line_height * len(chunk))

        page_num = int(i / max_rows_per_page) + 1
        pdf.drawString(width - margin, margin / 2, f"Page {page_num}")
        pdf.showPage()

    pdf.save()
    print("PDF generated:", file_path)

