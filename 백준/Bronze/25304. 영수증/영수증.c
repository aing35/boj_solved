#include <stdio.h>
#include <stdlib.h>

int main() {
    int X, N;
    int a, b;
    int sum = 0;

    scanf("%d", &X);
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d %d", &a, &b);
        sum += (a * b);
    }

    if (sum == X) {
        printf("Yes\n");
    }
    else {
        printf("No\n");
    }


    return 0;
}