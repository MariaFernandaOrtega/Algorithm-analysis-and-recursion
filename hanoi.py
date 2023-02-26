# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:24:20 2023

@author: Maria Fernanda Ortega
"""

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    # Recursive Python function to solve tower of hanoi
    if n == 0:
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)

# Driver code
N = 3

# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')

