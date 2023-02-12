#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <sys/time.h>
#include <omp.h>
#include "mmio_highlevel.h"

int main()
{
    //GFlops csv init
    FILE *fres1 = fopen("./csv/DistSpMV_Balanced.csv", "w");
    if (fres1 == NULL) printf("Writing results fails1.\n");
    fprintf(fres1, "matrix, rownum, colnum, nnzR, rec_time, spmv_time, time, GFlops, process, thread\n");
    fclose(fres1);

    FILE *fres2 = fopen("./csv/DistSpMV_Reordered.csv", "w");
    if (fres2 == NULL) printf("Writing results fails2.\n");
    fprintf(fres2, "matrix, rownum, colnum, nnzR, rec_time, spmv_time, time, GFlops, process, thread\n");
    fclose(fres2);

    FILE *fres3 = fopen("./csv/DistSpMV.csv", "w");
    if (fres3 == NULL) printf("Writing results fails3.\n");
    fprintf(fres3, "matrix, rownum, colnum, nnzR, rec_time, spmv_time, time, GFlops, process, thread\n");
    fclose(fres3);

    //themral csv init
    FILE *fres4 = fopen("./csv/DistSpMV_com.csv", "w");
    if (fres4 == NULL) printf("Writing results fails.\n");
    fprintf(fres4, " matrix, receiver, sender, num\n");

    FILE *fres5 = fopen("./csv/DistSpMV_Reordered_com.csv", "w");
    if (fres5 == NULL) printf("Writing results fails.\n");
    fprintf(fres5, " matrix, receiver, sender, num\n");

    FILE *fres6 = fopen("./csv/DistSpMV_Balanced_com.csv", "w");
    if (fres6 == NULL) printf("Writing results fails.\n");
    fprintf(fres6, " matrix, receiver, sender, num\n");


    //compulation csv init 
    FILE *fres7 = fopen("./csv/DistSpMV_calculation.csv", "w");
    if (fres7 == NULL) printf("Writing results fails.\n");
    fprintf(fres7, " matrix, process, sum_mesg, sum_local, sum_remote\n");

    FILE *fres8 = fopen("./csv/DistSpMV_Reordered_calculation.csv", "w");
    if (fres8 == NULL) printf("Writing results fails.\n");
    fprintf(fres8, " matrix, process, sum_mesg, sum_local, sum_remote\n");

    FILE *fres9 = fopen("./csv/DistSpMV_Balanced_calculation.csv", "w");
    if (fres9 == NULL) printf("Writing results fails.\n");
    fprintf(fres9, " matrix, process, sum_mesg, sum_local, sum_remote\n");

    //prepocess time init
    FILE *fres10 = fopen("./csv/DistSpMV_Reordered_preprocess.csv", "w");
    if (fres10 == NULL) printf("Writing results fails.\n");
    fprintf(fres10, "filename, m, n, nnzR, pre_time\n");
    fclose(fres10);

    FILE *fres11 = fopen("./csv/DistSpMV_Balanced_preprocess.csv", "w");
    if (fres11 == NULL) printf("Writing results fails.\n");
    fprintf(fres11, "filename, m, n, nnzR, pre_time\n");
    fclose(fres11);
/*
    FILE *fres12 = fopen("18_compare.csv", "w");
    if (fres12 == NULL) printf("Writing results fails.\n");
    fprintf(fres12, "filename, m, n, nnzR, GFlops");
    fclose(fres12);

    FILE *fres13 = fopen("balanced_compare.csv", "w");
    if (fres13 == NULL) printf("Writing results fails.\n");
    fprintf(fres13, "filename, m, n, nnzR, GFlops");
    fclose(fres13);
*/
    return 0;
}
