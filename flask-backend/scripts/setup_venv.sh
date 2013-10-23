#!/bin/bash

# move & remove
cd ..
rm -rf venv

# virtual environment setup
virtualenv venv --distribute --no-site-packages
. venv/bin/activate

# install tools
pip install Flask
pip install ystockquote

# 
deactivate
