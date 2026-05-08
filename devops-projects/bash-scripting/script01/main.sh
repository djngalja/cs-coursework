#!/bin/bash

. ./utils
. ./design.conf

if [[ -z $column1_background || -z $column1_font_color || -z $column2_background || -z $column2_font_color ]]
then
    #default color map: do NOT change
    column1_background=2 #green
    column1_font_color=4 #blue
    column2_background=5 #magenta
    column2_font_color=7 #white
fi

if [[ "$column1_background" =~ ^[0-7]$ && "$column1_font_color" =~ ^[0-7]$ && "$column2_background" =~ ^[0-7]$ && "$column2_font_color" =~ ^[0-7]$ ]]
then
    if [[ $column1_background == $column1_font_color || $column2_background == $column2_font_color ]]
    then 
        echo "[Error] design.conf: font and background colors must not match"
    else 
        get_design_vars
        get_sys_info
        print_sys_info
        echo
        read -p "Save data? [Y / N]" reply
        if [[ $reply == "y" || $reply == "Y" ]]
        then
            f_name="$(date +"%d_%m_%y_%H_%M_%S").status"
            print_sys_info_file >> $f_name
            echo "File $f_name was saved"
        else
            echo "File was NOT saved"
        fi
    fi
else
    echo "[Error] design.conf: wrong format parameters"
fi