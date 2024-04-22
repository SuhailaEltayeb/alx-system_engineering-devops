#!/usr/bin/python3
'''Script to return information about employee TODO list progress'''
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)
        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data.get('name')
        tasks_done = [task for task in todo_data if task.get('completed')]
        total_tasks = len(todo_data)

        print("Employee {} is done with tasks({}/{}):".format(employee_name, len(tasks_done), total_tasks))
        for task in tasks_done:
            print("\t{}".format(task.get('title')))

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
