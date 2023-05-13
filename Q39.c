#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INF 1e9

typedef struct {
    double x, y;
} Point;

int cmpx(const void *a, const void *b) {
    Point *p1 = (Point *)a, *p2 = (Point *)b;
    return (p1->x - p2->x);
}

int cmpy(const void *a, const void *b) {
    Point *p1 = (Point *)a, *p2 = (Point *)b;
    return (p1->y - p2->y);
}

double dist(Point p1, Point p2) {
    return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}

double brute_force(Point P[], int n) {
    double min_dist = INF;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (dist(P[i], P[j]) < min_dist) {
                min_dist = dist(P[i], P[j]);
            }
        }
    }
    return min_dist;
}

double strip_closest(Point strip[], int size, double d) {
    double min_dist = d;
    qsort(strip, size, sizeof(Point), cmpy);
    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size && (strip[j].y - strip[i].y) < min_dist; j++) {
            if (dist(strip[i], strip[j]) < min_dist) {
                min_dist = dist(strip[i], strip[j]);
            }
        }
    }
    return min_dist;
}

double closest_util(Point P[], int n) {
    if (n <= 3) {
        return brute_force(P, n);
    }
    int mid = n / 2;
    Point mid_point = P[mid];
    double dl = closest_util(P, mid);
    double dr = closest_util(P + mid, n - mid);
    double d = fmin(dl, dr);
    Point strip[n];
    int j = 0;
    for (int i = 0; i < n; i++) {
        if (fabs(P[i].x - mid_point.x) < d) {
            strip[j] = P[i];
            j++;
        }
    }
    return fmin(d, strip_closest(strip, j, d));
}

double closest(Point P[], int n) {
    qsort(P, n, sizeof(Point), cmpx);
    return closest_util(P, n);
}

int main() {
    Point P[] = {{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}};
    int n = sizeof(P) / sizeof(P[0]);
    printf("The smallest distance is %lf\n", closest(P, n));
    return 0;
}
