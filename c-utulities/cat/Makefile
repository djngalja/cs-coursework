CFLAGS = -std=c11 -Wall -Wextra -Werror

.PHONY: all test clean rebuild

all: cat

cat: main.c cat.c cat.h
	 gcc $(CFLAGS) -o cat main.c cat.c
    
clean:
	 rm -f cat
    
rebuild: clean all
