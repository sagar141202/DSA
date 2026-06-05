# Find Minimum in Rotated Sorted Array

## Problem Statement
Find the minimum element in a rotated sorted array. The array was initially sorted in ascending order, but it was rotated an unknown number of times. For example, given the array [3, 4, 5, 1, 2], the minimum element is 1. The array may contain duplicates. The function should return the index of the minimum element.

## Approach
We can use a modified binary search algorithm to solve this problem, taking into account the rotation of the array. The key idea is to compare the middle element with the rightmost element to determine which half of the array the minimum element is in.

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
- The problem can be solved using a modified binary search algorithm.
- The key idea is to compare the middle element with the rightmost element to determine which half of the array the minimum element is in.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.