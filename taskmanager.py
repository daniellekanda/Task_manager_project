#========TASK MANAGEMENT PROGRAM=========
#This program provides registered users access to a Task Managent program. 
#There are 4 options the user can take: Add a new registered user, add new tasks, view all logged tasks, and view tasks assigned to a specific user. 

#IMPORTING FUNCTION FROM OTHER FILE TO CHECK! 

import datetime
import os.path

#======DEFINING FUNCTIONS========

#Registering User function
def reg_user(menu, login_username):

    if menu == "r" and login_username == "admin":
        print(" ")
        print("You are adding a new user.")
        new_username = input("Please provide the new username: ")
        new_password = input("Please provide the new password: ")
        password_confirmation = input("Please re-enter the new password: ")

        if new_username in password_dictionary.keys():
                print("This username alredy exists. Please try a different username.")

        else:  

            if new_password == password_confirmation:
                with open('user.txt', 'a+') as f:
                    f.write("\n")
                    f.write("{}, {}".format(new_username, new_password))            

                print(" ")
                print("You have succesfully added a new user!")
                print(" ")

            elif new_password != password_confirmation:
                print("The passwords do not match. Please make sure both passwords are the same:\n ")

            elif menu == "r" and login_username != "admin":
                print("Only admins can register new users!")

#Add task function
def add_task():
    if menu == "a":
        assigned_username = input("Please enter the username of the person who the task is assigned to: ")
        task_title = input("Please enter the title of the task: ")
        task_description = input("Please enter a description of the task: ")
        due_date = input("Please enter the due date for this tasks: ")
        current_date = input("Please enter the current date: ")
        
        with open('tasks.txt', 'a+') as f:
           f.write("\n")
           f.write("{}, {}, {}, {}, {}, No".format(assigned_username, task_title, task_description, current_date, due_date))
        
        print(" ")
        print("You have succesfully logged a new tasks!")
        print(" ")

#Designed tasks function 
def design_task(tasks_split, task_number):
    output = f"______[{task_number}]_______"
    output += "\n"
    output += f"Assigned to: {tasks_split[0]}\n"
    output += f"Task summary: {tasks_split[1]}\n"
    output += f"Task description: {tasks_split[2]}\n"
    output += f"Date added: {tasks_split[3]}\n"
    output += f"Date to be completed: {tasks_split[4]}\n"
    output += f"Has the task been started?: {tasks_split[5]}\n"
    
    return(output)

#View all tasks function 
def view_all():
    task_number = 0
    with open('tasks.txt', 'r') as f: 
        for line in f:
            task_number += 1 
            split_data = line.strip().split(",")
            print(design_task(split_data, task_number))

#edit task fucntion 
def change_username(task, task_choice):
    change_user = input("User to be assigned to tasks: ")
    if task[-1] == "Yes":
        print("This task has been completed and cannot be edited.") #can only be edited if task not complete
    else:
        task[0] = change_user
        print(design_task(task, task_choice))            #prints to terminal designed change 

def change_due_date(task, task_choice):
    change_date = input("New completion date:  ")
    if task[-1] == "Yes":
        print("This task has been completed and cannot be edited.") #can only be edited if task not complete
    else:
        task[4] = change_date
        print(design_task(task, task_choice))  #prints to terminal 

def change_status(task, task_choice):
    change_status = input("Has the task been completed:  ")
    print(change_status)
    if task[-1] == "Yes":
        print("This task has been completed and cannot be edited.") #can only be edited if task not complete
    else:
        task[5] = change_status

        print(design_task(task, task_choice))  #prints to terminal 

#rewwrite a task in task.txt
def rewrite_task(task, place):
    #join the split task submitted so it can be written in correct format to file. 
    joined_task = ",".join(task)
    joined_task_w_newline = joined_task + "\n"

    with open('tasks.txt', 'r+') as f:
        contents = f.readlines()
    print(contents)
    contents[place] = joined_task_w_newline

    with open('tasks.txt', 'w+') as f:
        f.writelines(contents)

#View specific user assigned task function and option to edit task
def view_mine():
    task_number = 0
    selected_user = input("Please select a user: ").lower()
    
    with open('tasks.txt', 'r+') as f:
        position = 0 
        user_task_dictionary = {} #empty dictionary to store actual position of task in task.txt
        for line in f:
            position += 1
            tasks_split = line.strip().split(",")
            tasks_split.append(position)
            assinged_user = tasks_split[0]
            if assinged_user == selected_user:
                task_number += 1
                user_task_dictionary[task_number] = position #connects the task number with the specific position in task.txt
                print(design_task(tasks_split, task_number))
    
        print("You can edit an individual task by selecting the task number.\n To return to the main menu input '-1'.")      
        task_choice = int(input("Select a task number to edit or enter '-1': "))
        
        if task_choice == -1:
            print("Back to main menu!")
        else:
            position = user_task_dictionary[task_choice]
            print(position)
            print(task_choice)
        
        print("""What would you like to edit:
        1 - change user assigned 
        2 - change due date 
        3 - mark task as complete""")
        editing_menu = int(input("Please enter a number: "))

        if editing_menu == 1:
            with open('tasks.txt', 'r+') as f:
                for place, line in enumerate(f):
                    if place == (position -1):  #place is the position in task.txt we want to edit 
                        tasks_split = line.strip().split(",")
                        change_username(tasks_split, task_choice)   
                        rewrite_task(tasks_split, place) 
        
        elif editing_menu == 2:
            with open('tasks.txt', 'r+') as f:
                for place, line in enumerate(f):
                    if place == (position -1):  #place is the position in task.txt we want to edit 
                        tasks_split = line.strip().split(",")
                        change_due_date(tasks_split, task_choice)   
                        rewrite_task(tasks_split, place)
        
        elif editing_menu == 3:
            with open('tasks.txt', 'r+') as f:
                for place, line in enumerate(f):
                    if place == (position -1):  #place is the position in task.txt we want to edit 
                        tasks_split = line.strip().split(",")
                        change_status(tasks_split, task_choice)   
                        rewrite_task(tasks_split, place)

#Function to generate all reports for user_overview and task_overview
def generate_reports():
    def number_of_tasks():
        with open('tasks.txt', 'r+') as f:
            number_of_tasks = 0 
            for line in f:
                number_of_tasks += 1
        return(number_of_tasks)

    #complte tasks check for statistics
    def complete_check():
        with open('tasks.txt', 'r+') as f:
            completed_tasks = 0 
            uncompleted_tasks = 0
            for line in f:
                split_task = line.strip().split(",")
                if split_task[-1] == "yes":
                    completed_tasks += 1
        return(completed_tasks)

    #uncomplete task check for statistics 
    def uncomplete_check():
        with open('tasks.txt', 'r+') as f: 
            uncompleted_tasks = 0
            for line in f:
                split_task = line.strip().split(",")
                if split_task[-1] == "no":
                    uncompleted_tasks += 1
        return(uncompleted_tasks)         

    #overdue tasks
    def overdue_tasks():
        with open('tasks.txt', 'r+') as f:
            current_date = datetime.date.today()
            overdue_uncomplete_count = 0
            on_track = 0
            for line in f:
                #gets logged task date 
                split_task = line.strip().split(",")
                if split_task[-1] == "no":      #if the task has not been completed 
                    date_string = split_task[-2]
                    date_string_stripped = date_string.strip()
                    date_object = datetime.datetime.strptime(date_string_stripped, '%d %B %Y') #makes object with time added
                    task_date = date_object.date() #strips time values 
                    if current_date >= task_date:
                        overdue_uncomplete_count += 1
                    elif task_date > current_date:
                        on_track += 1

        return(overdue_uncomplete_count)



    #User_oveview Functions 
    #total number of tasks 
    def number_of_tasks():
        with open('tasks.txt', 'r+') as f:
            number_of_tasks = 0 
            for line in f:
                number_of_tasks += 1
        return(number_of_tasks)


    #tasks per user
    def tasks_per_user():
        with open('tasks.txt', 'r+') as f:
                user_tasks = {}
                for line in f:
                    tasks_split = line.strip().split(",")
                    assinged_user = tasks_split[0]
                    if assinged_user in user_tasks:
                        x = user_tasks[assinged_user]
                        user_tasks[assinged_user] = x + 1
                    else:
                        user_tasks[assinged_user] = 1

        return(user_tasks)   

    #completed tasks per user 
    def completed_tasks_per_user():
            with open('tasks.txt', 'r+') as f: 
                completed_tasks = {}
                for line in f:
                    split_task = line.strip().split(",")
                    status = split_task[-1]
                    user_name = split_task[0]
                    if status == "yes":
                        if user_name in completed_tasks:
                            x = completed_tasks[user_name]
                            completed_tasks[user_name] = x + 1
                        else:
                            completed_tasks[user_name] = 1
                
            return(completed_tasks)

    #uncompleted tasks per user 
    def uncompleted_task_per_user():
        with open('tasks.txt', 'r+') as f: 
            uncompleted_tasks = {}
            for line in f:
                split_task = line.strip().split(",")
                status = split_task[-1]
                user_name = split_task[0]
                if status == "no":
                    if user_name in uncompleted_tasks:
                        x = uncompleted_tasks[user_name]
                        uncompleted_tasks[user_name] = x + 1
                    else:
                        uncompleted_tasks[user_name] = 1

        return(uncompleted_tasks)    

    #overdue and uncomplete
    def overdue_uncomplete_per_user():
        with open('tasks.txt', 'r+') as f:
            current_date = datetime.date.today()
            overdue_uncomplete_count = 0
            on_track = 0
            user_uncomplete = {}    #dictionary of incomplete AND overdue 
            for line in f:
                #gets logged task date 
                split_task = line.strip().split(",")
                if split_task[-1] == "no":      #if the task has not been completed 

                    date_string = split_task[-2]
                    date_string_stripped = date_string.strip()
                    date_object = datetime.datetime.strptime(date_string_stripped, '%d %B %Y') #makes object with time added
                    task_date = date_object.date() #strips time values 
                    if current_date >= task_date:           #if the task is incomplete 
                        overdue_uncomplete_count += 1

                        assinged_user = split_task[0]
                        if assinged_user in user_uncomplete:
                            x = user_uncomplete[assinged_user]
                            user_uncomplete[assinged_user] = x + 1
                        else:
                            user_uncomplete[assinged_user] = 1  

        return(user_uncomplete) 

    #total number of tasks 
    total_tasks = number_of_tasks()

    completed_tasks = complete_check()
    uncompleted_tasks = uncomplete_check()
    overdue_uncompleted_tasks = overdue_tasks()
    percent_uncompleted = round((uncomplete_check() / total_tasks) * 100, 2)
    percent_overdue = round((overdue_tasks() / total_tasks) * 100, 2)

    with open('task_overview.txt', 'w+') as f:
        f.write(f"The total number of tasks generated is: {total_tasks}")
        f.write("\n")
        f.write(f"The total number of completed tasks is: {completed_tasks}")
        f.write("\n")
        f.write(f"The total number of uncompleted tasks is: {uncompleted_tasks}")
        f.write("\n")
        f.write(f"The total number of uncompleted tasks that are overdue is: {overdue_uncompleted_tasks}")
        f.write("\n")
        f.write(f"The percentage of uncomplete overdue tasks is: {percent_uncompleted}%")
        f.write("\n")
        f.write(f"The percentage of overdue tasks is {percent_overdue}%")


    #generate report for users overview          
    #percentage of tasks per user and writes to file 
    with open('user_overview.txt', 'a+') as f:
        f.write("------Percentage of tasks assigned per user------")
        f.write("\n")
        for key in tasks_per_user():
            value = tasks_per_user()[key]
            percentage = round((value/(number_of_tasks())) * 100, 2)
            f.write(f"{key} is assigned {percentage}% of tasks")
            f.write("\n")  

    #percentage of completed tasks and writes to file. 
    with open('user_overview.txt', 'a+') as f:
        f.write("\n")
        f.write("------Percentage of completed tasks-------")
        f.write("\n")
        for key in completed_tasks_per_user():
            value = completed_tasks_per_user()[key]
            percentage = round((value/(tasks_per_user()[key])) * 100, 2)
            f.write(f"{key} has completed {percentage}% of their assigned tasks")
            f.write("\n")  

    #percentage of uncompleted tasks per user and writes to file 
    with open('user_overview.txt', 'a+') as f:
        f.write("\n")
        f.write("------Percentage of uncompleted tasks-------")
        f.write("\n")
        for key in uncompleted_task_per_user():
            value = uncompleted_task_per_user()[key]
            percentage = round((value/(tasks_per_user()[key])) * 100, 2)
            f.write(f"{key} has not completed {percentage}% of their assigned tasks")
            f.write("\n")  

    #percentage of overdue and uncompleted tasks per user 
    with open('user_overview.txt', 'a+') as f:
        f.write("\n")
        f.write("------Percentage of overdue & uncompleted tasks-------")
        f.write("\n")
        for key in overdue_uncomplete_per_user():
            value = overdue_uncomplete_per_user()[key]
            percentage = round((value/(tasks_per_user()[key])) * 100, 2)
            f.write(f"{percentage}% of {key}'s tasks are overdue and incomplete")
            f.write("\n")        




                        
                   
#======IMPORTING LIBRARIES======
#Creates empty dictionary to store passwords
#opens text file and extracts current username and password. Assinging them as key and value and then storing them in the dictionary. 

password_dictionary = {} 

with open('user.txt', 'r') as f:
    for line in f:
        key, value = line.split(',')
        username = key.strip()
        password = value.strip()
        password_dictionary[username] = password


#===========LOGIN SECTION==============
#Ask for username and password from user. 
#checks that the username and password match the same key:value stored in the password dictionary. 
#if a match user accesses program. If not a match the user is prompted to enter a valid username and password. 

while True:
    login_username = input("Please enter your username: ") 
    login_password = input("Please enter your password: ")
    if (login_username, login_password) in password_dictionary.items():
        print(" ")
        print("Login Successful!")
        print(" ")
        break
    else:
        print("You have entered and incorrect username or password. Please try again.")

#=========TASK MANAGEMENT===========
#Present a menu to user of 4 options or to exit the program.
# Admin user gets a different menu with an extra option to view statistics about how many tasks and users are registered. 
# All other users get standard menu 
while True:
    if login_username == "admin":
        print("""Select one of the following options below:\n
    r = Register a user
    a = Adding a new task
    va = view all tasks
    vm = view my tasks
    gr - generate reports
    s = view statistics
    e = exit""")

    else:
        print("""Select one of the following options below:\n
    r = Register a user
    a = Adding a new task
    va = view all tasks
    vm = view my tasks
    e = exit""")
    

    menu = input("Please select an option: ").lower()

#Registering a user: Only admins can register new users. 
# requests a new username and passoword from admin. 
#Admin is asked to provide password twice for confirmation of password. 
#The username and password are then written to a text file storing all registered users. 
    if menu == "r":
        reg_user(menu,login_username)
    elif menu == "a":
        add_task()
    elif menu == "va":
        view_all()
    elif menu == "vm":
        view_mine()

#generate reports for task overview 
    elif menu == "gr" and login_username == "admin":
        generate_reports()
        print("Reports generated.")        

#generate reports for admin (task over view and user overview)
    elif menu == "gr" and login_username != "admin":
        print("Only admins can genereate reports!")

#Statistics (Admin Only): Admins can view how many registered tasks and users there are. 
# Other users recevie error message if they try to access statistics
    elif menu == "s" and login_username == "admin":
        task_file = './task_overview.txt'
        user_file = './user_overview.txt'

        check_task_file = os.path.isfile(user_file)
        check_user_file = os.path.isfile(user_file)

        if check_user_file and check_task_file == True:
            #displays statistics from task overview text file   
            with open('task_overview.txt', 'r+') as f:
                print("<-----Task Overview----->") 
                remove_char = ["[", "]", "'"]   
                for line in f:
                    contents = line.strip("\n").split(",")
                    string_unedited = str(contents)[1:-1]
                    for char in remove_char:
                        string_final = string_unedited.replace(char, " ")
                    print(string_final)
                print(" ")

            #displays statistics from user overview text file 
            with open('user_overview.txt', 'r+') as f: 
                print("<-----User Overview------>")
                remove_char = ["[", "]", "'"]  
                for line in f:
                    contents = line.strip("\n").split(",")
                    string_unedited = str(contents)[1:-1]
                    for char in remove_char:
                        string_final = string_unedited.replace(char, " ")
                    print(string_final)
                print(" ")  

        else:
            #function generates task and user overview reports 
            generate_reports()
            #displays statistics from task overview text file 
            with open('task_overview.txt', 'r+') as f:
                print("<-----Task Overview----->") 
                remove_char = ["[", "]", "'"]   
                for line in f:
                    contents = line.strip("\n").split(",")
                    string_unedited = str(contents)[1:-1]
                    for char in remove_char:
                        string_final = string_unedited.replace(char, " ")
                    print(string_final)
                print(" ")

            #displays statistics from user overview text file 
            with open('user_overview.txt', 'r+') as f: 
                print("<-----User Overview------>")
                remove_char = ["[", "]", "'"]  
                for line in f:
                    contents = line.strip("\n").split(",")
                    string_unedited = str(contents)[1:-1]
                    for char in remove_char:
                        string_final = string_unedited.replace(char, "")
                    print(string_final)
                print(" ")  
    
    elif menu == "s" and login_username != "admin":
        print("Only admins can check statistics!")
  
         
#Exit: allows user to exit program. 
    elif menu == "e":
        print("Goodbye!")
        exit()
    
    else:
        print("You have entered an invalid choice. Please select a choice from the menu provided.")

        
