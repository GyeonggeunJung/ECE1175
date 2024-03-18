#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define N 4

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
    printf("Matrix A : \n");
    for(int i = 0; i<N; i++){
        for(int j = 0; j<N; j++){
            printf("%f ", A[i][j]);
        }
        printf("\n");
    }
    printf("Matrix B : \n");
    for(int i = 0; i<N; i++){
        for(int j = 0; j<N; j++){
            printf("%f ", A[i][j]);
        }
        printf("\n");
    }

    // Code for Matrix Multiplication
    for(int i =0; i < N; i++){
        for(int j = 0; j<N; j++){
            C[i][j] = 0;
            for(int k = 0; k< N; k++){
                C[i][j] += A[i][k]*B[k][j];
            }
        }
    }

    printf("Matrix C : \n");
    for(int i = 0; i<N; i++){
        for(int j = 0; j<N; j++){
            printf("%f ", A[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}