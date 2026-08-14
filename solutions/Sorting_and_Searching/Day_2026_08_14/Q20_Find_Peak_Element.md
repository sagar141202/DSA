# Find Peak Element

## Problem Statement
A peak element in an array is an element that is not smaller than its neighbors. Given an integer array `nums`, find a peak element and return its index. If the input array is guaranteed to have a peak element, then any peak element can be returned. The array can have multiple peak elements, in which case any of the indices of these elements can be returned. The input array will have at least one element and may contain duplicates. For example, given `nums = [1,2,3,1]`, the output could be `2` because `3` is a peak element.

## Approach
The algorithm uses a binary search approach to find the peak element. It starts by finding the middle element of the array and comparing it with its neighbors. If the middle element is greater than its neighbors, it is a peak element. Otherwise, the algorithm moves to the left or right half of the array based on the comparison.

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
            // if mid element is smaller than the next one, then the peak must be on the right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                // if mid element is greater than or equal to the next one, then the peak must be on the left side
                right = mid;
            }
        }
        return left;
    }
};
```

## Test Cases
```
Input: nums = [1,2,3,1]
Output: 2
Input: nums = [1,2,1,3,5,6,4]
Output: 5
```

## Key Takeaways
- The binary search approach is used to find the peak element in O(log n) time complexity.
- The algorithm moves to the left or right half of the array based on the comparison of the middle element with its neighbors.
- The peak element can be any element that is not smaller than its neighbors.