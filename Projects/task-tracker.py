# Add, Remove, Edit a task
# Add and edit a description

tasks = []

# Auxiliary Functions
def displayTasks(all_tasks):
    print("\nYour Tasks: ")

    if len(all_tasks) <= 0:
        print ("\nNo tasks")
    else:
        for index, task in enumerate(all_tasks):
            print(f'{index+1}: {task}')

def newOperation(all_tasks):
    operation = input("Press 'A' to add task, 'E' to edit task, 'R' to remove task or 'F' to end the application.")
    if operation == 'A':
        addTask(all_tasks)
    elif operation == 'E':
        editTask(all_tasks)
    elif operation == 'R':
        removeTask(all_tasks)
    elif operation == 'F':
        return
    else:
        print("Invalid operation. Please try again.")
        newOperation(all_tasks)

def removeTask(all_tasks): #Removes the task
    task_number = input('Enter the number of task to be removed:')

    all_tasks.remove(all_tasks[int(task_number)-1])
    print(f'Task {task_number} has been removed')
    displayTasks(all_tasks)
    newOperation(all_tasks)

def addTask(all_tasks): #Adds the task
    new_task = input('Add a task: ')
    all_tasks.append(new_task)

    displayTasks(all_tasks)
    newOperation(all_tasks)

def editTask(all_tasks): #Edits the task
    task_number = input('Enter the number of task to be edited:')
    new_task = input('Edit task:')
    all_tasks[int(task_number)-1] = new_task
    print(f'Item {task_number} edited')

    displayTasks(all_tasks)
    newOperation(all_tasks)

# Start Application
addTask(tasks)