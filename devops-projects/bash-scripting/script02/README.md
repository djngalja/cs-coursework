![Bash Script](https://img.shields.io/badge/bash_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)

## Directory Analysis Script
A Bash script that analyzes a specified directory and provides detailed statistics about its contents.

### Usage
Clone this repository and run `main.sh` file. Before running the script, make sure it's executable:

```
chmod +x main.sh
./main.sh [directory_path]
```
If no directory path is provided, the script will analyze the current directory (`./`).

### Features
- The script generates a report containing:
    - Total number of directories (including nested ones)
    - Top 10 largest directories
    - Total number of files
    - Total number of
        - configuration files
        - text files
        - executable files
        - log files
        - archive files
    - Top 10 largest files
    - Top 10 largest executable files
    - Execution time: Total time taken to complete the analysis

- All file size calculations and rankings are performed using standard Unix `find` commands
- Results are displayed with formatted colored output for better readability