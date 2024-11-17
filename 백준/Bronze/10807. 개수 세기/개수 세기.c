#include <stdio.h>
#include <stdlib.h>

int main() {
    int N, v;
    scanf("%d", &N);
    int arr[101];
    int count = 0;

    for (int i = 0; i < N; i++) {
        scanf("%d ", &arr[i]);
    }

    scanf("%d", &v);

    for (int j = 0; j < N; j++) {
        if (v == arr[j]) {
            count++;
        }
    }

    printf("%d", count);
    return 0;
}