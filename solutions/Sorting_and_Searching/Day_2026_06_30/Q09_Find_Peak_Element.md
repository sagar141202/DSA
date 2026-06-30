# Find Peak Element

## Problem Statement
The problem requires finding a peak element in an array, which is an element that is not smaller than its neighbors. The input array will have at least one element and may have multiple peak elements. The goal is to find any one of the peak elements. For example, given the array `[1, 2, 3, 1]`, the peak element is `3`. The array can be unsorted, and the peak element can be anywhere in the array.

## Approach
The approach involves using a modified binary search algorithm to find the peak element. The algorithm works by comparing the middle element with its neighbors and moving the search space accordingly. If the middle element is greater than its neighbors, it is a peak element. Otherwise, the algorithm moves to the side where the neighbor is greater.

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
            // if mid element is smaller than next, peak must be on right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                // if mid element is greater than or equal to next, peak must be on left side
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
- The problem can be solved using a modified binary search algorithm.
- The algorithm works by comparing the middle element with its neighbors and moving the search space accordingly.
- The time complexity of the algorithm is O(log n), making it efficient for large inputs.