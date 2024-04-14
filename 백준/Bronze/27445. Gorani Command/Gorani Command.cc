#include <stdio.h>

int main() {
    int n, m, tmp, w = 51, h = 51, w_idx = 1, h_idx = 1;
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        scanf("%d", &tmp);
        if (tmp < h) {
            h = tmp;
            h_idx = i + 1;
        }
    }
    if (tmp < w) {
        w = tmp;
        w_idx = 1;
    }
    for(int i = 0 ; i < m - 1; i++) {
        scanf("%d", &tmp);
        if (tmp < w) {
            w = tmp;
            w_idx = i + 2;
        }
    }
    printf("%d %d", h_idx, w_idx);
    return 0;
}