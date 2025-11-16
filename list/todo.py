import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   # default in XAMPP (empty)
        database="todo_db"
    )

def add_task():
    task = input("Enter task: ")

    conn = connect_db()
    cursor = conn.cursor()

    sql = "INSERT INTO tasks (task) VALUES (%s)"
    cursor.execute(sql, (task,))
    conn.commit()

    print("✔ Task added successfully!\n")

    cursor.close()
    conn.close()

def view_tasks():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    if not rows:
        print("📭 No tasks found.\n")
    else:
        print("\n------ YOUR TO-DO LIST ------")
        for row in rows:
            print(f"ID: {row[0]} | Task: {row[1]} | Status: {row[2]}")
        print()

    cursor.close()
    conn.close()
def update_task():
    task_id = int(input("Enter task ID to update: "))
    new_task = input("Enter new task name: ")

    conn = connect_db()
    cursor = conn.cursor()

    sql = "UPDATE tasks SET task = %s WHERE id = %s"
    cursor.execute(sql, (new_task, task_id))
    conn.commit()

    print("📝 Task updated successfully!\n")

    cursor.close()
    conn.close()
def change_status():
    task_id = int(input("Enter task ID: "))

    print("1. Mark as Completed")
    print("2. Mark as Pending")
    choice = input("Choose (1 or 2): ")

    if choice == "1":
        status = "Completed"
    else:
        status = "Pending"

    conn = connect_db()
    cursor = conn.cursor()

    sql = "UPDATE tasks SET status = %s WHERE id = %s"
    cursor.execute(sql, (status, task_id))
    conn.commit()

    print("🔄 Status updated!\n")

    cursor.close()
    conn.close()
def delete_task():
    task_id = int(input("Enter task ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()

    sql = "DELETE FROM tasks WHERE id = %s"
    cursor.execute(sql, (task_id,))
    conn.commit()

    print("🗑️ Task deleted successfully!\n")

    cursor.close()
    conn.close()
def main():
    while True:
        print("========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Change Status")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Choose option (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            change_status()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
