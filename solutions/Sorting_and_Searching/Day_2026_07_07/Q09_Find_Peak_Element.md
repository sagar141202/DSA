# Find Peak Element

## Problem Statement
A peak element in an array is an element that is not smaller than its neighbors. Given an integer array `nums`, find a peak element and return its index. If the input array is empty, return -1. The array may contain multiple peak elements, and it is guaranteed that a peak element exists in the given array. For example, in the array `[1, 2, 3, 1]`, 3 is a peak element because it is not smaller than its neighbors. The function should find one peak element, not necessarily all of them.

## Approach
We can use a modified binary search algorithm to find the peak element. The idea is to compare the middle element with its neighbors and move towards the side that has a larger element. This approach works because the peak element must exist in the array.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            // If the middle element is smaller than the next one, 
            // the peak must be on the right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // Otherwise, the peak must be on the left side
            else {
                right = mid;
            }
        }
        return left;
    }
};
```

## Test Cases
```
Input: nums = [1, 2, 3, 1]
Output: 2
Input: nums = [1, 2, 1, 3, 5, 6, 4]
Output: 5
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm.
- The peak element must exist in the array, so we don't need to handle the case where no peak element is found.
- The time complexity is O(log n) because we divide the search space in half at each step.