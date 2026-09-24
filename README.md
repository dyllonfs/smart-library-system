# Smart Library Management System

A menu-driven **Library Management System built with Python** for managing library items, members, borrowing transactions, and saved library data.

This project was developed as a group assignment for **MCD4710 Introduction to Programming** and demonstrates the application of object-oriented programming, file handling, input validation, and basic data management.

## Features

### Staff
- Add library items
- Edit existing items
- Delete items
- View all library items sorted by title
- Save library data

### Members
- Register new library members
- Borrow available items
- Return borrowed items
- View available items
- View currently borrowed items

### Library Items
The system supports three types of library items:
- **Printed Books** — author and page count
- **E-Books** — file size and file format
- **Magazines** — issue number and publication date

### Borrowing
- Tracks the member and item involved in each transaction
- Records borrow and return dates
- Updates item availability when items are borrowed or returned
- Uses different borrowing durations for different item types

## Programming Concepts

This project applies several core Python and object-oriented programming concepts:

- **Object-Oriented Programming (OOP)**
- Classes and objects
- **Encapsulation** using private attributes
- **Inheritance** through specialised library item classes
- **Polymorphism** through overridden methods such as `get_borrow_duration()` and `__str__()`
- **Abstraction** using Python's `ABC` and `abstractmethod`
- Constructors and getter/setter methods
- Lists and iteration
- Conditional logic and loops
- Exception handling
- Input validation
- File handling and data persistence

## Technologies

- **Python 3**
- Python standard library:
  - `abc`
  - `datetime`
- Git & GitHub

No external Python packages are required.

## Project Structure

```text
smart-library-system/
│
├── main(Final Group Code).py   # Final group implementation
├── RevisedPrototype.py         # Earlier/revised prototype
│
├── library_items.txt           # Saved library item data
├── members.txt                 # Saved member data
├── borrow_records.txt          # Saved borrowing records
│
├── UMLandClassDiagrams.pdf     # UML and class diagrams
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/dyllonfs/smart-library-system.git
cd smart-library-system
```

### 2. Run the final program

Because the final source file contains spaces and parentheses in its filename, use:

```bash
python "main(Final Group Code).py"
```

### 3. Use the menu

The program starts with:

```text
=== MAIN MENU ===
1. Staff
2. Member
3. Exit
```

Select a role and follow the prompts to interact with the system.

## Data Persistence

The system uses text files to save and load data:

- `library_items.txt`
- `members.txt`
- `borrow_records.txt`

The **Save All Data** option writes the current library information, members, and borrowing records to these files.

## Borrowing Durations

Different library item types have different maximum borrowing durations:

| Item Type | Borrowing Duration |
|---|---:|
| Printed Book | 14 days |
| E-Book | 7 days |
| Magazine | 3 days |

## Class Design

The main class structure includes:

- `LibraryItem` — abstract base class for library resources
- `PrintedBook` — represents printed books
- `EBook` — represents electronic books
- `Magazine` — represents magazines
- `Member` — represents registered library members
- `BorrowRecord` — stores borrowing transaction information
- `Staff` — provides library inventory management operations

The UML and class diagrams are available in **UMLandClassDiagrams.pdf**.

## Project Context

**Course:** MCD4710 Introduction to Programming  
**Project:** Assignment 2 — Group Project  
**Language:** Python

This project was created to apply programming fundamentals and object-oriented programming concepts to a practical library management scenario.

## Authors

- Alexander Nathanel Chung
- Angad Singh Sawhney
- Dyllon Fellix Suhamdy
- Nathan Oliver Tjan
