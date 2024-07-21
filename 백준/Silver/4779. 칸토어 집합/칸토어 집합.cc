#include <stdio.h>

int d[1000000] = {0};

void f(int n, int s){
    if (n <= 0) {
        return;
    }
    n /= 3;
    f(n, s);
    for (int i = s + n; i < s + 2 * n; i++) {
        d[i] = 1;
    }
    f(n, s + 2*n);
}
int main() {
    int n;
    while (scanf("%d", &n) != EOF) {
        int v = 1;
        for (int i = 0; i < 1000000; i++) {
            d[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            v *= 3;
        }
        f(v, 0);
        for (int i = 0; i < v; i++) {
            if(d[i]) {
                printf(" ");
            } else {
                printf("-");
            }
        }
        printf("\n");
    }
    return 0;
}
