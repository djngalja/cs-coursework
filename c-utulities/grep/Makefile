CFLAGS = -std=c11 -Wall -Wextra -Werror

.PHONY: all test clean rebuild

all: grep

grep: main.c grep.c grep.h
	 gcc $(CFLAGS) -o grep main.c grep.c
   
clean:
	 rm -f grep
    
rebuild: clean all