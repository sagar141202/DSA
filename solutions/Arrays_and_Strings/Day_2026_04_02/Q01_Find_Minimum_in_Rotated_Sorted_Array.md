# Find Minimum in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find the minimum element in the array. The array was originally sorted in ascending order, but it was rotated at some point, and we need to find the smallest element. For example, if the original array was `[1, 2, 3, 4, 5]`, it could have been rotated to `[3, 4, 5, 1, 2]` or `[5, 1, 2, 3, 4]`. The constraints are that the array will have at least one element and at most 10^4 elements, and each element will be between 1 and 10^4.

## Approach
We will use a modified binary search algorithm to find the minimum element in the rotated sorted array. The idea is to compare the middle element with the rightmost element and decide which half to continue searching in. This approach takes advantage of the fact that the array is sorted and rotated, allowing us to find the minimum element efficiently.

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
            // if the middle element is greater than the rightmost element, 
            // the minimum element must be in the right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // if the middle element is less than or equal to the rightmost element, 
            // the minimum element must be in the left half
            else {
                right = mid;
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
```

## Key Takeaways
- The modified binary search algorithm is efficient for finding the minimum element in a rotated sorted array.
- The time complexity is O(log n) because we divide the search space in half at each step.
- The space complexity is O(1) because we only use a constant amount of space to store the indices and the minimum element.