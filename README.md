# Labify - Chemistry Inventory Management System

The **Labify** software is used to keep track of inventories in chemistry labs.<br>
It is a Python-based inventory management system.<br>
It helps lab managers keep track of their inventory of glassware, chemicals, and equipments.

<p align="center">
 <img src="images/labify.jpeg" alt="Labify Logo" width="200px">
</p>

## Features

- Track inventory levels
- Manage glassware, chemical and equipment stock. <br>
  *(Management: Add, Edit, Remove)*
- Track transaction history.

## Installation

To install Labify, follow these steps:

1. Clone the repository:
```
git clone git@github.com:cslynx/labify.git
```
2. Install dependencies:
```
pip install pyside6
pip install bcrypt
pip install itsdangerous
pip install thefuzz
``` 
3. Run the application:
```
cd labify
python3 main.py
```

## Usage

Labify provides a user-friendly interface for managing your lab inventory. Simply launch the application and start adding, updating, or removing items from your inventory.

## Acknowledgements

Labify was entirely developed using the Python programming language.<br>
The User Interface was developed using the Qt framework.<br>
Labify utilizes the following open-source Python libraries:
- PySide6
- bcrypt
- itsdangerous
- thefuzz

## TODO

Do all these if the current design is approved:
- [ ] Remove item_entry list view and ui file
- [ ] Remove deactivate and activate page change functions
- [ ] Remove save button from add entry page
- [ ] Remove restrict_page_change access control
- [ ] Remove unnecessary comments in the code

Otherwise switch all the changed features to the previous one.

