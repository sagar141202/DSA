# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The array may contain multiple peak elements, in that case, return the index of any one of the peak elements. The input array will always have at least one element and may contain duplicate elements. For example, given the array `[1, 2, 3, 1]`, the output should be `2` because `3` is a peak element.

## Approach
The algorithm uses a modified binary search approach to find the peak element in the array. It starts by checking the middle element and comparing it with its neighbors. If the middle element is greater than its neighbors, it is a peak element. If not, the algorithm moves to the left or right half of the array based on which neighbor is greater.

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
            // if mid element is smaller than next element, peak must be in right half
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // if mid element is greater than next element, peak must be in left half
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
- The algorithm uses a modified binary search approach to find the peak element in O(log n) time complexity.
- The space complexity is O(1) as no extra space is used.
- The algorithm works by comparing the middle element with its neighbors and moving to the left or right half of the array based on which neighbor is greater.