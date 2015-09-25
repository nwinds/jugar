""" creating an estimator for running time T(N) ~ aN^b
Suppose that you time a program as a function of N and produce
the following table.

        N   seconds
-------------------
     1024     0.000
     2048     0.001
     4096     0.002
     8192     0.005
    16384     0.016
    32768     0.049
    65536     0.155
   131072     0.482
   262144     1.515
   524288     4.731
  1048576    14.761
  2097152    46.186
  4194304   144.191
  8388608   450.223
 16777216  1406.071


Estimate the order of growth of the running time as a function of N.
Assume that the running time obeys a power law T(N) ~ a N^b. For your
answer, enter the constant b. Your answer will be marked as correct
if it is within 1% of the target answer - we recommend using
two digits after the decimal separator, e.g., 2.34.
"""
import math
dataList = [1024, 0.000, 2048, 0.001, 4096, 0.002, 8192,0.005,
16384,0.016, 32768,0.049, 65536,0.155, 131072,0.482, 262144,1.515,
524288,4.731, 1048576,14.761, 2097152,46.186, 4194304,144.191,
8388608,450.223, 16777216,1406.071]

def calculateT(li):
    sample = []
    for i in range(0, len(li)-1, 2):
        #ele1 = li[i+1][1]
        #ele0 = li[i][1]
        #type(ele1)
        n1 = math.log(li[i+1], 2)
        n0 = math.log(li[i], 2)
        sample.append(n1-n0)
    print(sample)
    return
calculateT(dataList)