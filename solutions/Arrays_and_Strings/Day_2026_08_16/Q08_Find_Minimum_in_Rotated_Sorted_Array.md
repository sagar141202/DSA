# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a sorted array that has been rotated an unknown number of times. The array is sorted in ascending order, but it has been rotated (clockwise) by some number of positions. For example, if the original array is [1, 2, 3, 4, 5], it can be rotated to [3, 4, 5, 1, 2] or [5, 1, 2, 3, 4]. The task is to find the minimum element in such an array. The array will contain distinct elements and will not be empty.

## Approach
The algorithm uses a modified binary search approach to find the minimum element in the rotated sorted array. It compares the middle element with the rightmost element to determine which half of the array the minimum element is in. The algorithm repeats this process until the minimum element is found.

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
        // Initialize two pointers, one at the start and one at the end of the array
        int left = 0, right = nums.size() - 1;
        
        // Continue the search until the two pointers meet
        while (left < right) {
            // Calculate the middle index
            int mid = left + (right - left) / 2;
            
            // If the middle element is greater than the rightmost element, the minimum must be in the right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // If the middle element is less than or equal to the rightmost element, the minimum must be in the left half
            else {
                right = mid;
            }
        }
        
        // At this point, left and right pointers are the same, and they point to the minimum element
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
- The problem can be solved using a modified binary search approach.
- The algorithm has a time complexity of O(log n), making it efficient for large arrays.
- The algorithm assumes that the input array is non-empty and contains distinct elements.