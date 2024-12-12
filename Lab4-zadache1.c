#include <stdio.h>

int main() {
    printf("двузначных чисел,которые делятся на 4,но не делятся на 6:\n");
    for (int i = 10; i <= 99; i++) {
        if (i % 4 == 0 && i % 6 != 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
    return 0;
}
