#!/usr/bin/python3
"""
    that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""


import json
import requests
import sys

domain_name = "https://jsonplaceholder.typicode.com"


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


def get_employee_tasks(employee_id) -> json:
    """
        get employee task list
    """
    try:
        response = requests.get(
            url="{}/users/{}/todos".format(domain_name, employee_id))

        return response.json()
    except Exception:
        return False


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


def export_employee_tasks_in_json(employee_id: int):
    """
        export employee task list in json
    """
    employee_infos = get_employee_information(employee_id)
    json_data = format_employee_list_format(employee_infos)

    with open("{}.json".format(
            employee_infos.get("id")), 'w', encoding="UTF-8") as file:
        file.write(json.dumps(json_data))
    file.closed


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage 0-gather_data_from_an_API.py <USERID>")

    export_employee_tasks_in_json(sys.argv[1])
