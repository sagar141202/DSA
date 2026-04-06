# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order, but then rotated (or shifted) by some number of positions. For example, the array [4, 5, 6, 7, 0, 1, 2] is a rotated sorted array because it can be obtained by rotating the sorted array [0, 1, 2, 4, 5, 6, 7] by 4 positions. The array can contain duplicate elements. The goal is to find the minimum element in the rotated array.

## Approach
The algorithm uses a modified binary search approach to find the minimum element in the rotated array. It checks the middle element of the current search range and compares it with the rightmost element to determine which half of the array the minimum element is in. The algorithm repeats this process until the search range is narrowed down to a single element, which is the minimum element.

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
        int left = 0;
        int right = nums.size() - 1;
        
        // if the array is not rotated
        if (nums[left] < nums[right]) {
            return nums[left];
        }
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            // if the middle element is greater than the rightmost element
            // the minimum element must be in the right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            }
            // if the middle element is less than the rightmost element
            // the minimum element must be in the left half
            else if (nums[mid] < nums[right]) {
                right = mid;
            }
            // if the middle element is equal to the rightmost element
            // we cannot determine which half the minimum element is in
            // so we move the right pointer one step to the left
            else {
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
Input: [2, 2, 2, 0, 1]
Output: 0
```

## Key Takeaways
- The algorithm uses a modified binary search approach to find the minimum element in the rotated array.
- The algorithm checks the middle element of the current search range and compares it with the rightmost element to determine which half of the array the minimum element is in.
- The algorithm handles duplicate elements by moving the right pointer one step to the left when the middle element is equal to the rightmost element.