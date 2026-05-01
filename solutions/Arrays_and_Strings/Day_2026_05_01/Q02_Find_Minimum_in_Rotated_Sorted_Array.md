# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order, but then rotated (or shifted) by some number of positions. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotated sorted array because it was initially sorted as `[0, 1, 2, 4, 5, 6, 7]` and then rotated by 4 positions. The constraints are that the array will not be empty, and there will be no duplicates in the array. The goal is to find the minimum element in this rotated sorted array.

## Approach
The algorithm uses a modified binary search approach to find the minimum element. It starts by checking the middle element of the array and comparing it with the last element. If the middle element is greater than the last element, the minimum element must be in the right half. Otherwise, it must be in the left half. This process is repeated until the minimum element is found.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left];
    }
};
```

## Test Cases
```
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
Input: [3, 4, 5, 1, 2]
Output: 1
```

## Key Takeaways
- The problem can be solved using a modified binary search approach.
- The time complexity of the solution is O(log n), where n is the number of elements in the array.
- The space complexity of the solution is O(1), as it only uses a constant amount of space to store the indices and the minimum element.