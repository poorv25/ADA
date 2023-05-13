#include <stdio.h>
#include <math.h>

double euclidean_distance(double x1, double y1, double x2, double y2) {
    if (x1 == x2 && y1 == y2) { // base case
        return 0;
    } else { // recursive case
        double mid_x = (x1 + x2) / 2;
        double mid_y = (y1 + y2) / 2;
        double left_distance = euclidean_distance(x1, y1, mid_x, mid_y);
        double right_distance = euclidean_distance(mid_x, mid_y, x2, y2);
        return sqrt(left_distance * left_distance + right_distance * right_distance);
    }
}

int main() {
    double x1, y1, x2, y2;
    printf("Enter the x and y coordinates of the first point (separated by a space): ");
    scanf("%lf %lf", &x1, &y1);
    printf("Enter the x and y coordinates of the second point (separated by a space): ");
    scanf("%lf %lf", &x2, &y2);
    double distance = euclidean_distance(x1, y1, x2, y2);
    printf("The Euclidean distance between the two points is: %lf\n", distance);
    return 0;
}
