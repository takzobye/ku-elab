#include <stdio.h>
int main()
{
    float preGrade = 1.75;
    int preCredit = 21;
    int credit = 18;
    float requiredGrade = 2.00;

    // Start Block

    int totalCredit = preCredit + credit;
    float preGradeMulCredit = preCredit * preGrade;
    float totalGradeMulCredit = requiredGrade * totalCredit;
    float currentGradeMulCredit = (totalGradeMulCredit) - preGradeMulCredit;
    float targetCurrentGrade = currentGradeMulCredit / credit;

    printf("The GPA this semester should be %.2f", targetCurrentGrade);

    // End Block

    return 0;
}