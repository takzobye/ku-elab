/*

Fibonacci Array
ให้เขียนฟังก์ชัน unsigned long *fibo_array(unsigned int n, double *golden_ratio); ที่คืนค่า array ของเลขฟิโบนัชชีจำนวน n ตัวแรก และคำนวณอัตราส่วนทองคำของเลขฟิโบนัชชีใน array เก็บไว้ที่ pointer golden_ratio

เลขฟิโบนัชชี หาได้จาก ผลรวมของตัวเลข 2 ตัวก่อนหน้า หรือ F[i] = F[i - 1] + F[i - 2] เมื่อ F[0] = 0 และ F[1] = 1

อัตราส่วนทองคำ หาได้จาก อัตราส่วนของเลขฟิโบนัชชีลำดับที่ n + 1 ต่อเลขฟิโบนัชชีลำดับที่ n

ตัวอย่าง array ของเลขฟิโบนัชชี 10 ตัวแรก คือ {0, 1, 1, 2, 3, 5, 8, 13, 21, 34} ซึ่งมีอัตราส่วนทองคำ คือ F[11] / F[10] = 89 / 55

*/

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