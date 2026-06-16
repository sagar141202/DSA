# Find Peak Element

## Problem Statement
The problem requires finding a peak element in an array, where a peak element is an element that is not smaller than its neighbors. Given an array of integers `nums`, find a peak element and return its index. The input array will always have at least one element and may contain multiple peak elements, but it is only necessary to return the index of one of them. For example, given the array `[1, 2, 3, 1]`, the peak element is `3` and its index is `2`. The array may also be rotated or unsorted.

## Approach
The algorithm uses a binary search approach to find the peak element. It starts by checking the middle element of the array and comparing it with its neighbors. If the middle element is greater than its neighbors, it is a peak element. If the middle element is smaller than its left neighbor, the peak element must be in the left half of the array. If the middle element is smaller than its right neighbor, the peak element must be in the right half of the array.

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
        int left = 0;
        int right = nums.size() - 1;
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
Input: nums = [1, 2, 3, 1]
Output: 2
Input: nums = [1, 2, 1, 3, 5, 6, 4]
Output: 5
```

## Key Takeaways
- The binary search approach is used to find the peak element in the array.
- The time complexity of the solution is O(log n), where n is the number of elements in the array.
- The space complexity of the solution is O(1), as it only uses a constant amount of space to store the indices and the middle element.