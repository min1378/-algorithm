#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = [0] * max(ar)
    result = 0
    for j in ar:
        count[j-1] += 1
    for i in count :
        while i > 1 :
            result += i // 2
    return result

n = int(input())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)