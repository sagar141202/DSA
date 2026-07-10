# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The array may contain multiple peak elements, and the task is to find at least one of them. The input array will always contain at least one element and may contain duplicates. For example, given the array [1, 2, 3, 1], the peak elements are 3.

## Approach
The algorithm uses a modified binary search approach to find the peak element in the array. It compares the middle element with its neighbors and moves the search space accordingly. If the middle element is greater than its neighbors, it is a peak element. Otherwise, the search space is reduced to the half where the peak element is more likely to exist.

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
            // if mid element is smaller than the next one, 
            // the peak must be on the right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // otherwise, the peak must be on the left side
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
Input: [1, 2, 3, 1]
Output: 2
Input: [1, 2, 1, 3, 5, 6, 4]
Output: 5
```

## Key Takeaways
- The problem can be solved using a modified binary search approach with a time complexity of O(log n).
- The space complexity is O(1) as no extra space is used.
- The solution works by comparing the middle element with its neighbors and reducing the search space accordingly.