#!/bin/bash 

. ./utils

start=$(date +%s)
start_h=$(date '+%d/%b/%Y:%H:%M:%S %z')

INIT_DIR="TEST"

if [[ $# != 3 ]]
then
    echo "[Error] Wrong number of parameters: $#/3"
elif [[ ! $1 =~ ^[a-zA-Z]{1,7}$ ]]
then
    echo "[Error] Wrong format: '$1' must contain 1-7 latin letters for directory names"
elif [[ ! $2 =~ ^[a-zA-Z]{1,7}\.[a-zA-Z]{1,3}$ ]]
then
    echo "[Error] Wrong format: '$2' must contain 1-7 letters for filenames, dot, 1-3 letters for extension"
elif [[ ! $3 =~ ^(100|[1-9][0-9]?)[mM][bB]$ ]]
then
    echo "[Error] Wrong format: '$3' must be 1-100 followed by 'mb' (case insensitive)"
else
    sys_clog $1 $2 $3
fi

end=$(date +%s)
end_h=$(date '+%d/%b/%Y:%H:%M:%S %z')

echo "Start time: $start_h" | tee -a file_generator.log
echo "End time: $end_h" | tee -a file_generator.log
echo "Script execution time (in seconds) : $((end - start))" | tee -a file_generator.log