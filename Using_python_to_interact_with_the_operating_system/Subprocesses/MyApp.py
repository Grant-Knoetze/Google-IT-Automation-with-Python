#!/usr/bin/env python3

import os
import subprocess

my_env = os.environ.copy() # Copy the environment seen by our process.
"""Modify the contents of the PATH environment variable
by adding a directory to it."""
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env) # Call myapp command setting env parameter to our newly prepared environment.
