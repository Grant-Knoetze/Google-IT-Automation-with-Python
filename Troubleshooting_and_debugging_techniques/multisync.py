#!/usr/bin/env python3

from multiprocessing import pool


def run(task):
    # Do something with the task here
    print("Handling {}".format(task))


if __name__ == "main":
    tasks = ['task1', 'task2', 'task3']
    # Create a pool of a specific number of CPU's
    p = pool(len(tasks))
    # Start each task within the pool
    p.map(run, tasks)
