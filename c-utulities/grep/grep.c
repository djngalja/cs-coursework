#include "grep.h"

// INPUT PARSING
int parse_input(struct grep_input *input, int argc, char **argv) {
  int error = 0;
  for (int i = 1; i < argc && error == 0; ++i) {
    // flags
    if (argv[i][0] == '-') {
      if (argv[i][1] == '\0') {
        error = -1;
        error_no_flag(input);
      } else if (input->e == 1 && input->num_e > input->num_e_patterns) {
        error = -1;
        error_no_pattern(input);
      } else if (input->f == 1 && input->pattern_file == NULL) {
        error = -1;
        error_no_file(input);
      } else {
        error = parse_flags(input, argv[i] + 1);
      }
    }
    // patterns
    else if (input->f == 1 && input->pattern_file == NULL) {
      input->pattern_file = argv[i];
    } else if (input->e == 1 && input->num_e > input->num_e_patterns) {
      input->patterns[input->num_e_patterns] = argv[i];
      ++(input->num_e_patterns);
    } else if (input->e == 0 && input->f == 0 && input->pattern == NULL) {
      input->pattern = argv[i];
    }
    // files
    else if (input->first_file_id == 0) {
      input->first_file_id = i;
    }
  }
  error = parsing_final_check(input);
  return error;
}

void error_no_flag(const struct grep_input *input) {
  if (input->s == 0) {
    printf("ERROR: flag not given\n");
  }
}

void error_no_pattern(const struct grep_input *input) {
  if (input->s == 0) {
    printf("ERROR: pattern not given\n");
  }
}

void error_no_file(const struct grep_input *input) {
  if (input->s == 0) {
    printf("ERROR: file not given\n");
  }
}

int parse_flags(struct grep_input *input, char *ptr) {
  int error = 0;
  while (*ptr && error == 0) {
    switch (*ptr) {
      case 'e': {
        input->e = 1;
        ++(input->num_e);
        break;
      }
      case 'i': {
        input->i = 1;
        break;
      }
      case 'v': {
        input->v = 1;
        break;
      }
      case 'c': {
        input->c = 1;
        break;
      }
      case 'l': {
        input->l = 1;
        break;
      }
      case 'n': {
        input->n = 1;
        break;
      }
      case 'h': {
        input->h = 1;
        break;
      }
      case 's': {
        input->s = 1;
        break;
      }
      case 'f': {
        input->f = 1;
        break;
      }
      case 'o': {
        input->o = 1;
        break;
      }
      default: {
        printf("ERROR: unknown flag <-%c>\n", *ptr);
        error = -1;
        break;
      }
    }
    ++ptr;
  }
  return error;
}

int parsing_final_check(const struct grep_input *input) {
  int error = 0;
  if (input->e == 1) {
    if (input->num_e == 0 || input->num_e != input->num_e_patterns) {
      error = -1;
      error_no_pattern(input);
    }
  }
  if (error == 0 && input->f == 1) {
    if (input->pattern_file == NULL) {
      error = -1;
      error_no_file(input);
    } else {
      error = validate_file(input->pattern_file, input);
    }
  }
  if (error == 0 && input->f == 0 && input->e == 0) {
    if (input->pattern == NULL) {
      error = -1;
      error_no_pattern(input);
    }
  }
  if (error == 0 && input->first_file_id == 0) {
    error = -1;
    error_no_file(input);
  }
  return error;
}

// FILE VALIDATION
int validate_f_names(int argc, char **argv, const struct grep_input *input) {
  int error = 0;
  for (int i = input->first_file_id; i < argc && error == 0; ++i) {
    error = validate_file(argv[i], input);
  }
  return error;
}

int validate_file(const char *f_name, const struct grep_input *input) {
  int error = 0;
  FILE *fptr = fopen(f_name, "r");
  if (!fptr) {
    error = -1;
    if (input->s == 0) {
      printf("ERROR: unable to open file <%s>\n", f_name);
    }
  } else {
    fclose(fptr);
  }
  return error;
}

// GREP
void grep(const struct grep_input *input, int argc, char **argv) {
  const int num_files = argc - input->first_file_id;
  for (int i = input->first_file_id; i < argc; ++i) {
    FILE *fptr = fopen(argv[i], "r");
    if (fptr) {
      int cnt_match_lines = 0;
      int cnt_lines = 0;
      char line[1024];
      while (fgets(line, sizeof(line), fptr)) {
        ++cnt_lines;
        int res = search_line(input, line, num_files, argv[i], cnt_lines);
        print_f_name(input, res, num_files, argv[i]);
        print_line_num(input, res, cnt_lines);
        print_matched_line(input, res, line);
        cnt_match_lines += res;
      }
      fclose(fptr);
      if (input->l == 1 && cnt_match_lines != 0) {
        printf("%s\n", argv[i]);
      }
      if (num_files > 1 && input->h == 0 && input->c == 1 && input->l == 0) {
        printf("%s:", argv[i]);
      }
      if (input->c == 1 && input->l == 0) {
        printf("%d\n", cnt_match_lines);
      }
    }
  }
}

int search_line(const struct grep_input *input, const char *line, int num_files,
                const char *f_name, int cnt_lines) {
  int cnt_match_lines = 0;
  int match_found = input->v == 1 ? REG_NOMATCH : 0;
  if (input->pattern != NULL) {
    if (call_search_pattern(input, input->pattern, line, num_files, f_name,
                            cnt_lines) == 0) {
      ++cnt_match_lines;
    }
  }
  if (input->num_e != 0) {
    for (int i = 0; i < input->num_e; ++i) {
      if (call_search_pattern(input, input->patterns[i], line, num_files,
                              f_name, cnt_lines) == 0) {
        ++cnt_match_lines;
      }
    }
  }
  if (input->pattern_file != NULL) {
    search_file(input, line, num_files, f_name, cnt_lines, &cnt_match_lines);
  }
  int res = cnt_match_lines == 0 ? REG_NOMATCH : 0;
  return res == match_found ? 1 : 0;
}

int call_search_pattern(const struct grep_input *input, const char *pattern,
                        const char *line, int num_files, const char *f_name,
                        int cnt_lines) {
  int res = 0;
  if (input->o == 1) {
    res = search_pattern_o(input, pattern, line, num_files, f_name, cnt_lines);
  } else {
    res = search_pattern(input, pattern, line);
  }
  return res;
}

int search_pattern_o(const struct grep_input *input, const char *pattern,
                     const char *line, int num_files, const char *f_name,
                     int cnt_lines) {
  int flag = set_flags(input);
  char sp[] = "\\*";
  if (strcmp(pattern, "*") == 0) {
    pattern = sp;
  }
  regex_t regex;
  regmatch_t match;
  int res = regcomp(&regex, pattern, flag);
  int cnt_matches = 0;
  if (res == 0) {
    const char *line_copy = line;
    int exit_cond = 0;
    while ((res = regexec(&regex, line_copy, 1, &match, 0)) == 0 &&
           exit_cond == 0) {
      if (strcmp(pattern, ".") == 0 && line_copy[match.rm_so] == '\n') {
        exit_cond = -1;
      } else {
        int start = match.rm_so;
        int end = match.rm_eo;
        print_f_name_o(input, num_files, f_name);
        print_line_num_o(input, cnt_lines);
        print_matched_pattern(input, start, end, line_copy);
        line_copy += end;
        ++cnt_matches;
      }
    }
  }
  regfree(&regex);
  return cnt_matches > 0 ? 0 : REG_NOMATCH;
}

int set_flags(const struct grep_input *input) {
  int flags = REG_EXTENDED;
  if (input->i == 1) {
    flags |= REG_ICASE;
  }
  return flags;
}

void print_f_name_o(const struct grep_input *input, int num_files,
                    const char *f_name) {
  if (num_files > 1 && input->v == 0 && input->c == 0 && input->l == 0) {
    printf("%s:", f_name);
  }
}

void print_line_num_o(const struct grep_input *input, int cnt_lines) {
  if (input->v == 0 && input->c == 0 && input->l == 0 && input->n == 1) {
    printf("%d:", cnt_lines);
  }
}

void print_matched_pattern(const struct grep_input *input, int start, int end,
                           const char *line) {
  if (input->v == 0 && input->c == 0 && input->l == 0) {
    printf("%.*s\n", end - start, line + start);
  }
}

int search_pattern(const struct grep_input *input, const char *pattern,
                   const char *line) {
  int flag = set_flags(input);
  char sp[] = "\\*";
  if (strcmp(pattern, "*") == 0) {
    pattern = sp;
  }
  regex_t regex;
  int res = regcomp(&regex, pattern, flag);
  if (res == 0) {
    res = regexec(&regex, line, 0, NULL, 0);
    if (strcmp(pattern, ".") == 0 && strlen(line) == 1 && line[0] == '\n') {
      res = res == 0 ? REG_NOMATCH : 0;
    }
  }
  regfree(&regex);
  return res;
}

void search_file(const struct grep_input *input, const char *line,
                 int num_files, const char *f_name, int cnt_lines,
                 int *cnt_match_lines) {
  FILE *fptr = fopen(input->pattern_file, "r");
  if (fptr) {
    char pattern[1024];
    while (fgets(pattern, sizeof(pattern), fptr)) {
      remove_trailing_n(pattern);
      if (call_search_pattern(input, pattern, line, num_files, f_name,
                              cnt_lines) == 0) {
        ++(*cnt_match_lines);
      }
    }
    fclose(fptr);
  }
}

void remove_trailing_n(char *pattern) {
  int len = strlen(pattern);
  if (len > 0 && pattern[len - 1] == '\n') {
    pattern[len - 1] = '\0';
  }
}

void print_f_name(const struct grep_input *input, int res, int num_files,
                  const char *f_name) {
  if (res == 1 && num_files > 1 && input->l == 0 && input->h == 0 &&
      input->c == 0 && input->o == 0) {
    printf("%s:", f_name);
  }
}

void print_line_num(const struct grep_input *input, int res, int cnt_lines) {
  if (res == 1 && input->c == 0 && input->l == 0 && input->n == 1 &&
      input->o == 0) {
    printf("%d:", cnt_lines);
  }
}

void print_matched_line(const struct grep_input *input, int res,
                        const char *line) {
  if (res == 1 && input->c == 0 && input->l == 0 && input->o == 0) {
    printf("%s", line);
  }
}

// testing
/* void print_grep_input(const struct grep_input *input, char **argv) {
  printf("=== Input Structure ===\nFlags:\n");

  printf("  -e: %d\n", input->e);
  printf("  -i: %d\n", input->i);
  printf("  -v: %d\n", input->v);
  printf("  -c: %d\n", input->c);
  printf("  -l: %d\n", input->l);
  printf("  -n: %d\n", input->n);
  printf("  -h: %d\n", input->h);
  printf("  -s: %d\n", input->s);
  printf("  -f: %d\n", input->f);
  printf("  -o: %d\n", input->o);

  printf("Pattern file (-f): %s\n",
         input->pattern_file ? input->pattern_file : "(null)");
  printf("Single pattern: %s\n", input->pattern ? input->pattern : "(null)");
  printf("Patterns from -e (%d total):\n", input->num_e);
  for (int i = 0; i < input->num_e && i < 100; i++) {
    printf("  [%d]: %s\n", i,
           input->patterns[i] ? input->patterns[i] : "(null)");
  }

  printf("num_e: %d\n", input->num_e);
  printf("num_e_patterns: %d\n", input->num_e_patterns);

  printf("First file: %s\n", argv[input->first_file_id]);
  printf("========================\n");
} */
