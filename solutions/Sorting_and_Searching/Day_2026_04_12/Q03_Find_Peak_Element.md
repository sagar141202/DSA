# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The input array will always have a peak element. If there are multiple peak elements, any of them can be returned as the result. The array can be unsorted and may contain duplicate elements.

## Approach
The algorithm uses a binary search approach to find the peak element. It works by repeatedly dividing the search interval in half and searching for the peak element in one of the two halves. The key intuition is that if the middle element is smaller than its neighbor, the peak element must be in the other half.

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
            // if mid element is smaller than next element, peak must be on right side
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
- The binary search approach is efficient for finding peak elements in unsorted arrays.
- The key to this problem is to understand that if the middle element is smaller than its neighbor, the peak element must be in the other half.
- This solution has a time complexity of O(log n) and a space complexity of O(1), making it efficient for large inputs.