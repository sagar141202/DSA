# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order but has been rotated (shifted) by some number of positions. For example, the array [4, 5, 6, 7, 0, 1, 2] is a rotated version of the sorted array [0, 1, 2, 4, 5, 6, 7]. The constraint is that there are no duplicate elements in the array. The goal is to find the minimum element in the rotated array.

## Approach
We can use a modified binary search algorithm to solve this problem. The intuition is to compare the middle element of the array with the last element and decide which half of the array the minimum element is in.

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
            
            // if the middle element is greater than the right element, 
            // the minimum element must be in the right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // if the middle element is less than or equal to the right element, 
            // the minimum element must be in the left half
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
Input: [1, 2, 3, 4, 5]
Output: 1
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm.
- The time complexity of the solution is O(log n), where n is the number of elements in the array.
- The space complexity of the solution is O(1), as it only uses a constant amount of space.