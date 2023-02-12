#!/bin/bash
#SBATCH -J abinit
#SBATCH -p kshctest
#SBATCH --exclusive
#SBATCH -N 4
#SBATCH --ntasks-per-node=8
#SBATCH -o ../output/balanced=4_32_4.out


cd ../
source ./env.sh

matrix=(audikw_1 bone010 dielFilterV2real asia_osm ldoor nlpkkt80 rajat31 rgg_n_2_21_s0 road_central inline_1 hugebubbles-00000 germany_osm italy_osm adaptive ecology1 vas_stokes_1M AS365 M6 NLR cant)

export UCX_LOG_LEVEL=error

for((i=0;i<20;i++))
do
     #srun --mpi=pmix_v3  ./balanced ../matrix/${matrix[${i}]}.mtx 4
    mpirun -n 32 ./balanced ../matrix/${matrix[${i}]}.mtx 4
done 

