# -*- coding: utf-8 -*-

int1 = int(input())
int2 = int(input())
int3 = int(input())

nums = []

if (int1%2)==0:
    nums.append(int1)
    
if (int2%2)==0:
    nums.append(int2)
    
if (int3%2)==0:
    nums.append(int3)
    
nums.sort()
    
for e in nums:
    print(e)