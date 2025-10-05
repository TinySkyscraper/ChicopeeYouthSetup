#!/bin/bash

script_name=$0
script_dir=$(dirname ${script_name})

cd ${script_dir}/..

source ./python_env/bin/activate
pip3 install -r ./requirements.txt
python3 youth_wed_setup.py
