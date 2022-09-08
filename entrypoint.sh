#!/bin/bash

source /root/.bashrc

conda activate mlops-workshop-d2d

jupyter notebook --allow-root --ip 0.0.0.0 --NotebookApp.token='' --NotebookApp.password=''
