from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

TASKS_FILE = 'tasks.json' 

# Load tasks from a JSON file if it exists, otherwise return an empty list.
# Returns f which is a list of tasks, or empty list if no file found.
def load_tasks(): 
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f: # loads tasks into 'f' list object
            return json.load(f)
    return []

# Writes/saves the list of tasks to a JSON file.
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

# main route
# displays the list of tasks
@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

# route to add a new task
# allows users to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks = load_tasks()
        tasks.append({'id': len(tasks), 'text': task, 'done': False})
        save_tasks(tasks)
    return redirect(url_for('index'))

# route to delete a task
# allows users to delete a task by its ID
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [item for item in tasks if item['id'] != task_id]
    save_tasks(tasks)
    return redirect(url_for('index'))

# health check route
# returns a simple JSON response indicating the app is running
@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

# runs the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# will update later (to add a completed toggle feature)
"""
@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
            break
    save_tasks(tasks)
    return redirect(url_for('index'))
"""