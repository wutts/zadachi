import os, csv, datetime

tasks_csv = 'tasks.csv'

# Check if CSV file exists, creates it if not
if os.path.exists(tasks_csv):
    pass
else:
    print('Tasks database does not exist.\n')
    print('Creating tasks database ...')
    with open(tasks_csv, 'w') as tasks_file_header:
        tasks_file_header.write('id,title,description,done,due,priority,created_at,updated_at\n')

# Load tasks function, showing tasks in CSV
def load_tasks():
    with open(tasks_csv, 'r') as tasks:
        tasks_reader = csv.DictReader(tasks)
        tasks_list = []
        for task in tasks_reader:
            print(task)
            tasks_list.append(task)
    return tasks_list

