import sys, os
sys.stdin = open('square.in', 'r')
sys.stdout = open('square.out', 'w')
r1 = map(int, raw_input().split(' '))
r2 = map(int, raw_input().split(' '))
dist = max(max(r1[0], r1[2], r2[0], r2[2]) - min(r1[0], r1[2], r2[0], r2[2]), max(r1[1], r1[3], r2[1], r2[3]) - min(r1[1], r1[3], r2[1], r2[3]))
print dist*dist