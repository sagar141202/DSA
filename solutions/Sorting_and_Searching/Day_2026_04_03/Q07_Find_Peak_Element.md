# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The input array will always have a peak element. If there are multiple peak elements, any of them can be returned as the result. The array can be unsorted and may contain duplicate elements. For example, in the array [1, 2, 3, 1], 3 is a peak element because it is not smaller than its neighbors. In the array [1, 2, 1, 3, 5, 6, 4], both 2 and 5 are peak elements.

## Approach
The algorithm uses a modified binary search to find the peak element. It starts by checking the middle element and comparing it with its neighbors. If the middle element is greater than its neighbors, it is a peak element. If the middle element is smaller than the left neighbor, the peak element must be in the left half. If the middle element is smaller than the right neighbor, the peak element must be in the right half.

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
            // if mid element is smaller than the next one, the peak must be on the right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                // otherwise, the peak must be on the left side
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
- The problem can be solved using a modified binary search algorithm.
- The time complexity is O(log n) due to the binary search.
- The space complexity is O(1) as it only uses a constant amount of space.