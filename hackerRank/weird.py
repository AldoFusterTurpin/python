#!/bin/python3

# ALDO FUSTER TURPIN

import math
import os
import random
import re
import sys

def isWeird(n: int):
    if n % 2 != 0:
        return True
    if n >= 2 and n <= 5:
        return False
    if n >= 6 and n <= 20:
        return True
    if n > 20:
        return False
    
    
    
if __name__ == '__main__':
    n = int(input().strip())
    if isWeird(n):
        print ("Weird")
    else:
        print("Not Weird")
