#!/bin/bash


# move to the source dir and activate the virtual environment
. venv/bin/activate

cd src


# spin up the data API
python main.py


# 
deactivate

