#ifndef CAT_H
#define CAT_H

#include <stdio.h>
#include <string.h>

struct flags {
  int b, E, v, n, s, T;
};

int parse_flags(struct flags *active_flags, int argc, char **argv);
int parse_short_flags(struct flags *active_flags, char *ptr);
int validate_f_names(int argc, char **argv, int *first_file_id);
void cat(const char *f_name, const struct flags *active_flags, int *cnt,
         char *last_char, int *cnt_blank);
void cnt_blank_lines(const struct flags *active_flags, const char *last_char,
                     int *cnt_blank, char current_char);
void print_line_endings(const struct flags *active_flags, const char *last_char,
                        char current_char);
void convert_control_chars(const struct flags *active_flags,
                           char *current_char);
void print_char(const struct flags *active_flags, const int *cnt_blank,
                int current_char, const char *last_char);

#endif
