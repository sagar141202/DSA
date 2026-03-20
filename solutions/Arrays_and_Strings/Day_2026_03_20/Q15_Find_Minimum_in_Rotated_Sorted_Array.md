# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem asks to find the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order, but then its elements were rotated some number of positions. For example, the array [4, 5, 6, 7, 0, 1, 2] is a rotation of the sorted array [0, 1, 2, 4, 5, 6, 7]. The minimum element in this array is 0. The array may contain duplicates. The function should return the minimum element in the rotated sorted array.

## Approach
The algorithm uses a modified binary search approach to find the minimum element in the rotated sorted array. It compares the middle element with the rightmost element to determine which half of the array the minimum element is in. If the middle element is greater than the rightmost element, the minimum element must be in the right half; otherwise, it must be in the left half.

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
- The algorithm uses a modified binary search approach to find the minimum element in the rotated sorted array.
- The time complexity is O(n) in the worst case when the array contains all identical elements.
- The space complexity is O(1) as it only uses a constant amount of space.