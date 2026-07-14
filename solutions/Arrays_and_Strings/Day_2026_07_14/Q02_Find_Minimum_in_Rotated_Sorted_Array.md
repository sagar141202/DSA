# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order but has been rotated an unknown number of times. For example, the array [4, 5, 6, 7, 0, 1, 2] is a rotated sorted array because it can be obtained by rotating the sorted array [0, 1, 2, 4, 5, 6, 7] three times to the right. The constraints are that the array contains distinct integers and the rotation is done in a circular manner. The goal is to find the index of the minimum element in the rotated sorted array.

## Approach
The approach is to use a modified binary search algorithm to find the minimum element in the rotated sorted array. The algorithm works by dividing the array into two halves and comparing the middle element with the rightmost element to determine which half contains the minimum element.

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
            // if the middle element is greater than the rightmost element, 
            // the minimum element must be in the right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // if the middle element is less than or equal to the rightmost element, 
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
- The problem can be solved using a modified binary search algorithm with a time complexity of O(log n).
- The key to the solution is to compare the middle element with the rightmost element to determine which half contains the minimum element.
- The solution assumes that the input array contains distinct integers and the rotation is done in a circular manner.