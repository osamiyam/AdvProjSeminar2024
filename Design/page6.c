#include <stdio.h>
#include <stdlib.h>

void work();

int main() {
  work();
  return 0;
}

void work() {
  unsigned char p1 = 23;
  unsigned char p2 = 34;

  while (p2 > 0) {
    p1 += 1;
    p2 -= 1;
  }
  printf("%d\n", p1);
}

