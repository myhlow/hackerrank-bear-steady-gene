#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

counter = {'A':0,'C':0,'G':0,'T':0}
def isSteady(l):
    if counter['A']<=l and counter['C']<=l and counter['G']<=l and counter['T']<=l:
        return True
    else:
        return False
        
def steadyGene(gene):
    # Write your code here
    l = len(gene)
    steady = l//4
    for g in gene:
        counter[g]=counter[g]+1
    low = high = 0
    minLen=l
    while low<l and high<l:
        if not isSteady(steady):
            m = gene[high]
            counter[m]=counter[m]-1
            high=high+1
        else:
            minLen = min(minLen,high-low)
            m = gene[low]
            counter[m]=counter[m]+1
            low=low+1
        #print(counter,high,low)
    return minLen
                
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
