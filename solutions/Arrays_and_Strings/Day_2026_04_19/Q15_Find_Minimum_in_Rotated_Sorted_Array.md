# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a sorted array that has been rotated an unknown number of times. The array was initially sorted in ascending order, but after rotation, the smallest element is now at an unknown position. The array contains distinct integers and has a length of at least 1. For example, given the array [3, 4, 5, 1, 2], the minimum element is 1, and given the array [4, 5, 6, 7, 0, 1, 2], the minimum element is 0.

## Approach
We can solve this problem using a modified binary search algorithm that takes into account the rotation of the array. The idea is to compare the middle element with the rightmost element and decide which half to continue searching in. If the middle element is greater than the rightmost element, the minimum element must be in the right half; otherwise, it must be in the left half.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
```

## Test Cases
```
Input: [3, 4, 5, 1, 2]
Output: 1
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm.
- The time complexity of the solution is O(log n), where n is the number of elements in the array.
- The space complexity of the solution is O(1), as it only uses a constant amount of space.