#!/bin/bash


# simple python web server
#python -m SimpleHTTPServer


# move to the source dir and activate the virtual environment
cd ../src
. ../venv/bin/activate


# spin up the data API
python main.py


# 
deactivate

