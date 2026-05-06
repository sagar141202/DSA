# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem involves finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order, but then rotated (shifted) by some number of positions. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotated sorted array because it was initially sorted as `[0, 1, 2, 4, 5, 6, 7]` and then rotated by 4 positions. The goal is to find the minimum element in such an array. The array will contain at least one element and may contain duplicates. The function should return the index of the minimum element.

## Approach
The algorithm uses a modified binary search approach to find the minimum element. It compares the middle element with the rightmost element and adjusts the search range accordingly. If the middle element is greater than the rightmost element, the minimum element must be in the right half; otherwise, it must be in the left half.

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
        
        // if the array is not rotated
        if (nums[left] < nums[right]) {
            return nums[left];
        }
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            // if the middle element is greater than the rightmost element
            if (nums[mid] > nums[right]) {
                // the minimum element must be in the right half
                left = mid + 1;
            } else if (nums[mid] < nums[right]) {
                // the minimum element must be in the left half
                right = mid;
            } else {
                // if the middle element is equal to the rightmost element
                // we can't be sure which half the minimum element is in
                // so we reduce the search range by one element
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
- The algorithm has a time complexity of O(log n) due to the use of binary search.
- The algorithm can handle arrays with duplicate elements by reducing the search range by one element when the middle element is equal to the rightmost element.
- The algorithm assumes that the input array is non-empty and contains at least one element.