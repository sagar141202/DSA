# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order but has been rotated (clockwise) by an unknown number of positions. For example, the array [4, 5, 6, 7, 0, 1, 2] is a rotated sorted array because it can be obtained by rotating the sorted array [0, 1, 2, 4, 5, 6, 7] by 4 positions. The array may contain duplicate elements. The goal is to find the minimum element in the rotated sorted array.

## Approach
We will use a modified binary search algorithm to find the minimum element in the rotated sorted array. The algorithm will compare the middle element with the rightmost element and decide which half to continue searching in. If the middle element is greater than the rightmost element, the minimum element must be in the right half; otherwise, it must be in the left half.

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
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
Input: [3, 3, 1, 3]
Output: 1
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm.
- The algorithm has a time complexity of O(n) in the worst case, where n is the number of elements in the array.
- The algorithm has a space complexity of O(1), as it only uses a constant amount of space.