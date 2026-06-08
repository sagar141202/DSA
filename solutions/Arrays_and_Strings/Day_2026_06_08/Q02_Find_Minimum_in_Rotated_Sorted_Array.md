# Find Minimum in Rotated Sorted Array

## Problem Statement
Find the minimum element in a rotated sorted array. The array was initially sorted in ascending order, but it was rotated an unknown number of times. For example, given the array [3, 4, 5, 1, 2], the minimum element is 1. The array can contain duplicate elements. The input array will have at least one element.

## Approach
We can use a modified binary search algorithm to solve this problem. The idea is to find the pivot element where the rotation occurred, and then find the minimum element. If the middle element is greater than the rightmost element, the minimum element must be in the right half. Otherwise, it must be in the left half.

## Complexity
- Time: O(n)
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
            } else if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                right--;
            }
        }
        return nums[left];
    }
};
```

## Test Cases
```
Input: [3, 4, 5, 1, 2]
Output: 1
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
Input: [1, 2, 3, 4, 5]
Output: 1
```

## Key Takeaways
- The modified binary search algorithm works well for finding the minimum element in a rotated sorted array.
- Handling duplicate elements is crucial, as it can affect the correctness of the solution.
- The time complexity is O(n) in the worst case, but it can be improved to O(log n) on average if the array is large and the rotation is random.