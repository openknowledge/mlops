#!/bin/bash

source /root/.bashrc

export SHELL=/bin/bash
jupyter notebook --allow-root --ip 0.0.0.0 --NotebookApp.token='' --NotebookApp.password=''&
jupyter lab --port 8889 --allow-root --ip 0.0.0.0 --NotebookApp.token='' --NotebookApp.password=''
