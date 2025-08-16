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



