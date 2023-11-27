# Build an application where users can add tasks to a list, mark them as completed, and delete them.
# Tasks:
# - Needs to display the task list (DONE)
# - Needs a user input for what they want to do (DONE)
# - Needs a user input to add a task (DONE)
# - Needs user input to delete task (DONE)
# - Needs user input to complete task

global_list = []

def addTask():
    userInput = input("What would you like to add to the list: ")

    global global_list
    global_list.append(userInput)
    print(global_list)

def deleteTask():
    global global_list
    userInput = input("What would you like to delete from the list: ")

    if userInput in global_list:
        global_list.remove(userInput)
        print(f"{userInput} removed from list.")
        print(global_list)
    else:
        print(f"{userInput} not found in list.")
        print(global_list)

def completeTask():
    global global_list
    userInput = input("What task did you complete: ")

    if userInput in global_list:
        global_list.remove(userInput)
        print(f"Congrats on completeing {userInput}.")
        print(global_list)
    else:
        print(f"{userInput} not found in list.")
        print(global_list)

def main():
    print("Welcome to the To-Do List!")

    while True:
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Quit")

        userInput = input("Please select what you would like to do: ")

        try:
            if userInput == "1":
                addTask()
            elif userInput == "2":
                deleteTask()
            elif userInput == "3":
                completeTask()
            elif userInput == "4":
                print("Thank you for using the To-Do List! Goodbye!")
                break
        except ValueError:
            print("Invalid input.")

main()