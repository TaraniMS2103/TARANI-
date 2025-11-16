Step 1 — Prerequisites
Make sure you have installed:
1.	Python (3.8 or above)
2.	python --version
3.	XAMPP (for MySQL)
o	Start MySQL via XAMPP Control Panel.
4.	VS Code (or any code editor)
Step 2 — Set up Database
1.	Open phpMyAdmin via XAMPP.
2.	Create the database:
CREATE DATABASE todo_db;
USE todo_db;
3.	Create the tasks table with all new columns:
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    priority ENUM('Low','Medium','High') DEFAULT 'Medium',
    due_date DATE,
    category VARCHAR(50),
    description TEXT,
    recurring ENUM('None','Daily','Weekly','Monthly') DEFAULT 'None'
);

Step 3 — Set up Project Folder
1.	Create a folder for your project, e.g., D:\LIST.
2.	Inside the folder, create:
app.py          # Flask app
templates/      # HTML files
    index.html
    add.html
    update.html
static/         # CSS / JS files
    style.css

Step 4 — Install Python Libraries
Open VS Code terminal inside your project folder:
pip install flask mysql-connector-python

Step 5 — Add Flask Code
1.	Copy the updated app.py (with /add, /update, /toggle, /delete, progress bar calculation, dark mode support).
2.	Make sure the connect_db() function points to your MySQL:
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   # XAMPP default
        database="todo_db"
    )

Step 6 — Add HTML Templates
1.	index.html → updated table, progress bar, dark mode toggle
2.	add.html → form with task, priority, due date, category, description, recurring
3.	update.html → same fields as add.html for editing
Step 7 — Add CSS
In static/style.css, include:
•	Styling for tables, buttons, forms
•	Dark mode styles
•	Progress bar styles

Step 8- Run Flask App
Open VS Code terminal in project folder:
python app.py
•	Flask server will start:
* Running on http://127.0.0.1:5000

Step 9 - Open Web App
1.	Open browser → http://127.0.0.1:5000/
2.	Test all functionality:
•	Add Task
•	Update Task
•	Delete Task
•	Toggle Status
•	Dark Mode
•	Progress Bar
•	Verify priority, due date, category, recurring fields
Step 10 - Optional Enhancements
•	Make the website mobile-responsive with CSS or Bootstrap
•	Add hover effects / animations
•	Add user login for multi-user support
•	Add notifications / email reminders

