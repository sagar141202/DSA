# Find Minimum in Rotated Sorted Array

## Problem Statement
Find the minimum element in a rotated sorted array. The array was originally sorted in ascending order, but it was rotated an unknown number of times. For example, the array [4, 5, 6, 7, 0, 1, 2] was originally [0, 1, 2, 4, 5, 6, 7] but was rotated 4 times. The function should take an array of integers as input and return the minimum element. The array will have at least one element and at most 10,000 elements. The elements will be between 0 and 10,000.

## Approach
The algorithm uses a modified binary search to find the minimum element in the rotated sorted array. It compares the middle element with the rightmost element to determine which half of the array the minimum element is in. The search space is then reduced by half in each iteration.

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
        int left = 0;
        int right = nums.size() - 1;
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
Input: [1]
Output: 1
```

## Key Takeaways
- The algorithm has a time complexity of O(log n) due to the use of binary search.
- The algorithm has a space complexity of O(1) as it only uses a constant amount of space.
- The algorithm can handle arrays with duplicate elements, but it may not work correctly if the array is not rotated.