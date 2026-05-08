#!/bin/bash 

. ./utils

if [[ $# != 6 ]]
then
    echo "[Error] Wrong number of parameters: $#/6"
elif [[ ! -d $1 ]]
then
    echo "[Error] Wrong format: '$1' is not a directory"
elif [[ ! $2 =~ ^[1-9][0-9]*$ ]]
then
    echo "[Error] Wrong format: '$2' is not a number of directories"
elif [[ ! $3 =~ ^[a-zA-Z]{1,7}$ ]]
then
    echo "[Error] Wrong format: '$3' must contain 1-7 latin letters for directory names"
elif [[ ! $4 =~ ^[1-9][0-9]*$ ]]
then
    echo "[Error] Wrong format: '$4' is not a number of files"
elif [[ ! $5 =~ ^[a-zA-Z]{1,7}\.[a-zA-Z]{1,3}$ ]]
then
    echo "[Error] Wrong format: '$5' must contain 1-7 letters for filenames, dot, 1-3 letters for extension"
elif [[ ! $6 =~ ^(100|[1-9][0-9]?)[kK][bB]$ ]]
then
    echo "[Error] Wrong format: '$6' must be 1-100 followed by 'kb' (case insensitive)"
else
    dirs_gen $1 $2 $3 $4 $5 $6
fi