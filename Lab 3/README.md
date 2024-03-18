# Cache & I/O Programming

## Task 1 : Monitor Cache Misses
- Cache is fast but small memory close to the processor.
<p align="center">
<img width="500" alt="image" src="https://github.com/GyeonggeunJung/ECE1175/assets/113646015/d48ecadf-b13e-4e0c-91c6-015621970f8b">
</p>

- How cache work?
<p align="center"> 
<img width="500" alt="image" src="https://github.com/GyeonggeunJung/ECE1175/assets/113646015/e3a5556c-4017-412a-a54f-575802fdddef">
</p>

- In C, multidimensional arrays are stored in row-major order in the memory. The way you access entries affects cache misses.
<p align="center"> 
<img width="500" alt="image" src="https://github.com/GyeonggeunJung/ECE1175/assets/113646015/99f9eeec-518e-4f48-a874-235044556d64">
</p>

- Analyze Matrix Multiplication Program Using Perf
<p align="center"> 
<img width="377" alt="image" src="https://github.com/GyeonggeunJung/ECE1175/assets/113646015/259c2c99-131c-44ba-bd1a-4813830de998">
</p>

- Write C/C++ code to implement NxNmatrix multiplication based on the provided code template and test it on N=256,512,1024.
- Use perf to analyze your code, and optimize it accordingly.
  - Produce correct results of matrix multiplication (you may want to verify it using a smaller N, e.g., 3x3).
  - Have minimal cache-miss-rate and runtime

## Task 2 : Direct GPIO Access

- Use GPIO 42 (internally connected to the onboard green LED) to generate a blinking pattern
<p align="center"> 
<img width="209" alt="image" src="https://github.com/GyeonggeunJung/ECE1175/assets/113646015/36d6cedf-e922-4724-863d-efb9053b65ce">
</p>



