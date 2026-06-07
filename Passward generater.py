# ==========================================
# Task Manager Project with Undo Feature
# ==========================================

# 1. Dictionary: To store tasks, using Task ID as the Key
tasks_dict = {}

# 2. Stack: A simple list to store deleted tasks for the Undo feature
undo_stack = []

# A simple counter to generate a unique ID for each new task
task_counter = 1 

# Helper function used to sort tasks based on priority
def get_priority(task):
    return task['priority']

# Main Program Loop
while True:
    print("\n" + "="*30)
    print("--- Smart Task Manager ---")
    print("1. Add a new task")
    print("2. View tasks (Sorted by priority)")
    print("3. Complete / Delete a task")
    print("4. Undo last deletion")
    print("5. Exit")
    print("="*30)
    
    choice = input("Choose an option from the menu (1-5): ")
    
    # ---------------------------------
    # 1. Add Task (Insert into Dictionary)
    # ---------------------------------
    if choice == '1':
        title = input("Enter task title: ")
        priority = int(input("Enter priority (1 is highest, 2, 3... etc.): "))
        
        # Save the task in the dictionary
        tasks_dict[task_counter] = {'id': task_counter, 'title': title, 'priority': priority}
        print("✅ Task added successfully!")
        
        task_counter += 1 # Increment counter for the next task
        
    # ---------------------------------
    # 2. View Tasks (Using List and Sort)
    # ---------------------------------
    elif choice == '2':
        if len(tasks_dict) == 0:
            print("📭 No tasks available at the moment.")
        else:
            # Convert dictionary values to a List so we can sort them
            tasks_list = list(tasks_dict.values())
            
            # Sort the list based on priority using the helper function
            tasks_list.sort(key=get_priority)
            
            print("\n📌 -- Current Tasks --")
            for task in tasks_list:
                print(f"ID: {task['id']} | Priority: {task['priority']} | Task: {task['title']}")
                
    # ---------------------------------
    # 3. Delete Task (Using Stack for temporary storage)
    # ---------------------------------
    elif choice == '3':
        task_id = int(input("Enter the ID of the task you want to complete/delete: "))
        
        # Check if the task exists in the dictionary
        if task_id in tasks_dict:
            # Remove from dictionary
            deleted_task = tasks_dict.pop(task_id) 
            
            # Add it to the Stack (Push/Append) for the Undo feature
            undo_stack.append(deleted_task) 
            print("🗑️ Task deleted and moved to the undo bin.")
        else:
            print("❌ Task ID not found!")
            
    # ---------------------------------
    # 4. Undo Deletion (Pop from Stack)
    # ---------------------------------
    elif choice == '4':
        # Check if there is anything in the stack
        if len(undo_stack) > 0:
            # Extract the last deleted task from the Stack (LIFO: Last In, First Out)
            restored_task = undo_stack.pop() 
            
            # Put it back into the main dictionary
            tasks_dict[restored_task['id']] = restored_task
            print(f"⏪ Undo successful! Task '{restored_task['title']}' has been restored.")
        else:
            print("⚠️ Nothing to undo. The stack is empty.")
            
    # ---------------------------------
    # 5. Exit Program
    # ---------------------------------
    elif choice == '5':
        print("👋 Goodbye!")
        break
        
    else:
        print("❌ Invalid choice, please try again.")