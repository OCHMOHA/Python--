#include <stdio.h>

int main() {
    int n = 5;
    unsigned long long sum = 0;
    unsigned long long a = 0, b = 1, next;

    for (int i = 0; i < n; i++) {
        sum += a;
        next = a + b;
        a = b;
        b = next;
    }

    printf("Сумму первых 30 чисел это: %llu\n", sum);
    return 0;
}