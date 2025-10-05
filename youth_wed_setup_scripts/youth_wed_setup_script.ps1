cd $PSScriptRoot\..

. ./python_env/bin/Activate.ps1
pip3 install -r ./requirements.txt
python3 youth_wed_setup.py
