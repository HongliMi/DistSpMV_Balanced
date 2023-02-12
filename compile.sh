module purge
module load compiler/devtoolset/7.3.1
module load compiler/rocm/2.9
module load mpi/mpich/3.2.1/intel


mpicc DistSpMV_Reordered.c -fopenmp -L/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/_install/lib  -lmetis -I/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/include -lm -O3 -o reorder
mpicc DistSpMV_Balanced.c -fopenmp -L/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/_install/lib  -lmetis -I/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/include -lm -O3 -o balanced
mpicc DistSpMV.c -fopenmp -L/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/_install/lib  -lmetis -I/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/include -lm -O3 -o  spmv

mpicc Balanced_com.c -fopenmp -L/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/_install/lib  -lmetis -I/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/include -lm -O3 -o balanced_com
mpicc Reordered_com.c -fopenmp -L/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/_install/lib  -lmetis -I/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/include -lm -O3 -o reordered_com
mpicc SpMV_com.c -fopenmp -L/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/_install/lib  -lmetis -I/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/include -lm -O3 -o  spmv_com


mpicc DistSpMV_Balanced_preprocess.c -fopenmp -L/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/_install/lib  -lmetis -I/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/include -lm -O3 -o balanced_preprocess
mpicc DistSpMV_Reordered_preprocess.c  -fopenmp -L/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/_install/lib  -lmetis -I/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/include -lm -O3 -o reordered_preprocess


gcc init_csv.c -o init_csv

