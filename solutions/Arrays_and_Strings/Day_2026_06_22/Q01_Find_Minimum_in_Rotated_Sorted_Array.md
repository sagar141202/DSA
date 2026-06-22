# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order but has been rotated (shifted) by some number of positions. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotated sorted array. The constraints are that the array is non-empty and contains distinct elements. The goal is to find the minimum element in the array.

## Approach
The approach to solve this problem is to use a modified binary search algorithm. The idea is to divide the array into two halves and determine which half contains the minimum element. This is done by comparing the middle element with the rightmost element. If the middle element is greater than the rightmost element, the minimum element must be in the right half. Otherwise, it must be in the left half.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        
        // if the array is not rotated, return the first element
        if (nums[left] < nums[right]) {
            return nums[left];
        }
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            // if the middle element is greater than the rightmost element, 
            // the minimum element must be in the right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // otherwise, the minimum element must be in the left half
            else {
                right = mid;
            }
        }
        
        return nums[left];
    }
};
```

## Test Cases
```
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
Input: [3, 4, 5, 1, 2]
Output: 1
Input: [11, 13, 15, 17]
Output: 11
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm.
- The time complexity of the solution is O(log n), which makes it efficient for large inputs.
- The space complexity is O(1), which means the solution uses constant space and does not depend on the size of the input array.