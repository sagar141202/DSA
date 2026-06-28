# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A sorted array is rotated when it is shifted by a certain number of positions. For example, the array [3, 4, 5, 1, 2] is a rotation of the sorted array [1, 2, 3, 4, 5]. The minimum element in this array is 1. The input array will contain distinct integers and will not be empty. The array can be rotated any number of times.

## Approach
We can use a modified binary search algorithm to solve this problem. The idea is to find the pivot point where the rotation occurred. If the middle element is greater than the rightmost element, the pivot point must be in the right half of the array. If the middle element is less than the rightmost element, the pivot point must be in the left half of the array.

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
Input: [3, 4, 5, 1, 2]
Output: 1
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
Input: [1]
Output: 1
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm.
- The pivot point where the rotation occurred can be found by comparing the middle element with the rightmost element.
- The time complexity of the solution is O(log n) and the space complexity is O(1).