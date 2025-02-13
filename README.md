# Student Database Management System

A Python-based **command-line application** for managing student records using SQLite. This system allows users to **add, search, update, delete, and display** student records efficiently.

## Features

- **Student Management**:
  - Add new students with name, age, and grade.
  - Search students by first or last name.
  - Update student grades.
  - Delete student records.
  - Display all current students in the system.

- **Database Integration**:
  - Uses **SQLite** to store and manage student records.
  - Data persistence ensures no loss of records upon program exit.

- **User-Friendly Interface**:
  - An interactive command-line menu for easy navigation.

## Requirements

- **Python 3.x** or higher.  
- **SQLite** (built-in with Python).  
- No external libraries required.  

## How to Run

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script with the following command below:

```bash
python PythonBankAccount.py
```

## Usage

The system provides the following options:

- **Add Student**: Enter first name, last name, age, and grade to add a new student.  
- **Search Student**: Find a student by first or last name.  
- **View All Students**: Display a list of all students in the database.  
- **Update Student Grade**: Modify a student’s grade using their ID or first name.  
- **Delete Student**: Remove a student from the database.  
- **Exit**: Close the program.  


## Example
```
**************************************************
Welcome to the Student Database Management System!

Choose an option:
1 - Add a new student
2 - Search for a student
3 - View all students
4 - Edit a student's grade
5 - Delete a student
6 - Exit
::: 1

Enter Student Details:
First Name: John
Last Name: Doe
Age: 20
Grade: 85.5

Student successfully added!
------------------------------------------------
List of Students:
-------------------------------------
ID      First Name     Last Name    Age   Grade
-------------------------------------
1       John          Doe          20    85.5    
-------------------------------------
Total students: 1.

------------------------------------------------
```

## Code Structure  

### Student Database Management  

- Student records are managed in an **SQLite database** table called `students`, where entries can be added, removed, updated, or displayed.  
- The database schema includes:  
  - **id** (Primary Key) – Auto-incremented student ID.  
  - **first_name** – Student’s first name.  
  - **last_name** – Student’s last name.  
  - **age** – Student’s age.  
  - **grade** – Student’s academic grade.  

### Class & Function Implementation  

The system is implemented using **functions** to handle student operations:  

- **`add_student()`** – Adds a new student after validating input.  
- **`get_student_by_name()`** – Searches for students by first or last name.  
- **`show_all_students()`** – Displays all students in the database.  
- **`update_student_grade()`** – Updates a student's grade using their name or ID.  
- **`delete_student()`** – Deletes a student record based on name or ID.  

Each function interacts with the SQLite database to ensure **data consistency and persistence**.  


## Author

- Developed by **GhostKX**
- GitHub: **[GhostKX](https://github.com/GhostKX/School-Management-Database)**
