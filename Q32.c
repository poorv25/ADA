#include <stdio.h>

int fibonacci(int n) {
    // Base case: the first two Fibonacci numbers are 0 and 1
    if (n == 0 || n == 1) {
        return n;
    }
    // Recursive case: compute the nth Fibonacci number using divide-and-conquer
    int smallerFib1 = fibonacci(n - 1);
    int smallerFib2 = fibonacci(n - 2);
    int result = smallerFib1 + smallerFib2;
    return result;
}

int main() {
    int n;
    printf("Enter a non-negative integer: ");
    scanf("%d", &n);
    if (n < 0) {
        printf("Error: input must be a non-negative integer.\n");
        return 1;
    }
    int result = fibonacci(n);
    printf("The %dth Fibonacci number is %d.\n", n, result);
    return 0;
}
