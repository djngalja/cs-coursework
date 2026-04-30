#include "cat.h"

int parse_flags(struct flags *active_flags, int argc, char **argv) {
  int error = 0;
  int i = 1;
  while (error == 0 && i < argc && argv[i][0] == '-') {
    if (argv[i][1] == '-') {
      if (strcmp(argv[i], "--number-nonblank") == 0) {
        active_flags->b = 1;
      } else if (strcmp(argv[i], "--squeeze-blank") == 0) {
        active_flags->s = 1;
      } else if (strcmp(argv[i], "--number") == 0) {
        active_flags->n = 1;
      } else {
        printf("ERROR: unknown flag <%s>\n", argv[i]);
        error = -1;
      }
    } else if (argv[i][1] != '\0') {
      error = parse_short_flags(active_flags, argv[i] + 1);
    }
    ++i;
  }
  if (active_flags->b) {
    active_flags->n = 0;
  }
  return error;
}

int parse_short_flags(struct flags *active_flags, char *ptr) {
  int error = 0;
  while (*ptr && error == 0) {
    switch (*ptr) {
      case 'b': {
        active_flags->b = 1;
        break;
      }
      case 'e': {
        active_flags->E = 1;
        active_flags->v = 1;
        break;
      }
      case 'E': {
        active_flags->E = 1;
        break;
      }
      case 'v': {
        active_flags->v = 1;
        break;
      }
      case 'n': {
        active_flags->n = 1;
        break;
      }
      case 's': {
        active_flags->s = 1;
        break;
      }
      case 't': {
        active_flags->T = 1;
        active_flags->v = 1;
        break;
      }
      case 'T': {
        active_flags->T = 1;
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

int validate_f_names(int argc, char **argv, int *first_file_id) {
  int error = 0;
  int i = 1;
  while (error == 0 && i < argc) {
    if (argv[i][0] != '-') {
      if (*first_file_id == 0) {
        *first_file_id = i;
      }
      FILE *fptr = fopen(argv[i], "r");
      if (!fptr) {
        printf("ERROR: unable to open file <%s>\n", argv[i]);
        error = -1;
      } else {
        fclose(fptr);
      }
    }
    ++i;
  }
  return error;
}

void cat(const char *f_name, const struct flags *active_flags, int *cnt,
         char *last_char, int *cnt_blank) {
  FILE *fptr = fopen(f_name, "r");
  if (!fptr) {
    printf("ERROR: unable to open file <%s>\n", f_name);
  } else {
    char current_char;
    while ((current_char = fgetc(fptr)) != EOF) {
      if ((active_flags->n == 1 && *last_char == '\n') ||
          (active_flags->b == 1 && *last_char == '\n' &&
           current_char != '\n')) {
        printf("%6d\t", *cnt);
        ++(*cnt);
      }
      cnt_blank_lines(active_flags, last_char, cnt_blank, current_char);
      print_line_endings(active_flags, last_char, current_char);
      convert_control_chars(active_flags, &current_char);
      if (active_flags->T == 1 && current_char == '\t') {
        printf("^");
        current_char += 64;
      }
      print_char(active_flags, cnt_blank, current_char, last_char);
      *last_char = current_char;
    }
    if (active_flags->E == 1 && *last_char == '\r') {
      putchar(*last_char);
    }
    fclose(fptr);
  }
}

void cnt_blank_lines(const struct flags *active_flags, const char *last_char,
                     int *cnt_blank, char current_char) {
  if (active_flags->s == 1) {
    if (current_char == '\n' && *last_char == '\n') {
      ++(*cnt_blank);
    } else {
      *cnt_blank = 0;
    }
  }
}

void print_line_endings(const struct flags *active_flags, const char *last_char,
                        char current_char) {
  if (active_flags->E == 1 && current_char == '\n') {
    if (*last_char == '\r') {
      printf("^M");
    }
    printf("$");
  }
}

void convert_control_chars(const struct flags *active_flags,
                           char *current_char) {
  if (active_flags->v == 1) {
    if (*current_char == 127) {
      printf("^");
      *current_char = '?';
    } else if (*current_char < 32 && *current_char != '\n' &&
               *current_char != '\t') {
      printf("^");
      *current_char += 64;
    }
  }
}

void print_char(const struct flags *active_flags, const int *cnt_blank,
                int current_char, const char *last_char) {
  if (*cnt_blank <= 1 && !(current_char == '\r' && active_flags->E == 1)) {
    if (active_flags->E == 1 && *last_char == '\r' && current_char != '\n') {
      putchar(*last_char);
    }
    putchar(current_char);
  }
}
