# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The input array will always have a peak element. If there are multiple peak elements, any of them can be returned as the result. For example, given the array [1, 2, 3, 1], the peak element is 3. The array can be unsorted.

## Approach
The algorithm uses a modified binary search approach to find the peak element in the array. It starts by checking the middle element and comparing it with its neighbors. If the middle element is greater than its neighbors, it is a peak element. Otherwise, the algorithm continues to search in the half of the array where the peak element is likely to be.

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
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
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
- The algorithm has a time complexity of O(log n) making it efficient for large inputs.
- The algorithm only uses a constant amount of space, making it space-efficient.
- The algorithm can be applied to any array with distinct elements, not just integers.