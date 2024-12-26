#include <stdio.h>

int main() {
    int suitNumber;
    scanf("%d", &suitNumber);

    switch (suitNumber) {
        case 1:
            printf("Масть: пики\n");
            break;
        case 2:
            printf("Масть: трефы\n");
            break;
        case 3:
            printf("Масть: бубны\n");
            break;
        case 4:
            printf("Масть: червы\n");
            break;
    }

    return 0;
}