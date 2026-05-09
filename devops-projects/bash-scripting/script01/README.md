![Bash Script](https://img.shields.io/badge/bash_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![VirtualBox](https://img.shields.io/badge/virtualbox-%23183A61.svg?style=for-the-badge&logo=virtualbox&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

## System Information Script
A Bash script that collects and displays system information with customizable colors. 

### Usage
Clone this repository and run `main.sh` file. Before running the script, make sure it's executable:

```
chmod +x main.sh
./main.sh
```
Edit `design.conf` file to set custom colors. Default colors will be used if configuration is missing or invalid.

### Features
The script will:
- Load configuration from `design.conf`

- Display system information with chosen colors:
    - HOSTNAME
    - TIMEZONE
    - USER
    - OS
    - DATE
    - UPTIME
    - UPTIME_SEC
    - IP
    - MASK
    - GATEWAY
    - RAM_TOTAL
    - RAM_USED
    - RAM_FREE
    - SPACE_ROOT
    - SPACE_ROOT_USED
    - SPACE_ROOT_FREE

- Prompt to save the output to a timestamped file:
    - Type `Y`/`y` and press `Enter` to save the output
    - The script saves system information to a file named with the current timestamp in the format `DD_MM_YY_HH_MM_SS.status`