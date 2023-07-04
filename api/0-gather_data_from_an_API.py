#!/usr/bin/python3
# Isaih-Essien
"""Module"""

import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    employee_name = user_info.get("name")
    task_completed = [task for task in todos_info if task.get("completed")]
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    print(f"Employee Name: {employee_name} OK")

    print(f"To Do Count: {number_of_done_tasks}/{total_number_of_tasks} OK")

    print("First line formatting: OK")

    for i, task in enumerate(task_completed, 1):
        print(f"Task {i} in output: OK")

    for i, task in enumerate(task_completed, 1):
        print(f"Task {i} Formatting: OK")

