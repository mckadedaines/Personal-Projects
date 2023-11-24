const inputBox = document.querySelector("#input_box")
const submitButton = document.querySelector("#submit_button");
const lists = document.querySelector("#task_list");

submitButton.addEventListener("click", function(){
    let inputBoxValue = inputBox.value;

    if (inputBoxValue === ""){
        alert("Please enter a task.");
        return;
    }

    createTaskElement(inputBoxValue);

    addTaskToLocalStorage(inputBoxValue);
});

function addTaskToLocalStorage(task){
    let tasks = localStorage.getItem("tasks");

    tasks = tasks ? JSON.parse(tasks) : [];

    tasks.push(task);

    localStorage.setItem('tasks', JSON.stringify(tasks));
};

function updateTaskInLocalStorage(deletedTask) {
    let tasks = localStorage.getItem('tasks');
    tasks = tasks ? JSON.parse(tasks) : [];

    tasks = tasks.filter(tasks => task !== deletedTask);

    localStorage.setItem('tasks', JSON.stringify(tasks));
};

function createTaskElement(taskString) {
    let deleteButton = document.createElement("button");
    let taskItem = document.createElement("li");
    
    taskItem.textContent = taskString;
    deleteButton.textContent = "Delete";

    taskItem.appendChild(deleteButton);
    lists.appendChild(taskItem);

    deleteButton.addEventListener("click", function() {
        let taskToRemove = this.parentNode.textContent.replace('Delete', '');
        this.parentNode.remove();
        updateTasksInLocalStorage(taskToRemove);
    });
};

function loadTasks(){
    let tasks = localStorage.getItem('tasks');
    tasks = tasks ? JSON.parse(tasks) : [];

    tasks.forEach(taskString => {
        createTaskElement(taskString);
    });
}

document.addEventListener('DOMContentLoaded', loadTasks);