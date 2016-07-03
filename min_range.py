# -*- coding: utf-8 -*-
"""
You have k lists of sorted integers.
Find the smallest range that includes at least
one number from each of the k lists. 

For example, 
List 1: [4, 10, 15, 24, 26] 
List 2: [0, 9, 12, 20] 
List 3: [5, 18, 22, 30] 

The smallest range here would be [20, 24] as it contains 24 from list 1,
20 from list 2, and 22 from list 3.
"""

def min_range(lists):
    
    min_range = MinRange(lists)
    return min_range.min_range

class MinRange(object):
    
    def __init__(self,lists):
        lists = sorted(lists, key = lambda x: len(x), reverse = True)
        self.origin_list = sorted(lists.pop())
        self.lists = [sorted(n_list, reverse = True) for n_list in lists]
        self.ranges = tuple((n,n) for n in self.origin_list)
        self.len_ranges = len(self.ranges)
        self.find_min_range()
        
    def find_min_range(self):
        
        for n_list in self.lists:            
            self.ranges_temp = []
            self.n_list = n_list
            
            self.remove_unnecessary_small()
            self.n_list.sort()
            self.remove_unnecessary_large()   
            
            for i in self.n_list:
                self.new_range_cap(i)
                self.new_range_mid(i)
                self.new_range_base(i)
            
            self.ranges = self.ranges_temp
            self.len_ranges = len(self.ranges)
        
        self.min_range = min(self.ranges, key = lambda x: x[1] - x[0])
        
    def new_range_cap(self,i):
        for j in range(0,self.len_ranges):
            if j < self.len_ranges - 1:
                if i > self.ranges[j][1] and i < self.ranges[j+1][1]:
                    self.ranges_temp.append((self.ranges[j][0],i))
                    break
            else:
                if i > self.ranges[j][1]:
                    self.ranges_temp.append((self.ranges[j][0],i))
                    break
    
    def new_range_mid(self,i):
        for j in range(0,self.len_ranges):
            if self.ranges[j][0] < i < self.ranges[j][1]:
                self.ranges_temp.append(self.ranges[j])
    
    def new_range_base(self,i):
        for j in range(0,self.len_ranges):
            if j > 0:
                if i < self.ranges[j][0] and i > self.ranges[j-1][0]:
                    self.ranges_temp.append((i,self.ranges[j][1]))
                    break
            else:
                if i < self.ranges[j][0]:
                    self.ranges_temp.append((i,self.ranges[j][1]))
                    break

    def remove_unnecessary_large(self):
        
        if self.n_list[-1] < self.ranges[0][0]:
            while len(self.n_list) > 1 and self.n_list[-2] < self.ranges[0][0]:
                self.n_list.pop()
    
    def remove_unnecessary_small(self):
        
        if self.n_list[-1] < self.ranges[0][0]:
            while len(self.n_list) > 1 and self.n_list[-2] < self.ranges[0][0]:
                self.n_list.pop()