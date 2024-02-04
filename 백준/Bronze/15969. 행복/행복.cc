#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int minh = 1001, maxh = -1;
    
    for(int i = 0; i < n ; i ++){
        int a;
        scanf("%d", &a);
        if(minh > a) {
            minh = a;
        }
        if(maxh < a) {
            maxh = a;
        }
    }
    printf("%d", maxh - minh);
}