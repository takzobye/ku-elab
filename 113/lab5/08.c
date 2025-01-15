#include <stdio.h>

int main()
{
    int current_step = 0;
    int stairs = 0;
    int round = 1;

    printf("Input number of stairs: ");
    scanf("%d", &stairs);

    current_step = stairs;

    while (1)
    {
        printf("---- round %d ----\n", round);

        for (int i = 1; i <= stairs; i++)
        {
            if (i == current_step - 1)
            {
                printf("|-O-|\n");
            }
            else if (i == current_step)
            {
                printf("|-^-|\n");
            }
            else
            {
                printf("|---|\n");
            }
        }

        round++;

        int step = 0;

        printf("Input step command: ");
        scanf("%d", &step);

        if (step == 0)
        {
            break;
        }

        int temp = current_step;

        if (step > 0)
        {
            current_step -= step;
        }
        else
        {
            current_step += -step;
        }

        if (current_step < 2)
        {
            current_step = 2;
        }
        else if (current_step > stairs)
        {
            current_step = stairs;
        }
    }

    return 0;
}