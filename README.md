# School Database Management System

This Python script creates a SQLite database named 'school.db' to manage student information and grades. The database has two tables: Students and Grades.

## Getting Started

### Prerequisites

- Python installed (version 3.x)
- SQLite3

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Run the Python script:

    ```bash
    python school_database.py
    ```

## Database Structure

### Students Table

- `student_id` (INTEGER): Primary key
- `name` (TEXT): Student's name
- `year_level` (INTEGER): Student's year level

### Grades Table

- `student_id` (INTEGER): Foreign key referencing `student_id` in the Students table
- `subject` (TEXT): Subject name
- `grade` (INTEGER): Student's grade in the subject

## Data Input

The script reads student information and grades from a file named 'School Grades.txt'. The file should contain data in the following format:

student_id name year_level subject grade

For example:

1 John Doe 10 Math 90

2 Jane Smith 11 Science 85

## Notes

- The script uses SQLite as the database engine.
- If 'school.db' doesn't exist, it will be created automatically.
- The student data is fictional and do not represent any actual students.

Feel free to customize the script and database structure according to your requirements.

## Author

Alex McKinley

