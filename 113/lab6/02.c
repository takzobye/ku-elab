#include <stdio.h>
#include <stdlib.h>

unsigned long *fibo_array(unsigned int n, double *golden_ratio);

int main() {
    double golden_ratio;
    unsigned int n = 0;

    scanf("%d", &n);

    fibo_array(n, &golden_ratio);

    return 0;
}

unsigned long *fibo_array(unsigned int n, double *golden_ratio) {
    unsigned long *arr = (unsigned long *)malloc(n * sizeof(unsigned long));
    arr[0] = 0;
    arr[1] = 1;

    for (int i = 2; i < n; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
    }

    double extraNum1 = arr[n - 1] + arr[n - 2];
    double extraNum2 = arr[n - 1] + extraNum1;

    *golden_ratio = extraNum2 / extraNum1;

    return arr;
}