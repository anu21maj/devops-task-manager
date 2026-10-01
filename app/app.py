from flask import Flask, render_template, jsonify, request
from app.database import get_db_connection

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(tasks)


@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    title = data.get("title")

    if not title:
        return {"error": "Task title is required"}, 400

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s)",
        (title,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Task added successfully"}, 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"]) #This route is for updating a specific task based on its ID. It listens for PUT requests at the endpoint "/api/tasks/<task_id>", where <task_id> is a placeholder for the actual ID of the task to be updated.
def update_task(task_id): #This function handles the logic for updating a task
    data = request.get_json() #This line retrieves the JSON data sent in the request body and stores it in the variable data. The data is expected to contain information about the task that needs to be updated, such as its completion status.

    completed = data.get("completed") #This line extracts the value associated with the key "completed" from the data dictionary. It represents whether the task is marked as completed or not. The value is stored in the variable completed.

    connection = get_db_connection() #This line establishes a connection to the database by calling the get_db_connection() function. It returns a connection object that allows interaction with the database.

    cursor = connection.cursor() #This line creates a cursor object using the connection object. The cursor is used to execute SQL queries and fetch results from the database.

    #This line executes an SQL query to update the "completed" status of a specific task in the "tasks" table. The query uses placeholders (%s) for the values to be updated, and the actual values are provided as a tuple (completed, task_id). The completed variable represents the new completion status, and task_id represents the ID of the task to be updated.
    cursor.execute(
        "UPDATE tasks SET completed = %s WHERE id = %s",
        (completed, task_id)
    )

    #This line commits the changes made to the database. It ensures that the update operation is saved and persisted in the database. Without this line, the changes would not be applied, and the task's completion status would remain unchanged.
    connection.commit()

    #This line closes the cursor and the database connection to free up resources.
    cursor.close()
    #This line closes the database connection.
    connection.close()

    return {"message": "Task updated successfully"}

@app.route("/api/tasks/<int:task_id>", methods=["DELETE"]) #This route is for deleting a specific task based on its ID. It listens for DELETE requests at the endpoint "/api/tasks/<task_id>", where <task_id> is a placeholder for the actual ID of the task to be deleted.
def delete_task(task_id): #This function handles the logic for deleting a task. It takes the task_id as a parameter, which represents the ID of the task to be deleted.
    connection = get_db_connection() #This line establishes a connection to the database by calling the get_db_connection() function. It returns a connection object that allows interaction with the database.

    cursor = connection.cursor() #This line creates a cursor object using the connection object. The cursor is used to execute SQL queries and fetch results from the database.


#this line executes an SQL query to delete a specific task from the "tasks" table based on its ID. The query uses a placeholder (%s) for the task ID, and the actual value is provided as a tuple (task_id,). The task_id variable represents the ID of the task to be deleted.
    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,)
    )

    connection.commit() #This line commits the changes made to the database. It ensures that the delete operation is saved and persisted in the database. Without this line, the task would not be removed from the database.

    cursor.close() #this line closes the cursor to free up resources. It is good practice to close the cursor after executing the SQL query.
    connection.close() #This line closes the database connection to free up resources. It is good practice to close the connection after completing the database operations.

    return {"message": "Task deleted successfully"}
#this line checks if the script is being run directly (as the main program) and not being imported as a module in another script. If it is the main program, it starts the Flask application by calling app.run(). The host parameter is set to "0.0.0.0" and the port parameter is set to 5000.


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)