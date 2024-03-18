#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define N 1024
#define BLOCK_SIZE 16

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
    for (int i = 0; i < N; i += BLOCK_SIZE) {
        for (int j = 0; j < N; j += BLOCK_SIZE) {
            for (int k = 0; k < N; k += BLOCK_SIZE) {
                for (int ii = i; ii < i + BLOCK_SIZE && ii < N; ++ii) {
                    for (int jj = j; jj < j + BLOCK_SIZE && jj < N; ++jj) {
                        for (int kk = k; kk < k + BLOCK_SIZE && kk < N; ++kk) {
                            C[ii][jj] += A[ii][kk] * B[kk][jj];
                        }
                    }
                }
            }
        }
    }
    // Measure the clock time
    clock_t end_time = clock();
    float elapse = (float)(end_time - start_time) / CLOCKS_PER_SEC;
    printf("Elapse : %.4f seconds\n", elapse);
    
    return 0;
}
