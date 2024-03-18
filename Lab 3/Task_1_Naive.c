#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define N 1024

float A[N][N];
float B[N][N];
float C[N][N];

int main(){
    // Randomly Init A and B
    srand((unsigned)time(NULL));
    for(int i = 0; i<N; i++){
        for(int j = 0; j<N; j++){
            A[i][j] = rand()/(float)RAND_MAX;
            B[i][j] = rand()/(float)RAND_MAX;
        }
    }
    //Set up clcok
    clock_t start_time = clock();

    // Code for Matrix Multiplication
    for(int i =0; i < N; i++){
        for(int j = 0; j<N; j++){
            C[i][j] = 0;
            for(int k = 0; k< N; k++){
                C[i][j] += A[i][k]*B[k][j];
            }
        }
    }
    // Measure the clock time
    clock_t end_time = clock();
    float elapse = (float)(end_time - start_time) / CLOCKS_PER_SEC;
    printf("Elapse : %.4f seconds\n", elapse);
    
    return 0;
}
