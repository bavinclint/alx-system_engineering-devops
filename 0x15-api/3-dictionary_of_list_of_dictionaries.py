#!/usr/bin/python3
"""
    that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""


import json
import requests

domain_name = "https://jsonplaceholder.typicode.com"


def get_employees_informations():
    """
        get all employee informations
    """
    try:
        response = requests.get(
            url="{}/users/".format(domain_name))

        return response.json()
    except Exception:
        return False


def get_employee_information(employee_id: int) -> json:
    """
        get employee informations
    """
    try:
        response = requests.get(
            url="{}/users/{}/".format(domain_name, employee_id))

        return response.json()
    except Exception:
        return False


def get_employee_tasks(employee_id: int) -> json:
    """
        get employee task list
    """
    try:
        response = requests.get(
            url="{}/users/{}/todos".format(domain_name, employee_id))

        return response.json()
    except Exception:
        return False


def format_task_to_json(task: json, employee_infos: json):
    """
        format a task to json
    """

    return {
        'task': task.get("title"),
        'completed': task.get("completed"),
        'username': employee_infos.get('username')
    }


def format_employee_list_format(employee_infos: json):
    """
        format employee list
    """
    json_task_data = []
    json_data = {}
    employee_tasks = get_employee_tasks(employee_infos.get("id"))

    for task in employee_tasks:
        json_task_data.append(
            {
                'task': task.get("title"),
                'completed': task.get("completed"),
                'username': employee_infos.get("username")
            }
        )

    json_data[employee_infos.get("id")] = json_task_data

    return json_data


def export_all_employee_to_json():
    """
        export employee task list in json
    """
    employees = get_employees_informations()
    all_employees = {}

    for employee in employees:
        with open("todo_all_employees.json", 'w', encoding="UTF-8") as file:
            all_employees.update(format_employee_list_format(employee))
            file.write(json.dumps(all_employees))


if __name__ == "__main__":
    export_all_employee_to_json()
