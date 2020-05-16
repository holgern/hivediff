#!/usr/bin/env python

from ui.mainwindow import *
import argparse

parser = argparse.ArgumentParser(description="hivediff - Tkinter GUI tool based on Python's difflib to view edits on Hive posts")
parser.add_argument('-a', '--authorperm', metavar=('authorperm'), nargs=1, help='Authorperm of a hive post', required=False)
parser.add_argument('-f', '--file', metavar=('file'), nargs=1, help='Markdown file with YAML header', required=False)

args = parser.parse_args()

authorperm = args.authorperm[0] if args.authorperm else None
file = args.file[0] if args.file else None

main_window = MainWindow()
main_window.start(authorperm, file)
