/*

แปลงรูปแบบ 12-hour เป็น 24-hour
จงเขียนโปรแกรมที่รับเวลาในรูปแบบ 12-hour (เช่น 12:59 pm โดยคำว่า am/pm เป็น upper/lower case ก็ได้) แล้วแสดงผลลัพธ์เป็นเวลาเดียวกันในรูปแบบ 24-hour ดังตัวอย่าง

*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int hour, minute;
    char unit[3];

    printf("Enter a 12-hour time [eg. 12:34 am]: ");
    scanf("%d:%d %2s", &hour, &minute, unit);

    if (unit[0] == 'a' || unit[0] == 'A') {
        if (hour == 12) {
            printf("Equivalent 24-hour time: 00:%02d", minute);
        } else {
            printf("Equivalent 24-hour time: %02d:%02d", hour, minute);
        }
    } else {
        if (hour == 12) {
            printf("Equivalent 24-hour time: 12:%02d", minute);
        } else {
            printf("Equivalent 24-hour time: %02d:%02d", hour + 12, minute);
        }
    }

    return 0;
}