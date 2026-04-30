#include "cat.h"

int main(int argc, char **argv) {
  int error = 0;
  struct flags active_flags = {0, 0, 0, 0, 0, 0};
  int first_file_id = 0;
  if (argc < 2) {
    error = -1;
  }
  if (error == 0) {
    error = parse_flags(&active_flags, argc, argv);
  } else {
    printf("ERROR: filename not given\n");
  }
  if (error == 0) {
    error = validate_f_names(argc, argv, &first_file_id);
  }
  if (error == 0) {
    int cnt = 1;
    char last_char = '\n';
    int cnt_blank = 0;
    for (int i = first_file_id; i < argc; ++i) {
      cat(argv[i], &active_flags, &cnt, &last_char, &cnt_blank);
    }
  }
  return 0;
}
