#include <stdio.h>

int main(){
    float num1, num2; 

    printf("10 пар чисел:\n");

    for (int i = 1; i <= 10; i++) {
        printf("пар %d:\n", i);
        printf(" 1й чисел: ");
        scanf("%f", &num1);
        printf(" 2й чисел: ");
        scanf("%f", &num2);

        if (num1 > num2) {
            printf("The larger number is: %.2f\n", num1);
        } else if (num2 > num1) {
            printf("The larger number is: %.2f\n", num2);
        } else {
            printf("Both numbers are equal: %.2f\n", num1);
        }
    }

    return 0;
}