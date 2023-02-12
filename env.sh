module purge
module load compiler/devtoolset/7.3.1
module load compiler/rocm/2.9
module load mpi/mpich/3.2.1/intel
export PATH=/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/_install/lib:$PATH
export LIBRARY_PATH=/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/_install/lib:$LIBRARY_PATH
export LD_LIBRARY_PATH=/public/home/ghfund2_a17/DistSpMV_Balanced/metis-5.1.0/_install/lib:$LD_LIBRARY_PATH



