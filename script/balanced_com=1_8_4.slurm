#!/bin/bash
#SBATCH -J abinit
#SBATCH -p kshctest
#SBATCH --exclusive
#SBATCH -N 1
#SBATCH --ntasks-per-node=8
#SBATCH -o ../output/balanced_com=1_8_4.out

cd ../
source ./env.sh


#matrix=(audikw_1 bone010 dielFilterV2real asia_osm ldoor nlpkkt80 rajat31 rgg_n_2_21_s0 road_central inline_1 hugebubbles-00000 germany_osm italy_osm adaptive ecology1 vas_stokes_1M AS365 M6 NLR cant)

export UCX_LOG_LEVEL=error

mpirun -np 8 ./balanced_com ../matrix/road_central.mtx 4
mpirun -np 8 ./balanced_com ../matrix/inline_1.mtx 4





