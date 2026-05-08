#!/bin/bash 

. ./utils

file="/var/www/html/metrics.html"
temp_file="metrics.tmp"

if [[ $# != 0 ]]
then
    echo "[Error] Wrong number of parameters: $#/0"
else
    collect_stat
fi