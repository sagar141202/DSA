# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The input array will always have a peak element. If there are multiple peak elements, any of them can be returned as the result. For example, given the array [1, 2, 3, 1], the peak element is 3. Given the array [1, 2, 1, 3, 5, 6, 4], the peak elements are 2 and 6.

## Approach
The algorithm uses a binary search approach to find the peak element. It starts by checking the middle element of the array, and then decides which half to continue searching in. The decision is based on whether the middle element is smaller than its neighbor.

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
            // if middle element is smaller than the next one, 
            // then the peak must be on the right side
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
Input: [1, 2, 3, 1]
Output: 2
Input: [1, 2, 1, 3, 5, 6, 4]
Output: 5
```

## Key Takeaways
- The peak element is not necessarily the maximum element in the array.
- The binary search approach is used to reduce the time complexity to O(log n).
- The space complexity is O(1) because no extra space is used.