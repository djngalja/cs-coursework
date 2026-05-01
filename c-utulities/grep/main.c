#include "grep.h"

int main(int argc, char **argv) {
  int error = 0;
  struct grep_input input = {0, 0, 0,    0,    0,  0, 0, 0,
                             0, 0, NULL, NULL, {}, 0, 0, 0};
  if (argc < 2) {
    error = -1;
  }
  if (error == 0) {
    error = parse_input(&input, argc, argv);
    // print_grep_input(&input, argv); // testing
  } else {
    printf("ERROR: no input\n");
  }
  if (error == 0) {
    error = validate_f_names(argc, argv, &input);
  }
  if (error == 0) {
    grep(&input, argc, argv);
  }
  return 0;
}
