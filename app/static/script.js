const taskInput = document.getElementById("taskInput");
const addTaskButton = document.getElementById("addTaskButton");
const taskList = document.getElementById("taskList");


async function loadTasks() {

    const response = await fetch("/api/tasks");

    const tasks = await response.json();

    taskList.innerHTML = "";

    tasks.forEach(function (task) {

        const newTask = document.createElement("li");

        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.checked = task.completed;

        checkbox.addEventListener("change", async function () {

            await fetch(`/api/tasks/${task.id}`, {

                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    completed: checkbox.checked
                })
            });

            loadTasks();
        });


        const taskText = document.createElement("span");
        taskText.textContent = " " + task.title;


        const deleteButton = document.createElement("button");
        deleteButton.textContent = " Delete";

        deleteButton.addEventListener("click", async function () {

            await fetch(`/api/tasks/${task.id}`, {
                method: "DELETE"
            });

            loadTasks();
        });


        newTask.appendChild(checkbox);
        newTask.appendChild(taskText);
        newTask.appendChild(deleteButton);

        taskList.appendChild(newTask);
    });
}


addTaskButton.addEventListener("click", async function () {

    const taskText = taskInput.value.trim();

    if (taskText === "") {
        return;
    }

    await fetch("/api/tasks", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            title: taskText
        })
    });

    taskInput.value = "";

    loadTasks();
});


loadTasks();