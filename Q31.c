#include <stdio.h>

int factorial(int n) {
    // Base case: the factorial of 0 is 1
    if (n == 0) {
        return 1;
    }
    // Recursive case: compute the factorial of n using divide-and-conquer
    int smallerFactorial = factorial(n - 1);
    int result = n * smallerFactorial;
    return result;
}

int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    if (n < 0) {
        printf("Error: input must be a positive integer.\n");
        return 1;
    }
    int result = factorial(n);
    printf("%d! = %d\n", n, result);
    return 0;
}
