"""
Assessment Details: MCD4710 Introduction to Programming - Assignment 2 Group code (final program)
Group Members:
Alexander Nathanel Chung (Student ID: 37745379)
Angad Singh Sawhney (Student ID: 36726443)
Dyllon Fellix Suhamdy (Student ID: 37745395)
Nathan Oliver Tjan (Student ID: 36726877)

"""
"""
Purpose:
This program implements a menu-driven Smart Library Management System.
It allows staff to manage library items and members to register, borrow,
return, and view library items. The program uses object-oriented programming,
inheritance, polymorphism, encapsulation, and file handling to manage and
store library data.
"""

from abc import ABC, abstractmethod
from datetime import date
class LibraryItem(ABC):
    """Represents a library item."""
    def __init__(self, item_id, title, item_type, status="Available"):
        """
        Initialize a library item.

        Inputs/Parameters: 
        item_id: The unique ID of the library item. 
        title: The title of the library item. 
        item_type: The type of library item. 
        status: The current status of the item.

        Output: 
        None. Initializes the library item's attributes.
        """
        self.__item_id = item_id       # Unique ID identifier
        self.__title = title           # Material title
        self.__status = status         # Material status: 'Available' or 'Borrowed'
        self.__type = item_type

    def get_item_id(self):
        """
        Return the library item's ID.
        
        Inputs/Parameters:
        None 

        Output:
        The unique ID of the library item
        """
        return self.__item_id

    def get_title(self):
        """
        Return the library item's title.
        
        Inputs/Parameters: 
        None 

        Output:
        The title of the library item
        """
        return self.__title

    def get_status(self):
        """
        Return the library item's status.
        
        Inputs/Parameters: 
        None 

        Output: 
        The current status of the library item
        
        """
        return self.__status

    def get_type(self):
        """
        Return the library item's type.

        Inputs/Parameters:
        None
         
        Output:
        The type of the library item
        """
        return self.__type

    def set_item_id(self, new_item_id):
        """
        Update the library item's ID.
        
        Inputs/Parameters: 
        new_item_id: The new ID to assign to the library item
        
        Output: 
        None. Updates the item's ID

        """
        self.__item_id = new_item_id

    def set_title(self, new_title):
        """
        Update the library item's title.
        
        Inputs/Parameters:
        new_title: The new title to assign to the library item
         
        Output:
        None. Updates the item's title
        """
        self.__title = new_title

    def set_type(self, new_type):
        """
        Update the library item's type.
        
        Inputs/Parameters:
        new_type: The new type to assign to the library item
        
        Output:
        None. Updates the item's type
        """
        self.__type = new_type

    def set_status(self, new_status):
        """
        Update the library item's status.
        
        Inputs/Parameters:
        new_status: The new status to assign to the library item

        Output:
        None. Updates the item's status
        """
        self.__status = new_status

    @abstractmethod
    def get_borrow_duration(self):
        """
        Return the borrowing duration for a library item.
        
        Inputs/Parameters:
        None
        
        Output:
        The maximum borrowing duration for the library item 
        """
        pass

    def __str__(self):
        """
        Return the library item's details as a string.
        
        Inputs/Parameters:
        None
        
        Output:
        A string containing the item's ID, title, type, and status

        """
        return (f"ID: {self.__item_id}, Title: {self.__title}, Type: {self.__type}, Status: {self.__status}")


class PrintedBook(LibraryItem):
    """Represents a printed book in the library."""

    def __init__(self, item_id, title, author, number_of_pages, status="Available"):
        """
        Initialize a printed book.
        
        Inputs/Parameters:
        item_id: The unique ID of the printed book
        title: The title of the printed book
        author: The author of the printed book
        number_of_pages: The number of pages in the book
        status: The current status of the book 
        
        Output:
        None. Initializes the printed book's attributes
        """

        super().__init__(
            item_id,
            title,
            "Printed Book",
            status
        )

        self.__author = author
        self.__number_of_pages = number_of_pages

    def get_author(self):
        """
        Return the book's author.
        
        Inputs/Parameters:
        None
 
        Output:
        The author of the printed book
        """
        return self.__author

    def get_number_of_pages(self):
        """
        Return the number of pages in the book.
        
        Inputs/Parameters:
        None
        
        Output:
        The number of pages in the printed book
        """
        return self.__number_of_pages

    def set_author(self, new_author):
        """
        Update the book's author.
        
        Inputs/Parameters:
        new_author: The new author of the printed book
        
        Output:
        None. Updates the book's author
        """
        self.__author = new_author

    def set_number_of_pages(self, new_number_of_pages):
        """
        Update the number of pages in the book.
        
        Inputs/Parameters:
        new_number_of_pages: The new number of pages
        
        Output:
        None. Updates the number of pages
        """
        self.__number_of_pages = new_number_of_pages

    def get_borrow_duration(self):
        """
        Return the borrowing duration for a printed book.

        Inputs/Parameters:
        None
        
        Output:
        14, representing the maximum borrowing duration in days
        """
        Printed_Book_Borrow_Duration = 14 
        return Printed_Book_Borrow_Duration

    def __str__(self):
        """
        Return all details of the printed book.
        
        Inputs/Parameters:
        None
        
        Output:
        A string containing the book's ID, title, type, status,
        author, and number of pages
        """
        return (f"{super().__str__()}, Author: {self.__author}, Pages: {self.__number_of_pages}")


class EBook(LibraryItem):
    """Represents an electronic book in the library."""

    def __init__(self, item_id, title, file_size, file_format,status="Available"):
        """
        Initialize an ebook.
        
        Inputs/Parameters:
        item_id: The unique ID of the e-book
        title: The title of the e-book
        file_size: The size of the e-book file
        file_format: The format of the e-book file
        status: The current status of the e-book
        
        Output:
        None. Initializes the e-book's attributes
        """
        super().__init__(item_id,title,"EBook",status)
        self.__file_size = file_size
        self.__format = file_format

    def get_file_size(self):
        """
        Return the file size.
        
        Inputs/Parameters:
        None
        
        Output:
        The file size of the e-book
        """
        return self.__file_size

    def get_format(self):
        """
        Return the e-book format.

        Inputs/Parameters:
        None
        
        Output:
        The file format of the e-book
        """
        return self.__format

    def set_file_size(self, new_file_size):
        """
        Change the file size.
        
        Inputs/Parameters:
        new_file_size: The new file size of the e-book
        
        Output:
        None. Updates the e-book's file size
        """
        self.__file_size = new_file_size

    def set_format(self, new_file_format):
        """
        Change the e-book format.
        
        Inputs/Parameters:
        new_file_format: The new format of the e-book
        
        Output:
        None. Updates the e-book's file format
        """
        self.__format = new_file_format

    def get_borrow_duration(self):
        """
        Return the borrowing duration for an e-book.
        
        Inputs/Parameters:
        None
        
        Output:
        7, representing the maximum borrowing duration in days
        """
        Ebook_Borrow_Duration = 7
        return Ebook_Borrow_Duration

    def __str__(self):
        """
        Return all details of the e-book.
        
        Inputs/Parameters:
        None
        
        Output:
        A string containing the e-book's ID, title, type, status,
        file size, and file format
        """
        return (f"{super().__str__()}, File Size: {self.__file_size}, Format: {self.__format}")


class Magazine(LibraryItem):
    """Represents a magazine in the library."""

    def __init__(self, item_id, title, issue_number,publication_date, status="Available"):
        """
        Initialize a magazine.

        Inputs/Parameters:
        item_id: The unique ID of the magazine
        title: The title of the magazine
        issue_number: The issue number of the magazine
        publication_date: The publication date of the magazine
        status: The current status of the magazine
    
        Output:
        None. Initializes the magazine's attributes
        """
        super().__init__(item_id,title,"Magazine",status)
        self.__issue_number = issue_number
        self.__publication_date = publication_date

    def get_issue_number(self):
        """
        Return the magazine issue number.
        
        Inputs/Parameters:
        None

        Output:
        The issue number of the magazine
        """
        return self.__issue_number

    def get_publication_date(self):
        """
        Return the publication date.
        
        Inputs/Parameters:
        None

        Output:
        The publication date of the magazine
        """
        return self.__publication_date

    def set_issue_number(self, new_issue_number):
        """
        Change the issue number.
        
        Inputs/Parameters:
        new_issue_number: The new issue number of the magazine

        Output:
        None. Updates the magazine's issue number
        """
        self.__issue_number = new_issue_number

    def set_publication_date(self, new_publication_date):
        """
        Change the publication date.
        
        Inputs/Parameters:
        new_publication_date: The new publication date of the magazine

        Output:
        None. Updates the magazine's publication date
        """
        self.__publication_date = new_publication_date

    def get_borrow_duration(self):
        """
        Return the borrowing duration for a magazine.
        
        Inputs/Parameters:
        None

        Output:
        3, representing the maximum borrowing duration in days
        """
        Magazine_Borrow_Duration = 3 
        return Magazine_Borrow_Duration

    def __str__(self):
        """
        Return all details of the magazine.
        
        Inputs/Parameters:
        None
        
        Output:
        A string containing the magazine's ID, title, type, status,
        issue number, and publication date
        """
        return (f"{super().__str__()}, Issue Number: {self.__issue_number}, Publication Date: {self.__publication_date}")


class Member:
    """Represents a registered library member."""

    def __init__(self, member_name, contact_number):
        """
        Initialize a library member.

        Input/Parameters:
        member_name (str): The full name of the member.
        contact_number (str): The member's contact number.

        Output:
        None
        """
        self.__member_name = member_name
        self.__contact_number = contact_number
        self.__borrowed_items_list = []

    def get_member_name(self):
        """
        Return the member's name.

        Input/Parameters:
        None

        Output:
        returns str: The name of the member.
        """
        return self.__member_name

    def get_contact_number(self):
        """
        Return the member's contact number.

        Input/Parameters:
        None

        Output:
        returns str: The contact number of the member.
        """
        return self.__contact_number

    def get_borrowed_items_list(self):
        """
        Return the list of items currently borrowed.

        Input/Parameters:
        None

        Output:
        returns list: A list of LibraryItem objects borrowed by the member.
        """
        return self.__borrowed_items_list

    def set_member_name(self, new_member_name):
        """
        Change the member's name.

        Input/Parameters:
        new_member_name (str): The new name to assign.

        Output:
        None
        """
        self.__member_name = new_member_name

    def set_contact_number(self, new_contact_number):
        """
        Change the member's contact number.

        Input/Parameters:
        new_contact_number (str): The new contact number to assign.

        Output:
        None
        """
        self.__contact_number = new_contact_number

    def borrow_item(self, item):
        """
        Borrow an available library item.

        Input/Parameters:
        item (LibraryItem): The item object to borrow.

        Output:
        returns bool: True if successfully borrowed, False otherwise.
        """
        if item.get_status() == "Available":
            self.__borrowed_items_list.append(item)
            item.set_status("Borrowed")
            return True
        return False

    def return_item(self, item):
        """
        Return an item currently borrowed by the member.

        Input/Parameters:
        item (LibraryItem): The item object to return.

        Output:
        returns bool: True if found and returned, False otherwise.
        """
        item_found = False
        updated_list = []
        
        for current_item in self.__borrowed_items_list:
            # Remove the returned item while keeping all other borrowed items
            if current_item == item and item_found == False:
                item_found = True
                item.set_status("Available")
            else:
                updated_list.append(current_item)
        
        if item_found == True:
            self.__borrowed_items_list = updated_list
            return True
        return False

    def __str__(self):
        """
        Return the member's details.

        Input/Parameters:
        None

        Output:
        returns str: A formatted string containing the member's name, contact, and list of borrowed items.
        """
        borrowed_items = ""
        for item in self.__borrowed_items_list:
            borrowed_items = borrowed_items + item.get_title() + ", "

        if borrowed_items == "":
            borrowed_items = "None"

        return ("Name: " + self.__member_name + ", Contact: " + self.__contact_number + ", Borrowed Items: " + borrowed_items)


class BorrowRecord:
    """Stores information about one borrowing transaction."""

    def __init__(self, member, item, borrow_date, return_date=None):
        """
        Initialize a borrowing record.

        Input/Parameters:
        member (Member): The member borrowing the item.
        item (LibraryItem): The item being borrowed.
        borrow_date (date): The date the item was borrowed.
        return_date (date, optional): The date the item was returned. Defaults to None.

        Output:
        None
        """
        self.__member = member
        self.__item = item
        self.__borrow_date = borrow_date
        self.__return_date = return_date

    def get_member(self):
        """
        Return the member involved in the borrowing.

        Input/Parameters:
        None

        Output:
        returns Member: The member object associated with this record.
        """
        return self.__member

    def get_item(self):
        """
        Return the borrowed library item.

        Input/Parameters:
        None

        Output:
        returns LibraryItem: The item object associated with this record.
        """
        return self.__item

    def get_borrow_date(self):
        """
        Return the borrowing date.

        Input/Parameters:
        None

        Output:
        returns date: The date the item was borrowed.
        """
        return self.__borrow_date

    def get_return_date(self):
        """
        Return the return date.

        Input/Parameters:
        None

        Output:
        returns date or None: The return date if returned, else None.
        """
        return self.__return_date

    def set_member(self, new_member):
        """
        Change the member associated with the record.

        Input/Parameters:
        new_member (Member): The new member to assign.

        Output:
        None
        """
        self.__member = new_member

    def set_item(self, new_item):
        """
        Change the item associated with the record.

        Input/Parameters:
        new_item (LibraryItem): The new library item to assign.

        Output:
        None
        """
        self.__item = new_item

    def set_borrow_date(self, new_borrow_date):
        """
        Change the borrowing date.

        Input/Parameters:
        new_borrow_date (date): The new borrow date.

        Output:
        None
        """
        self.__borrow_date = new_borrow_date

    def set_return_date(self, new_return_date):
        """
        Record or change the return date.

        Input/Parameters:
        new_return_date (date): The new return date.

        Output:
        None
        """
        self.__return_date = new_return_date

    def __str__(self):
        """
        Return the borrowing record details.

        Input/Parameters:
        None

        Output:
        returns str: A formatted string showing member, item, and transaction dates.
        """
        return (f"Member: {self.__member}, Item: {self.__item}, Borrow Date: {self.__borrow_date}, Return Date: {self.__return_date}")


class Staff:
    """Represents a staff member who manages library inventory."""

    def __init__(self, staff_id, staff_name):
        """
        Initialize a staff member.
        
        Input/Parameters:
        staff_id (str): The staff id provided to the function.
        staff_name (str): The staff name provided to the function.
        
        Output:
        No direct return value. Performs the requested operation.
        """
        self.__staff_id = staff_id
        self.__staff_name = staff_name


    def get_staff_id(self):
        """
        Return the staff ID.

        Input/Parameters:
        None
        
        Output:
        returns the requested value.
        """
        return self.__staff_id


    def get_staff_name(self):
        """
        Return the staff name.
        
        Input/Parameters:
        None
        
        Output:
        returns the requested value.
        """
        return self.__staff_name


    def set_staff_id(self, new_staff_id):
        """
        Change the staff ID.
        
        Input/Parameters:
        new_staff_id (str): The new staff id provided to the function.
        
        Output:
        No direct return value. Updates the corresponding attribute.
        """
        self.__staff_id = new_staff_id


    def set_staff_name(self, new_staff_name):
        """
        Change the staff name.
         
        Input/Parameters:
        new_staff_name (str): The new staff name provided to the function.
        
        Output:
        No direct return value. Updates the corresponding attribute.
        """
        self.__staff_name = new_staff_name


    def add_item(self, item_list, item):
        """
        Add a new item if its ID does not already exist.

        Input/Parameters:
        item_list (list): The current list of library items.
        item (LibraryItem): The new item object to be added.
        
        Output:
        returns bool: True if the item was added, False if the ID already exists.
        
        """
        for existing_item in item_list:
            if existing_item.get_item_id() == item.get_item_id():
                return False

        item_list.append(item)
        return True


    def edit_item(self, item_list, item_id):
        """
        Find an item by ID and edit selected details.
        
        Input/Parameters:
        item_list (list): The item list provided to the function.
        item_id (str): The item id provided to the function.
        
        Output:
        returns LibraryItem or None: The matching item, or None if not found.
        """
        for item in item_list:
            if item.get_item_id() == item_id:
                return item

        return None


    def delete_item(self, item_list, item_id):
        """
        Delete an item using its item ID.
        
        Input/Parameters:
        item_list (list): The item list provided to the function.
        item_id (str): The item id provided to the function.

        Output:
        returns bool: True if the operation succeeds, otherwise False.
        
        """
        for item in item_list:
            if item.get_item_id() == item_id:
                item_list.remove(item)
                return True

        return False

    def view_all_items(self, item_list):
        """
        Return all library items sorted by title.
        
        Input/Parameters:
        item_list (list): The item list provided to the function.
        
        Output:
        returns list: Library items sorted by title.
        """
        # Create a copy so sorting does not change the original item list
        item_list_sorted = item_list[:]

        #Return library items sorted by title using Lexicographic ordering.

        for item in item_list_sorted: 
            for index in range (len(item_list_sorted)-1): 
                # Compare titles alphabetically with case insensitivity
                title1 = item_list_sorted[index].get_title().lower()
                title2 = item_list_sorted[index+1].get_title().lower() 
                
                if title1 > title2: 
                    # Swap elements if current item belongs after next item
                    temp = item_list_sorted[index]
                    item_list_sorted[index] = item_list_sorted[index+1]
                    item_list_sorted[index+1] = temp
        return item_list_sorted

    
    def save_data(self, item_list, filename):
        """
        Save library item information into a text file.
        
        Input/Parameters:
        item_list (list): The item list provided to the function.
        filename (str): The filename provided to the function.
        
        Output:
        returns bool: True if the data is saved successfully, otherwise False
        """
        try:
            file = open(filename, "w")

            for item in item_list:

                if item.get_type() == "Printed Book":
                    file.write(item.get_type() + "," +
                        item.get_item_id() + "," +
                        item.get_title() + "," +
                        item.get_status() + "," +
                        item.get_author() + "," +
                        str(item.get_number_of_pages()) + "\n")

                elif item.get_type() == "EBook":
                    file.write(item.get_type() + "," +
                        item.get_item_id() + "," +
                        item.get_title() + "," +
                        item.get_status() + "," +
                        item.get_file_size() + "," +
                        item.get_format() + "\n")

                elif item.get_type() == "Magazine":
                    file.write(item.get_type() + "," +
                        item.get_item_id() + "," +
                        item.get_title() + "," +
                        item.get_status() + "," +
                        item.get_issue_number() + "," +
                        item.get_publication_date() + "\n")

            file.close()

        except OSError: 
            return False 
        else:
            return True


    def __str__(self):
        """
        Return the staff member's details.
        
        Input/Parameters:
        None
        
        Output:
        returns str: A formatted string containing the object's details
        """
        return f"Staff ID: {self.__staff_id}, Staff Name: {self.__staff_name}"



#----------------------- MAIN MENU -------------------
def main_menu(): 
    """
    Display the main menu and redirects the user to the Staff or Member menu, or exit the program.
    Input/Parameters:
    None
        
    Output:
    No direct return value. Performs the requested operation.
    """
    while True: 
        confirmed_exit = False 
        print()
        print("=== MAIN MENU ===")
        print("1. Staff")
        print("2. Member")
        print("3. Exit")
        main_menu_input = input("Select role: ")

        if main_menu_input == "1": 
            staff_menu()
        elif main_menu_input == "2": 
            member_menu()
        elif main_menu_input == "3":
            while True: 
                exit_confirmation = input("Are you sure you want to exit (y/n)? ")
                if exit_confirmation == "y": 
                    print("Exiting program...")
                    confirmed_exit = True 
                    break 
                elif exit_confirmation =="n": 
                    break 
                else: 
                    print("Invalid Input")
                    continue  
            if confirmed_exit == True: 
                break 
        else: 
            print("Invalid Choice")
            continue 

item_list = []
members = []
borrow_records = []
staff = Staff("S001", "Nathan")

#--------------- STAFF MENU ---------------------
def staff_menu():
    """
    Displays the staff menu and allows staff to manipulate or view the library item info
    
    Input/Parameters:
    None
    
    Output:
    No direct return value. Performs the requested operation.
    """
    while True: 
        print()
        print("--- STAFF MENU ---")
        print("1. Add Item")
        print("2. Edit Item")
        print("3. Delete Item")
        print("4. View All Items")
        print("5. Save All Data")
        print("6. Back")
        staff_menu_input = input("Enter choice: ")

        if staff_menu_input == "1": 
            add_item()
        elif staff_menu_input== "2": 
            edit_item()
        elif staff_menu_input == "3": 
            delete_item()
        elif staff_menu_input =="4": 
            view_all_items()
        elif staff_menu_input == "5": 
            save_data()
        elif staff_menu_input =="6": 
            return 
        else: 
            print("Invalid Choice")
            continue 
                

def add_item(): 
    """
    asks staff for the new library item details and adds it into the item list
    
    Input/Parameters:
    None
    
    Output:
    returns bool: True if the operation succeeds, otherwise False.
    """
    print()
    print("Add Item: ")

    item_type = input("Enter type (book/ebook/magazine): ").lower()

    if item_type == "book":
        item_id = input("Enter ID: ")
        if item_id == "":
            print("INVALID. CANNOT BE LEFT EMPTY ")
            return
        title = input("Enter Title: ")
        if title == "":
            print("INVALID. CANNOT BE LEFT EMPTY ")
            return
        author = input("Enter Author: ")
        if author == "":
            print("INVALID. CANNOT BE LEFT EMPTY ")
            return
        try:
            number_of_pages = int(input("Enter Pages: "))
        except ValueError:
            print("INVALID INPUT. PAGES MUST BE A NUMBER.")
            return

        new_item = PrintedBook(item_id,title,author,number_of_pages)

    elif item_type == "ebook":
        item_id = input("Enter ID: ")
        if item_id == "":
            print("INVALID. CANNOT BE LEFT EMPTY ")
            return
        title = input("Enter Title: ")
        if title == "":
            print("INVALID. CANNOT BE LEFT EMPTY ")
            return
        file_size = input("Enter Size: ")
        if file_size == "":
            print("INVALID. CANNOT BE LEFT EMPTY ")
            return
        file_format = input("Enter Format (PDF/EPUB): ").upper()
        if file_format != "PDF" and file_format != "EPUB":
            print("INVALID FORMAT.")
            return

        new_item = EBook(item_id,title,file_size,file_format)

    elif item_type == "magazine":
        item_id = input("Enter ID: ")
        if item_id == "":
            print("INVALID. CANNOT BE LEFT EMPTY ")
            return
        title = input("Enter Title: ")
        if title == "":
            print("INVALID. CANNOT BE LEFT EMPTY ")
            return
        issue_number = input("Enter Issue Number: ")
        if issue_number == "":
            print("INVALID. CANNOT BE LEFT EMPTY ")
            return
        publication_date = input("Enter Publication Date: ")
        if publication_date == "":
            print("INVALID. CANNOT BE LEFT EMPTY ")
            return

        new_item = Magazine(item_id,title,issue_number,publication_date)

    else:
        print("INVALID ITEM TYPE.")
        return

    if staff.add_item(item_list, new_item) == True:
        print("Item added successfully")
    else:
        print("Item ID already exists")
    

def edit_item(): 
    """
    searches the specified item by its id, displays the details and edits the details wanted by the staff
    
    Input/Parameters:
    None
    
    Output:
    returns LibraryItem or None: The matching item, or None if not found.
    """
    print()
    print("Edit Item:")
    print()
    print("All available items: ")
    for item in item_list:
            if item.get_status() == "Available":
                print(item)

    item_id = input("Enter item ID to edit: ")

    selected_item = staff.edit_item(item_list, item_id)

    if selected_item is None:
        print("ITEM NOT FOUND")
        return

    print()
    print("Current Details:")
    print(selected_item)

    item_type = selected_item.get_type()

    print()
    print("Select detail to edit:")
    print("1. Title")

    if item_type == "Printed Book":
        print("2. Author")
        print("3. Number of Pages")

    elif item_type == "EBook":
        print("2. File Size")
        print("3. Format")

    elif item_type == "Magazine":
        print("2. Issue Number")
        print("3. Publication Date")

    print("4. Back")

    choice = input("Enter choice: ")

    if choice == "1":
        new_title = input("Enter new title: ")
        selected_item.set_title(new_title)

    elif choice == "2":

        if item_type == "Printed Book":
            new_author = input("Enter new author: ")
            selected_item.set_author(new_author)

        elif item_type == "EBook":
            new_file_size = input("Enter new file size: ")
            selected_item.set_file_size(new_file_size)

        elif item_type == "Magazine":
            new_issue_number = input("Enter new issue number: ")
            selected_item.set_issue_number(new_issue_number)

    elif choice == "3":

        if item_type == "Printed Book":
            try:
                new_number_of_pages = int(
                    input("Enter new number of pages: ")
                )
                selected_item.set_number_of_pages(new_number_of_pages)

            except ValueError:
                print("INVALID INPUT. PAGES MUST BE A NUMBER.")
                return

        elif item_type == "EBook":
            new_format = input("Enter new format (PDF/EPUB): ").upper()

            if new_format == "PDF" or new_format == "EPUB":
                selected_item.set_format(new_format)
            else:
                print("INVALID FORMAT.")
                return

        elif item_type == "Magazine":
            new_publication_date = input(
                "Enter new publication date: "
            )
            selected_item.set_publication_date(
                new_publication_date
            )

    elif choice == "4":
        return

    else:
        print("INVALID CHOICE")
        return

    print("Item updated successfully")
    

def delete_item():
    """
    searches an item by its id, and removes the item from the item list
    
    Input/Parameters:
    None
    
    Output:
    returns bool: True if the operation succeeds, otherwise False.
    """ 
    print()
    print("Delete Item:")

    item_id = input("Enter Item ID to delete: ")

    selected_item = None

    for item in item_list:
        if item.get_item_id() == item_id:
            selected_item = item

    if selected_item is None:
        print("ITEM NOT FOUND")
        return

    print("Found:", selected_item)

    confirmed_delete = False
    while True:
        delete_confirmation = input(
            "Are you sure you want to delete this item (y/n) ?"
        )

        if delete_confirmation == "y":
            confirmed_delete = True
            break

        elif delete_confirmation == "n":
            break

        else:
            print("INVALID INPUT")
            continue

    if confirmed_delete == True:
        if staff.delete_item(item_list, item_id) == True:
            print("Item deleted successfully")
        else:
            print("UNABLE TO DELETE ITEM")

def view_all_items(): 
    """
    displays all library items, with their id and other details in the item list sorted by title

    Input/Parameters:
    None
    
    Output:
    returns list: Library items sorted by title.
    """
    print()
    print("View All Items:")

    item_list_sorted = staff.view_all_items(item_list)

    if len(item_list_sorted) == 0:
        print("NO LIBRARY ITEMS FOUND")
        return

    for item in item_list_sorted:
        print(item)


#--------------------- MEMBER MENU ------------------------
def member_menu(): 
    """displays member menu and redirects users to register, borrow, return or view items"""
    while True: 
            print()
            print("--- MEMBER MENU ---")
            print("1. Register")
            print("2. Borrow Item")
            print("3. Return Item")
            print("4. View Available Items")
            print("5. View My Borrowed Items")
            print("6. Back")
            member_menu_input = input("Enter choice: ")

            if member_menu_input == "1": 
                register()
            elif member_menu_input== "2": 
                borrow_item()
            elif member_menu_input == "3": 
                return_item()
            elif member_menu_input =="4": 
                view_available_items()
            elif member_menu_input == "5": 
                view_my_borrowed_items()
            elif member_menu_input =="6": 
                return      
            else: 
                print("Invalid Choice")
                continue 

def register(): 
    """asks user for name and contact number and creates a new instance of a member"""
    member_name = input("Enter Name: ")
    if member_name == "":
        print("INVALID. CANNOT BE LEFT EMPTY ")
        return 
    contact_number = input("Enter Contact: ")
    if contact_number == "":
        print("INVALID. CANNOT BE LEFT EMPTY ")
        return 
        
    
    new_member = Member(member_name, contact_number)
    members.append(new_member)
    
    print("Member registered successfully.")

def borrow_item(): 
    """search for an available item by its id and assigns it to the member, whilst updating the item's status to borrowed """
    member_name = input("Enter your name: ")
    
    current_member = None
    for member in members:
        if member.get_member_name() == member_name:
            current_member = member
            break
            
    if current_member is None:
        print("Member not found")
        return

    print("--- Available Items ---")
    for item in item_list:
        if item.get_status() == "Available":
            print(item)
            
    item_id = input("Enter Item ID: ")
    
    selected_item = None
    for item in item_list:
        if item.get_item_id() == item_id:
            selected_item = item
            break
            
    if selected_item is None:
        print("Item not found")
        return
        
    if current_member.borrow_item(selected_item)== True: 
        borrow_date = date.today()

        new_borrow_record = BorrowRecord(current_member, selected_item,borrow_date)
        borrow_records.append(new_borrow_record)
        print("Item borrowed successfully")
    else:
        print("ITEM IS NOT AVAILABLE")


def return_item(): 
    """search for an item borrowed by its id from the member, and updates the item's status to available again """
    member_name = input("Enter your name: ")
    
    current_member = None
    for member in members:
        if member.get_member_name() == member_name:
            current_member = member
            break
            
    if current_member is None:
        print("Member not found")
        return

    print("\nYour Borrowed Items:")
    for item in current_member.get_borrowed_items_list():
        print(item)
            
    item_id = input("Enter Item ID to return: ")
    
    selected_item = None
    for item in current_member.get_borrowed_items_list():
        if item.get_item_id() == item_id:
            selected_item = item
            break
            
    if selected_item is None:
        print("Item not found")
        return
        
    if current_member.return_item(selected_item) == True:
        return_date = date.today()

        for record in borrow_records:
            if record.get_member() == current_member and record.get_item() == selected_item:
                if record.get_return_date() is None:
                    record.set_return_date(return_date)

        print("Item returned successfully")

    else:
        print("ITEM NOT RETURNED")


def view_available_items(): 
    """displays all library items that are currently available to be borrowed as a list with all the details"""
    print("--- Available Items ---")
    for item in item_list:
        if item.get_status() == "Available":
            print(item)

def view_my_borrowed_items(): 
    """displays all library items that are currently borrowed by a member with all its details"""
    member_name = input("Enter your name: ")
    
    current_member = None
    for member in members:
        if member.get_member_name() == member_name:
            current_member = member
            break
            
    if current_member is None:
        print("Member not found")
        return
        
    print("\n--- Your Borrowed Items ---")
    for item in current_member.get_borrowed_items_list():
        borrow_date = None

        for record in borrow_records:
            if record.get_member() == current_member and record.get_item() == item:
                if record.get_return_date() is None:
                    borrow_date = record.get_borrow_date()

        print("ID:", item.get_item_id(),"Title:", item.get_title(),"Borrow Date:", borrow_date)

#--------------------- FILE HANDLING ------------------------
def load_items(filename): 
    """
    Load saved library items from a text file.
    
    Input/Parameters:
    filename (str): The name or path of the file containing saved library items.

    Output:
    returns None: The function updates the global item_list with the loaded items.
    """
    try: 
        fileref_read = open(filename, "r")
        file_lines = fileref_read.readlines()
        for row in file_lines: 
            # Strip trailing whitespace or space and split line into a data list
            row = row.strip().split(",")
            try:
                item_type = row[0]
                item_id = row[1]
                title =  row[2]
                status = row[3] 
                if item_type == "Printed Book": 
                    author = row[4]
                    pages = int(row[5])
                    item_list.append(PrintedBook(item_id,title,author,pages,status))
                elif item_type == "EBook": 
                    file_size = row[4]
                    file_format = row[5]
                    item_list.append(EBook(item_id,title,file_size,file_format,status))
                elif item_type == "Magazine": 
                    issue_number = row[4]
                    pub_date = row[5]
                    item_list.append(Magazine(item_id,title,issue_number,pub_date,status))
                else: 
                    continue 
            except TypeError: 
                continue  
            except ValueError:
                print(f"Warning: Could not convert data type on row: {row}") 
                continue  
            except IndexError:
                print(f"Warning: Corrupted row with missing fields skipped: {row}") 
                continue 
        fileref_read.close()

    except FileNotFoundError: 
        print('NO SAVED ITEM LIST FOUND')
    except OSError: 
        print('ERROR IMPORTING ITEM LIST')

def save_data():
    """
    Save all current library data to their respective text files.

    Input/Parameters:
    None

    Output:
    returns None: Displays whether all library data was saved successfully.
    """

    items_saved = staff.save_data(item_list, "library_items.txt")
    members_saved = save_members("members.txt")
    borrow_records_saved = save_borrow_records("borrow_records.txt")

    if items_saved == True and members_saved == True and borrow_records_saved == True:
        print("Data saved successfully")

    else:
        print("ERROR SAVING DATA")

def save_members(filename):
    """
    Save registered members to a text file.
    
    Input/Parameters:
    filename (str): The name or path of the file where member data will be saved.

    Output:
    returns bool: True if the member data was saved successfully, False if an error occurred.
    """

    try:
        fileref_write = open(filename, "w")

        for member in members:
            fileref_write.write(
                member.get_member_name() + "," +
                member.get_contact_number() + "\n"
            )

        fileref_write.close()

    except OSError:
        return False

    else:
        return True

def load_members(filename):
    """
    Load saved member information from a text file into the members list.

    Input/Parameters:
    filename (str): The name or path of the file containing saved member data.

    Output:
    returns None: The function updates the global members list with the loaded members.
    """

    try:
        fileref_read = open(filename, "r")
        file_lines = fileref_read.readlines()

        for row in file_lines:
            row = row.strip().split(",")

            try:
                members.append(Member(row[0], row[1]))

            except IndexError:
                continue

        fileref_read.close()

    except FileNotFoundError:
        print("ERROR IMPORTING MEMBER LIST")

    except OSError:
        print("ERROR IMPORTING MEMBER LIST")

def save_borrow_records(filename):
    """
    Save all borrowing records to a text file.

    Input/Parameters:
    filename (str): The name or path of the file where borrow records will be saved.

    Output:
    returns bool: True if the borrow records were saved successfully, False if an error occurred.
    """

    try:
        fileref_write = open(filename, "w")

        for record in borrow_records:

            member = record.get_member()
            item = record.get_item()

            if record.get_return_date() is None:
                return_date = ""
            else:
                return_date = str(record.get_return_date())

            fileref_write.write(member.get_member_name() + "," +
                member.get_contact_number() + "," +
                item.get_item_id() + "," +
                str(record.get_borrow_date()) + "," +
                return_date + "\n")

        fileref_write.close()

    except OSError:
        return False

    else:
        return True


def load_borrow_records(filename):
    """
    Load saved borrow records from a text file and restore borrowing information.

    Input/Parameters:
    filename (str): The name or path of the file containing saved borrow records.

    Output:
    returns None: The function updates the global borrow_records list and restores the borrowed items for each member.
    """

    try:
        fileref_read = open(filename, "r")
        file_lines = fileref_read.readlines()
        for row in file_lines:
            row = row.strip().split(",")

            try:
                member_name = row[0]
                contact_number = row[1]
                item_id = row[2]
                borrow_date = row[3]
                return_date = row[4]

                current_member = None
                for member in members:
                    if member.get_member_name() == member_name and member.get_contact_number() == contact_number:
                        current_member = member

                selected_item = None
                for item in item_list:
                    if item.get_item_id() == item_id:
                        selected_item = item

                if current_member is None or selected_item is None:
                    continue

                if return_date == "":
                    return_date = None

                new_borrow_record = BorrowRecord(current_member,
                    selected_item,
                    borrow_date,
                    return_date)
                
                borrow_records.append(new_borrow_record)

                # Restore items that were still borrowed when the data was saved
                if return_date is None:
                    current_member.get_borrowed_items_list().append(selected_item)
                    selected_item.set_status("Borrowed")

            except IndexError:
                continue

        fileref_read.close()

    except FileNotFoundError:
        print("ERROR IMPORTING BORROW RECORDS")

    except OSError:
        print("ERROR IMPORTING BORROW RECORDS")

load_items("library_items.txt")
load_members("members.txt")
load_borrow_records("borrow_records.txt")

main_menu()

