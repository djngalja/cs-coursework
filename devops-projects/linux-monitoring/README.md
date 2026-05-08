![Bash Script](https://img.shields.io/badge/bash_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)

# Linux Monitoring
My solutions to a system monitoring assignment, tested on _Ubuntu Server 20.04 LTS_. 

## ex01. File generator

A bash script that generates directories and fills them with files:
- Uses given character sets (e.g. `ABC`) for names
- __Naming rules__: min 4 chars + `_DDMMYY`(e.g. `ABCC_080526`), preserves char order (`baaa` invalid if `ab` given)
- Terminates automatically at 1GB free space threshold  
- Logs every created file/directory (path, timestamp, file size) <br />

__Usage example__: <br />
![Usage example](readme_img/ex01/img01.png)

## ex02. Filesystem Clogger

A bash script that fills the system with files across multiple locations until only 1GB of free space remains:
- Uses `INIT_DIR` (a variable in `main.sh`, defaulting to `./TEST`) as the base for generating directories
- Creates up to 100 directiories in multiple locations, __never__ in paths containing `bin` or `sbin`
- Generates a different number of files (up to 100) in each directory 
- Uses given character sets (e.g. `ABC`) for names
- __Naming rules__: min 4 chars + `_DDMMYY`(e.g. `ABCC_080526`), preserves char order (`baaa` invalid if `ab` given)
- Terminates automatically at 1GB free space threshold  
- Logs every created file/directory (path, timestamp, file size) 
- Prints and logs its start time, end time and total runtime<br />

__Usage example__: <br />
![Usage example](readme_img/ex02/img01.png)

## ex03. Cleanup Utility

A bash script that deletes files and directories created by `ex02`.

__Usage example__:
```
./main.sh 1    # Delete using the log file
./main.sh 2    # Delete using time range (prompts for start/end)
./main.sh 3    # Delete by name pattern [A-Za-z]+_[0-9]{6}
```