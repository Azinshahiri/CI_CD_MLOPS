#!/bin/bash

#!/bin/bash

echo [$(date)]: "START"
echo [$(date)]: "Creating env with Python version"
conda create --prefix ./env python=3.10 -y

echo [$(date)]: "Activating the environment"
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate ./env

echo "[$(date)]: Installing the requirements"
pip install -r requirements_dev.txt

echo "[$(date)]: END"
