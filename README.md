# DistSpMV_Balanced

## check-list 
- __Algorithm:__ Distributed Sparse Matrix-Vector Multiplication (DistSpMV_Balanced)
- __Program:__ C OpenMP and MPI code
- __Compilation:__ mpicc (3.2.1)
- __Running:__ mpirun (3.2.1)
- __Dataset__ 20 sparse square matrices in the SuiteSparse Matrix Collection.
- __Hardware:__ AMD 32-core EPYC 7551 CPU
- __Output:__ 20 Matrix related information, traffic, computation time, communication time, etc.
## Introduction
1. The __csv__ folder is used to store (.csv) files that need to be written to run code, which is convenient for us to carry out visualization through python code later.
2. The __draw__ folder stores some python code that visualizes the running results.
3. The __figure__ folder is used to store the visual image of the running result.
4. __metis-5.1.0__ is the package we need to run the code.
5.The __output__ folder is used to store the output (.out) file of our running code, which records in detail the calculation time, communication time, rate and other information of each matrix under various processes.
6. The __run__ folder is used to store the scripts where we run the code.
7. The __script__ folder contains all of our scripts.
8. The rest is for our code and environment and compile scripts. __env.sh__ is the environment setting, __compile.sh__ is the compile script.

## Experimental workflow.
1. The required software package were downloaded from GitHub platform to the experimental platform, and then  download the 20 matrices required in the paper from the website https://sparse.tamu.edu into a folder named __"matrix"__ and put it in the upper directory of the software package for our subsequent operations. 
2. Check the __"compile.sh"__ file in the software package. If there is no related module in the file, it is better to load the module according to the same version and change the path of the file to the current experimental path.
3. Go to the location of the current software package and compile the program.
```
cd  /path/to/DistSpMV\_Balanced
source compile.sh
```
4. Initialization of the csv file.
```
./init_csv
```
Each time we submit a running task for related evaluation, we need to initialize the csv file, which is convenient for us to use python files to read the file for graph display.
5. Go to the __run__ directory and submit tasks for performance check.
```
cd run
source runspmv.sh
cd ../run
source runreorder.sh
cd ../run
source runbalanced.sh
```
6. Wait for the program to finish running, enter the __draw__ directory to run python code for drawing.
```
cd ../draw
python draw.py
```
At this time, __"fig4\_performance.png"__ will be generated in the __figure__ directory. This figure corresponds to the performance comparison of 20 matrices in the three versions of __Figure 4__ in the paper.If some running rates are displayed as 0, it indicates that the matrix may not be successfully calculated in this case due to changes in the environment. It is recommended to use the same version of the environment and run the csv file several times after initializing it.
7. Go to the __run__ directory to submit the task and run the code that logs traffic and computation.
```
cd ../run
sbatch runcom.sh
```
8. After the program is finished, enter the draw directory and submit python code for drawing.
```
cd ../draw
sbatch draw_thermal.sh
```
After running correctly, we can see that some new images are generated in __figure__ directory, including heat maps and a comparison of computation and traffic, corresponding to __Figure 5__ in the paper.
9. Submit the task in the __run__ directory to run the code about the record preprocessing time.
```
cd ../run
sbatch runpreprocess.sh
```
10. After the program is finished, enter the __draw__ directory and submit python code for drawing.
```
cd ../draw
python preprocess.py
```
Once running correctly, you can see that a picture called __"fig7_preprocess_time.png"__ is generated in __figure__ directory, showing __DistSpMV_Balanced__ and __DistSpMV_Reordered__ preprocessing times, as shown in __Figure 7__ of the paper.
## Output information
According to the above steps, we get the (.out) file of the processing information of the matrix under each process in the output folder. Relevant examples will be shown in the next part. Now the meanings of each part are roughly explained as follows: <br>
__Line 1__ outputs the number of processes and threads.<br>
__Line 2-3__ output the input matrix’s information including the path of matrix file, The number of rows, columns and nonzeros.<br>
__Line 4__ prints the number of total communication. <br>
__Line 5__ prints the prepocess time.(in milliseconds) <br>
__Line 6__ prints the communication time time.(in milliseconds) <br> 
__Line 7__ prints the total calculation time.(in milliseconds)  <br>
__Line 8__ prints the total time and the calculated rate. <br>
__Line 9__ prints the number of calculated errors to check for correctness. <br>
Meanwhile, in order to present our results more clearly, we recorded the output information in a (.csv) file, and stored the picture in figure through python drawing, which can be directly compared with the picture in the paper.
