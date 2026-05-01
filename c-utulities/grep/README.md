# Grep Utility
Custom implementation of the `grep` command-line utility for searching patterns inside text files.

## Features
- **Pattern matching**
- **Supported Flags**:
  - `-e`: Specify multiple patterns
  - `-i`: Case-insensitive matching
  - `-v`: Invert match (show non-matching lines only)
  - `-c`: Show only count of matching lines
  - `-l`: Show only filenames containing matches
  - `-n`: Show line numbers
  - `-h`: Suppress filename prefixes in multi-file output
  - `-s`: Suppress error messages
  - `-o`: Show only matching parts of lines
  - `-f`: Read patterns from a file
- **All two-flag combinations**: e.g., `-iv`, `-nc`, `-sl`
- **Multi-file Support**: Process multiple files simultaneously
- **Compatible with POSIX `grep`**

## Build
```bash
make                 # Build the executable (creates 'grep')
make all             # Same as 'make'
make clean           # Remove built executable
make rebuild         # Clean and rebuild
```

## Usage
```bash
./grep [flags...] pattern [files...]
./grep [flag] -f pattern_file [files...]
./grep [flag] -e pattern1 -e pattern2 [files...]
```

## Examples
```bash
./grep hello file.txt
./grep -e hello -e world file.txt
./grep -f patterns.txt file.txt
./grep -iv hello file.txt
```
