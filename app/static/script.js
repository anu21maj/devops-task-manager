const taskInput = document.getElementById("taskInput");
const addTaskButton = document.getElementById("addTaskButton");
const taskList = document.getElementById("taskList");

addTaskButton.addEventListener("click", function () {

    const taskText = taskInput.value.trim();

    if (taskText === "") {
        return;
    }

    const newTask = document.createElement("li");

    newTask.textContent = taskText;

    taskList.appendChild(newTask);

    taskInput.value = "";
});
