# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order, but then its elements were rotated some number of positions. For example, the array [4, 5, 6, 7, 0, 1, 2] is a rotated sorted array because it can be obtained by rotating the sorted array [0, 1, 2, 4, 5, 6, 7] 3 positions to the right. The constraints are that the array will not be empty and there will be no duplicates in the array. The goal is to write a function that can find the minimum element in such an array.

## Approach
The algorithm used here is a modified binary search algorithm. The intuition is to find the pivot element where the rotation occurs, and then the minimum element will be the next element after the pivot. We can find the pivot by comparing the middle element with the rightmost element.

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
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            // if mid element is greater than rightmost element, 
            // then the pivot must be in the right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // if mid element is less than or equal to rightmost element, 
            // then the pivot must be in the left half
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
```

## Key Takeaways
- We can use a modified binary search algorithm to find the minimum element in a rotated sorted array.
- The key is to find the pivot element where the rotation occurs.
- The time complexity of this solution is O(log n), which is more efficient than a linear search.