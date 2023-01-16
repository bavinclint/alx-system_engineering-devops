#!/usr/bin/python3
"""
    that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import csv
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


def write_csv_row(employee_id: int, writer):
    """
        write csv row
    """
    employee_infos = get_employee_information(employee_id)
    employee_tasks = get_employee_tasks(employee_id)

    for task in employee_tasks:
        writer.writerow(
            [
                employee_id,
                employee_infos.get("username"),
                task.get("completed"),
                task.get("title")
            ]
        )


def export_employee_tasks_in_csv(employee_id: int):
    """
        export employee task list in csv
    """
    with open("{}.csv".format(employee_id), mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, lineterminator='\n')
        write_csv_row(employee_id, writer)
    file.closed


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage 1-export_to_CSV.py <USERID>")

    export_employee_tasks_in_csv(sys.argv[1])
