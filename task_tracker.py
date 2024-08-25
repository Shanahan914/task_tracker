import argparse
import json
import datetime


# helper functions

#turns datetime into a json serializeable format
def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Function unable to serialize this type of data")

#gets the existing json file of actions (if it exists) or sets it to an empty list 
def get_repo():
    try: 
        with open("task-cli.json") as json_repo:
            repo = json.load(json_repo)
        return repo
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

#gets the max id number and adds 1 to generate id for new task
def get_new_id():
    repo = get_repo()   
    if len(repo) < 1:
        return 1
    else:
        return int(max(repo.keys())) + 1
    
#validating id has been provided (is 2nd arg an int?)
def is_id_valid(id):
    try:
        int(id)
        return True
    except ValueError:
        return False


#validating arg is likely a string (based on length only)
def is_task_valid(task):
    if task:
        return True if len(task) > 3 else False 
    else:
        return False


#save repo
def save_repo(repo):
    try:
        with open("task-cli.json", "w") as outfile:
            outfile.seek(0)
            json.dump(repo, outfile, indent=2, default=serialize_datetime)
    except IOError:
        print ("There was a problem with the file system. Please try again.")


#update status
def update_status(id, status):
    if is_id_valid(id):
        repo=get_repo()
        try:
            repo[id]["status"] = status
            save_repo(repo)
            print (f"Task marked as {status} (ID:{args.first})")
        except KeyError:
            print ("You must provide a valid id number. You can use the list action to see all your current tasks")


#list based on current status
def list_by_status(status):
    repo = get_repo()
    if len(repo) == 0:
        print ("No tasks have been added")
    else:
        print("-----------------")
        print (f"Your current tasks with a status of {status}:")
        for x in repo:
            if repo[x]["status"] == status:
                print (f"ID{x}: {repo[x]['description']}")
        print("-----------------")
                    


# argparse initialisation
parser = argparse.ArgumentParser(
    prog="task_tracker.py",
    description="valid actions are add, update, delete, mark-in-progress, mark-done, list, list + done/todo/in-progress"
)

parser.add_argument("action", choices=["add", "update", "delete", "mark-in-progress", "mark-done","list", "list-done", "list-todo", "list-in-progress"])
parser.add_argument("first", nargs="?")
parser.add_argument("second", nargs="?")

args = parser.parse_args()

# defining the action logs

# add a task
if args.action == "add":
    if is_task_valid(args.first):
        new_id = get_new_id()
        task_data= {
            "description": args.first,
            "status": "todo",
            "createdAt":datetime.datetime.now(),
            "updatedAt":datetime.datetime.now()
        }

        repo = get_repo()
        repo[new_id] = task_data

        save_repo(repo)
        
        print (f"Task added successfully (ID:{new_id})")
    else:
        print ("Please add a task description of 4 characters or more")
    

#update a task
if args.action == "update":
    if is_id_valid(args.first) and is_task_valid(args.second):
        repo = get_repo()
        try:
            repo[args.first]["description"] = args.second
            save_repo(repo)
            print (f"Task updated (ID: {args.first})")
        except KeyError:
            print("You must provide a valid id number. You can use the list action to see all your current tasks")
    else:
        print ("Your entry must be update <id> <task> <description>")


#deletes a task
if args.action == "delete":
    if is_id_valid(args.first):
        repo = get_repo()
        try:
            repo.pop(args.first)
            save_repo(repo)
            print("Task deleted")
        except KeyError:
            print("You must provide a valid id number")
    else:
        print ("Your entry must be: delete <id>")


#marks task as "in progress"
if args.action == "mark-in-progress":
    update_status(args.first, "in progress")
    

#marks task as "done"
if args.action == "mark-done":
    update_status(args.first, "done")     



#lists all tasks
if args.action == "list":
    repo = get_repo()
    if len(repo) == 0:
        print ("No tasks have been added")
    else:
        print("-----------------")
        print ("Your current tasks:")
        for x in repo:
            print (f"ID{x}: {repo[x]['description']} -- {repo[x]['status']}")
        print("-----------------")
                    

#lists action with status of done
if args.action == "list-done":
    list_by_status("done")


#lists action with status of done
if args.action == "list-in-progress":
    list_by_status("in progress")


#lists action with status of done
if args.action == "list-todo":
    list_by_status("todo")


    




