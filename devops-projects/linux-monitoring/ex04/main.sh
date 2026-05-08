#!/bin/bash 

. ./data

if [[ $# != 0 ]]
then
    echo "[Error] Wrong number of parameters: $#/0"
else
    for (( i=0; i < 5; i++ ))
    do
        line_num=$(shuf -i 100-1000 -n 1)
        current_date=$(date -d "+$i days" '+%d/%b/%Y')
        timezone=$(date '+%z')
        f_name="combined_log_format_$(date -d "+$i days" '+%d_%b_%Y').log"
        for (( j=0; j < $line_num; j++ ))
        do
            ip="$(shuf -i 0-255 -n 1).$(shuf -i 0-255 -n 1).$(shuf -i 0-255 -n 1).$(shuf -i 0-255 -n 1)"
            hour=$(printf "%02d" $(shuf -i 0-23 -n 1))
            min=$(printf "%02d" $(shuf -i 0-59 -n 1))
            sec=$(printf "%02d" $(shuf -i 0-59 -n 1))
            method=${methods[$(shuf -i 0-4 -n 1)]}
            url=${urls[$(shuf -i 0-4 -n 1)]}
            code=${status_codes[$(shuf -i 0-9 -n 1)]}
            agent=${agents[$(shuf -i 0-7 -n 1)]}
            echo "$ip - - [$current_date:$hour:$min:$sec $timezone] \"$method $url HTTP/1.1\" $code - \"-\" \"$agent\""
        done | sort -k4 > $f_name
    done
fi