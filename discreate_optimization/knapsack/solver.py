#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def Optimize_1(items, k, j):
    # based on recursion
    if j == -1:
        return (0, [])
    elif k < items[j][2]:
        return Optimize_1(items, k, j-1)
    else:
        res_1, selected_index_1 = Optimize_1(items, k-items[j][2], j-1)
        res_1 += items[j][1]

        res_2, selected_index_2 = Optimize_1(items, k, j-1)
        if res_1 > res_2:
            return res_1, selected_index_1 + [j]
        else:
            return res_2, selected_index_2

def Optimize_2(items, k):
    # based on dynamic programming
    dp_matrix = [[0]*(len(items)+1) for _ in xrange(k+1)]
    for i in xrange(1, k+1):
        for j in  xrange(1, len(items)+1):
            # test if weight is less than equal to capacity
            if items[j-1][2] <= i:
                dp_matrix[i][j] = max(dp_matrix[i][j-1], items[j-1][1]+dp_matrix[i-items[j-1][2]][j-1])
            else:
                dp_matrix[i][j] = dp_matrix[i][j-1]

    taken_index = []
    i, j = k, len(items)
    while(True):
        if dp_matrix[i][j] != dp_matrix[i][j-1]:
            taken_index.append(j-1)
            i -= items[j-1][2]
        j = j-1
        if i <= 0 or j <= 0:
            break

    return dp_matrix[k][len(items)], taken_index[::-1]

class Node():

    def __init__(self):
        self.value = None
        self.capacity = None
        self.eastimate = None
        self.left = None
        self.right = None 


# class BranchBound:
#     def  __init__(self):
#         self.Tree = None

#     def Optimize_3(self, items, k):
#         # based on branch and bound
#         dp_matrix = [[0]*(len(items)+1) for _ in xrange(k+1)]
#         for i in xrange(1, k+1):
#             for j in  xrange(1, len(items)+1):
#                 # test if weight is less than equal to capacity
#                 if items[j-1][2] <= i:
#                     dp_matrix[i][j] = max(dp_matrix[i][j-1], items[j-1][1]+dp_matrix[i-items[j-1][2]][j-1])
#                 else:
#                     dp_matrix[i][j] = dp_matrix[i][j-1]

#         taken_index = []
#         i, j = k, len(items)
#         while(True):
#             if dp_matrix[i][j] != dp_matrix[i][j-1]:
#                 taken_index.append(j-1)
#                 i -= items[j-1][2]
#             j = j-1
#             if i <= 0 or j <= 0:
#                 break

#         return dp_matrix[k][len(items)], taken_index[::-1]


def Optimize_3(items, k):
    # based on branch and bound
    dp_matrix = [[0]*(len(items)+1) for _ in xrange(k+1)]
    for i in xrange(1, k+1):
        for j in  xrange(1, len(items)+1):
            # test if weight is less than equal to capacity
            if items[j-1][2] <= i:
                dp_matrix[i][j] = max(dp_matrix[i][j-1], items[j-1][1]+dp_matrix[i-items[j-1][2]][j-1])
            else:
                dp_matrix[i][j] = dp_matrix[i][j-1]

    taken_index = []
    i, j = k, len(items)
    while(True):
        if dp_matrix[i][j] != dp_matrix[i][j-1]:
            taken_index.append(j-1)
            i -= items[j-1][2]
        j = j-1
        if i <= 0 or j <= 0:
            break

    return dp_matrix[k][len(items)], taken_index[::-1]



def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    # #method 1a:- select iteam greedily, sort the item from larger to lower value.
    # items = sorted(items, key=lambda x: x[1])[::-1]
    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight

    # #method 1b:- select iteam greedily, sort the item from lower to larger weight. That is trying to fit more items.
    # items = sorted(items, key=lambda x: x[2])
    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight

    # # method 2:- select iteam greedily, sort the item from larger to lower using value/weight ratio (density).
    # items = sorted(items, key=lambda x: x[1]/float(x[2]))[::-1]
    # # print [x/float(y) for _, x, y in items]
    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight

    # taken = [0]*len(items)
    # # method 3:- select iteam dynamic programming using recursion.
    # value, taken_index = Optimize_1(items, capacity, item_count-1)
    # test_val = 0
    # for index in taken_index:
    #     taken[index] = 1
    #     test_val += items[index][1]

    # print taken_index, value, test_val

    test_val = 0
    taken = [0]*len(items)
    # method 4:- select iteam dynamic programming.
    value, taken_index = Optimize_2(items, capacity)
    for index in taken_index:
        taken[index] = 1
        test_val += items[index][1]

    # print taken_index, value, test_val
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

