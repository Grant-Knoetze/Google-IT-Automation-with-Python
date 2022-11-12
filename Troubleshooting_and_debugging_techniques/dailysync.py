#!/usr/bin/env python3
import os
import multiprocessing
import subprocess

for root, dirs, files in os.walk("/data/prod/"):
    tasks = ["task1", "task2", "task3"]
    p = pool(len(tasks))
    src = "/data/prod/"
    dest = "/data/prod_backup/"
    subprocess.call(["rsync", "-arq", src, dest])
