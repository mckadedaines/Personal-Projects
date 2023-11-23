const inputBox = document.querySelector("#input_box")
const submitButton = document.querySelector("#submit_button");
const lists = document.querySelector("#task_list");

submitButton.addEventListener("click", function(){
    let inputBoxValue = inputBox.value;

    if (inputBoxValue === ""){
        alert("Please enter a task.");
        return;
    }

    let deleteButton = document.createElement("button");
    let taskItem = document.createElement("li");
    
    taskItem.textContent = inputBoxValue;
    deleteButton.textContent = "Delete";

    taskItem.appendChild(deleteButton);
    lists.appendChild(taskItem);

    inputBox.value = ""; 

    deleteButton.addEventListener("click", function() {
        this.parentNode.remove();
    })
});