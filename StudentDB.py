import sqlite3

# Connect to the database (this will create a new file called 'school.db' if it doesn't exist)
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Create Students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY,
        name TEXT,
        year_level INTEGER
    )
''')

# Create Grades table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Grades (
        student_id INTEGER,
        subject TEXT,
        grade INTEGER,
        FOREIGN KEY (student_id) REFERENCES Students(student_id)
    )
''')


with open('School Grades.txt', 'r') as file:
    for line in file:
        data = line.split()

        student_data = (data[0], data[1], data[2])
        grade_data = (data[0], data[3], data[4])
        print(student_data)
        print(grade_data)
        cursor.execute('INSERT INTO Students VALUES (?, ?, ?)', student_data)

        cursor.execute('INSERT INTO Grades VALUES (?, ?, ?)', grade_data)



# Commit the changes and close the connection
conn.commit()
conn.close()

