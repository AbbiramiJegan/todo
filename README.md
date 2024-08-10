# To-Do List Application

This is a simple web-based to-do list application built using Django. Users can add tasks, mark them as completed, and delete tasks from their list.

## Features

1. **Adding a New Task:**
   - Users can input a task description and click the "Add Task" button.
   - The task is saved to the database with an initial status of incomplete.

2. **Marking a Task as Completed:**
   - Each task is displayed with a "Finished" button.
   - When clicked, the task status is updated to "completed" in the database.

3. **Deleting a Task:**
   - Tasks are listed with a "Delete" button.
   - Clicking the button removes the task from the list.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/AbbiramiJegan/todo.git
   ```

2. Navigate to the project directory:
   ```
   cd todo-app
   ```

3. Install dependencies (assuming you have Python and pip installed):
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Access the application in your browser at `http://localhost:8000/`.

## Technologies Used

- Django (Python web framework)
- SQLite (default database)
- Bootstrap (for styling)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---
