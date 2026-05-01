#ifndef GREP_H
#define GREP_H

#include <regex.h>
#include <stdio.h>
#include <string.h>

struct grep_input {
  int e, i, v, c, l, n, h, s, f, o;
  char *pattern_file;  // f
  char *pattern;
  char *patterns[100];  // e
  int num_e;
  int num_e_patterns;
  int first_file_id;
};

// INPUT PARSING
int parse_input(struct grep_input *input, int argc, char **argv);
void error_no_flag(const struct grep_input *input);
void error_no_pattern(const struct grep_input *input);
void error_no_file(const struct grep_input *input);
int parse_flags(struct grep_input *input, char *ptr);
int parsing_final_check(const struct grep_input *input);
// FILE VALIDATION
int validate_f_names(int argc, char **argv, const struct grep_input *input);
int validate_file(const char *f_name, const struct grep_input *input);
// GREP
void grep(const struct grep_input *input, int argc, char **argv);
int search_line(const struct grep_input *input, const char *line, int num_files,
                const char *f_name, int cnt_lines);
int call_search_pattern(const struct grep_input *input, const char *pattern,
                        const char *line, int num_files, const char *f_name,
                        int cnt_lines);
int search_pattern_o(const struct grep_input *input, const char *pattern,
                     const char *line, int num_files, const char *f_name,
                     int cnt_lines);
int set_flags(const struct grep_input *input);
void print_f_name_o(const struct grep_input *input, int num_files,
                    const char *f_name);
void print_line_num_o(const struct grep_input *input, int cnt_lines);
void print_matched_pattern(const struct grep_input *input, int start, int end,
                           const char *line);
int search_pattern(const struct grep_input *input, const char *pattern,
                   const char *line);
void search_file(const struct grep_input *input, const char *line,
                 int num_files, const char *f_name, int cnt_lines,
                 int *cnt_match_lines);
void remove_trailing_n(char *pattern);
void print_f_name(const struct grep_input *input, int res, int num_files,
                  const char *f_name);
void print_line_num(const struct grep_input *input, int res, int cnt_lines);
void print_matched_line(const struct grep_input *input, int res,
                        const char *line);
// void print_grep_input(const struct grep_input *input, char **argv); //
// testing

#endif
