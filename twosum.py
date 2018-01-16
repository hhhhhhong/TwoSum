#!/usr/bin/python
import sys
import math

def two_sum(nums, target):
   for x in range(0, 5):
      for y in range(0, 5):
	 if nums[x] + nums[y] == target:
	    print('Answer: %d, %d' %(x, y)) 


def main():
   num_list = [1,2,3,4,5]
   target = 9
   two_sum(num_list, target)

if __name__=='__main__':
    main()
