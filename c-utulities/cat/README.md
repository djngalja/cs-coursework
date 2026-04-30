# Cat Utility

Custom implementation of the `cat` command-line utility for displaying text files.

## Features
- **File display**: output file contents to `stdout`
- **Supported Flags**:
  - `-b`, `--number-nonblank`: Number non-empty lines
  - `-e`: The same as `-v` and `-E` together
  - `-E`: Display `$` at end of lines (`^M$` for Windows files)
  - `-n`, `--number`: Number all lines
  - `-s`, `squeeze-blank`: Squeeze multiple blank lines into one
  - `-t`: Display non-printable characters (except for newlines)
  - `-T`: Display tab characters as `^I`
  - `-v`: Display non-printable characters (except for tabs and newlines)
- **Compatible with POSIX `cat`**

## Build

```bash
make                 # Build the executable (creates 'cat')
make all             # Same as 'make'
make clean           # Remove built executable
make rebuild         # Clean and rebuild
```

## Usage
```bash
./cat [flag] [files...]
./cat -n file.txt
./cat -e file1.txt file2.txt
```
