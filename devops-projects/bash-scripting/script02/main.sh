#!/bin/bash

. ./utils

start=$(date +%s)

if [[ $# == 0 ]]
then
    MY_PATH="./"
elif [[ ${1:(-1)} != "/" ]] 
then
    MY_PATH="$1/"
else 
    MY_PATH="$1"
fi

if [[ -d "$MY_PATH" ]]
then 
    print_report
else
    echo "[Error] main.sh: "$1" is not a directory"
fi

end=$(date +%s)
echo -e "\033[1;32;44mScript execution time (in seconds) =\033[0m $((end - start))"