#include <stdlib.h>
int cont_op = 0;
// Algoritmo 2
int f(int n)
{
    int i, j, k, res = 0;
    for (i = n / 2; i <= n; i += i)
        for (j = n + 1; j <= 2 * i; j += 2)
            for (k = j / 2; k <= n * i; k += k / 2 + 1)
            {
                res = res + 2 * n;
                cont_op++;
            }
    return res;
}

int main(){
    printf("Hello World");
}