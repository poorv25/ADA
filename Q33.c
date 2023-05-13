#include <stdio.h>

int gcd(int a, int b) {
    // Base case: if one of the numbers is 0, the GCD is the other number
    if (a == 0) {
        return b;
    }
    if (b == 0) {
        return a;
    }
    // Recursive case: compute the GCD using Euclid's algorithm
    int remainder = a % b;
    return gcd(b, remainder);
}

int main() {
    int a, b;
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    int result = gcd(a, b);
    printf("The GCD of %d and %d is %d.\n", a, b, result);
    return 0;
}
