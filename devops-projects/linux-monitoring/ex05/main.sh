#!/bin/bash 

. ./utils

if [[ $# != 1 ]]
then
    echo "[Error] Wrong number of parameters: $#/1"
elif [[ ! $1 =~ ^[1-4]$ ]]
then
    echo "[Error] Wrong format: '$1' must be 1-4"
else
    sys_monitor $1
fi