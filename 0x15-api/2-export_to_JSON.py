#!/usr/bin/python3
""" Exporting csv files"""
import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        my_id = sys.argv[1]
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(my_id)
        dict1 = requests.get(url).json()
        username = dict1.get('username')
        url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.\
               format(my_id)
        list2 = requests.get(url2).json()
        dict_tasks = {}
        dict_tasks[my_id] = []
        t_total = 0
        for tasks in list2:
            if tasks.get('userId') == int(my_id):
                status = tasks.get('completed')
                text = tasks.get('title')
                dict_tasks[my_id].append({"task": text, "completed":
                                         status, "username": username})
        with open('USER_ID.json', 'w') as outfile:
            json.dump(dict_tasks, outfile)
