# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order but has been rotated an unknown number of times. For example, the array [4, 5, 6, 7, 0, 1, 2] is a rotated version of the sorted array [0, 1, 2, 4, 5, 6, 7]. The goal is to write an efficient algorithm to find the minimum element in such an array. The input array will contain at least one element and will not be empty.

## Approach
The approach involves using a modified binary search algorithm to find the minimum element in the rotated sorted array. The algorithm checks the middle element of the array and compares it with the last element to determine which half of the array the minimum element is in.

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
            if (nums[mid] > nums[right]) {
                // minimum element is in the right half
                left = mid + 1;
            } else {
                // minimum element is in the left half
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
Input: [1]
Output: 1
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm with a time complexity of O(log n).
- The algorithm takes advantage of the fact that the array is initially sorted and then rotated.
- The solution does not use any extra space, resulting in a space complexity of O(1).