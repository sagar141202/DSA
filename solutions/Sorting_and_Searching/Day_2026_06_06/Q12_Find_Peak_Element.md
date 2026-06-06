# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The array may contain multiple peak elements, and the solution should return the index of any one of them. The input array will always have at least one element, and the first and last elements are considered to have only one neighbor.

## Approach
The solution uses a modified binary search algorithm to find a peak element in the array. The algorithm starts by checking the middle element and comparing it with its neighbors. If the middle element is a peak, the algorithm returns its index; otherwise, it moves to the half of the array where a peak element is more likely to exist.

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
            // a peak must exist on the right side.
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                // Otherwise, a peak must exist on the left side.
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
Output: 1 or 5
```

## Key Takeaways
- The modified binary search algorithm reduces the time complexity to O(log n).
- The algorithm assumes that the input array is not empty and has at least one peak element.
- The solution returns the index of any peak element, not necessarily the first or last one.