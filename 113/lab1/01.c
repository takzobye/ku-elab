#include<stdio.h>
int main() {
    int computer_time = 785;  // ในโปรแกรมตรวจอาจเปลี่ยนค่าของตัวแปรนี้ แต่นิสิตไม่ต้องเปลี่ยนค่าของตัวแปรนี้
    
    // Start Block

    int day = computer_time / (24 * 60);
    int hour = (computer_time / 60) - (day * 24);
    int minute = computer_time - ((day * 24 * 60) + (hour * 60));

    printf("It is %d days %d hours and %d minutes.", day, hour, minute);

    // End Block

    return 0;
}