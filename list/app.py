from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   # XAMPP default
        database="todo_db"
    )

# Home page - show tasks
@app.route("/")
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    
    # Calculate progress
    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t[2] == "Completed"])
    progress = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0
    
    cursor.close()
    conn.close()
    return render_template("index.html", tasks=tasks, progress=progress)


# Add task page
# Add task page
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        task = request.form["task"]
        priority = request.form["priority"]
        due_date = request.form["due_date"]  # format: YYYY-MM-DD
        category = request.form["category"]
        description = request.form["description"]
        recurring = request.form["recurring"]

        conn = connect_db()
        cursor = conn.cursor()
        sql = """
        INSERT INTO tasks (task, priority, due_date, category, description, recurring)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (task, priority, due_date, category, description, recurring))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/")
    
    # GET request — show the form
    return render_template("add.html")


# Delete task
@app.route("/delete/<int:task_id>")
def delete(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")

# Change status
@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM tasks WHERE id = %s", (task_id,))
    status = cursor.fetchone()[0]
    new_status = "Pending" if status == "Completed" else "Completed"
    cursor.execute("UPDATE tasks SET status = %s WHERE id = %s", (new_status, task_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")
# Update task page
@app.route("/update/<int:task_id>", methods=["GET", "POST"])
def update(task_id):
    conn = connect_db()
    cursor = conn.cursor()

    if request.method == "POST":
        new_task = request.form["task"]
        cursor.execute("UPDATE tasks SET task = %s WHERE id = %s", (new_task, task_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/")

    # GET request — show current task
    cursor.execute("SELECT task FROM tasks WHERE id = %s", (task_id,))
    task = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("update.html", task_id=task_id, task=task[0])

if __name__ == "__main__":
    app.run(debug=True)
