#!/usr/bin/env python3
import psutil
import shutil

du = shutil.disk_usage("/")  # In bytes.
print(du)


"""Calculate percentage of free space"""
free_space = du.free / du.total * 100  # In percentage
print(free_space)


"""cpu_percent receives an interval in seconds as the first parameter and a boolean (True || False) as the second
  parameter and returns an average percentage of CPU usage in that interval  since cpu usage varies moment by moment
  due to processes starting and stopping.. If no "percpu" boolean is included, a general system-wide percentage is
  returned, percpu=True will return a percentage per cpu."""

cu = psutil.cpu_percent(interval=0.1, percpu=True)
print(cu)
