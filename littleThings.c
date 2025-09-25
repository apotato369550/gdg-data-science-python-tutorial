#include <stdio.h>

#define CONSTANT 3.14

int main () {

    float a = 3.14;
    int b = (int)a;   // explicit cast
    printf("%d\n", b);
    // outputs 3

    int i = 0;
    i++;
    // i is 1

    int iAmAVariable = 100;

    printf("Hello, %s\n", "Jay!");
    // Hello, Jay!

    return 0;
}