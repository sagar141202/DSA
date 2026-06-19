# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The input array will always have a peak element. If there are multiple peak elements, any of them can be returned as the result. For example, given the array [1, 2, 3, 1], the output should be 3, as 3 is a peak element. The array can be unsorted and can contain duplicate elements. The constraints are 1 <= nums.length <= 1000, and -2^31 <= nums[i] <= 2^31 - 1.

## Approach
The algorithm uses a modified binary search to find the peak element. It starts by considering the middle element of the array and compares it with its neighbors. If the middle element is greater than its neighbors, it is a peak element. Otherwise, the algorithm moves to the half of the array where the peak element is more likely to be.

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
- The algorithm uses a modified binary search to find the peak element in O(log n) time complexity.
- The space complexity is O(1) as it only uses a constant amount of space.
- The algorithm works by comparing the middle element with its neighbors and moving to the half of the array where the peak element is more likely to be.