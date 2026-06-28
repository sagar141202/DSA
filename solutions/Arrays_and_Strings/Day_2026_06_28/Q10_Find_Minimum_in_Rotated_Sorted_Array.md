# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order, but then its elements were rotated (shifted) by some number of positions. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotated sorted array because it can be obtained by rotating the sorted array `[0, 1, 2, 4, 5, 6, 7]` by 4 positions. The problem statement guarantees that there are no duplicate elements in the array and that the array is non-empty. The goal is to write an efficient algorithm to find the minimum element in such an array.

## Approach
The algorithm uses a modified binary search approach to find the minimum element in the rotated sorted array. It works by maintaining two pointers, one at the start and one at the end of the array, and iteratively narrowing down the search range until the minimum element is found. The key intuition is to compare the middle element with the rightmost element to determine which half of the array the minimum element is in.

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
        
        // If the array is not rotated, the minimum element is at the start
        if (nums[left] < nums[right]) {
            return nums[left];
        }
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            // If the middle element is greater than the rightmost element, 
            // the minimum element must be in the right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // If the middle element is less than or equal to the rightmost element, 
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
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0

Input: [3, 4, 5, 1, 2]
Output: 1

Input: [1]
Output: 1
```

## Key Takeaways
- The problem can be solved using a modified binary search approach.
- The key to the solution is to compare the middle element with the rightmost element to determine which half of the array the minimum element is in.
- The time complexity of the solution is O(log n), making it efficient for large inputs.