#!/bin/bash 

. ./utils

INIT_DIR="../02/TEST"

if [[ $# != 1 ]]
then
    echo "[Error] Wrong number of parameters: $#/1"
elif [[ ! $1 =~ ^[1-3]$ ]]
then
    echo "[Error] Wrong format: '$1' must be 1-3"
else
    sys_clean $1
fi