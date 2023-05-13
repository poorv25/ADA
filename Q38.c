#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int getNumLength(int num) {
    int length = 0;
    while (num != 0) {
        length++;
        num /= 10;
    }
    return length;
}

int power(int base, int exponent) {
    if (exponent == 0) {
        return 1;
    } else if (exponent % 2 == 0) {
        int result = power(base, exponent/2);
        return result * result;
    } else {
        return base * power(base, exponent-1);
    }
}

int karatsuba(int x, int y) {
    int xLen = getNumLength(x);
    int yLen = getNumLength(y);
    int n = fmax(xLen, yLen);
    if (n == 1) {
        return x * y;
    }
    int m = ceil(n/2.0);
    int powerOf10 = power(10, m);

    int a = x / powerOf10;
    int b = x % powerOf10;
    int c = y / powerOf10;
    int d = y % powerOf10;

    int ac = karatsuba(a, c);
    int bd = karatsuba(b, d);
    int ad_plus_bc = karatsuba(a+b, c+d) - ac - bd;

    return ac * powerOf10*2 + ad_plus_bc * powerOf10 + bd;
}

int main() {
    int x = 123456789;
    int y = 987654321;
    int result = karatsuba(x, y);
    printf("The result of multiplying %d and %d is %d.\n", x, y, result);
    return 0;
}
