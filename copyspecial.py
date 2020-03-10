#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "troyerjl with help from benjmm, knmarvel, and Janell.Huyck"


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    path_codex = r"__(.+?)__"
    special_paths = []
    for file_ in os.listdir(dir):
        file_match = re.search(path_codex, file_)
        if file_match:
            path = os.path.join(dir, file_)
            special_paths.append(os.path.abspath(path))
    if special_paths == []:
        print("No special files found in "+dir)
    print(special_paths)
    return special_paths


def copy_to(paths, dir):
    for file_ in paths:
        shutil.copy(file_, dir)


def zip_to(paths, zippath):
    cmd = ["zip", "-j", zippath]
    cmd.extends(paths)
    subprocess.run(cmd)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument(
        'dirs', type=str, help="location(s) in which to search", nargs="+")
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.
    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with
    # required args, the general rule is to print a usage message and exit(1).
    paths = []
    for dir in args.dirs:
        paths.extend(get_special_paths(dir))
    if not args.dirs and not args.tozip:
        print("Path List: ")
        for path in paths:
            print(path)
    if args.todir:
        copy_to(paths, args.todir)
    if args.tozip:
        zip_to(paths, args.tozip)


if __name__ == "__main__":
    main()
