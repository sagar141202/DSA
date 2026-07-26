# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order but has been rotated (clockwise) by an unknown number of positions. For example, the array [4, 5, 6, 7, 0, 1, 2] is a rotated version of the sorted array [0, 1, 2, 4, 5, 6, 7]. The array may contain duplicate elements. The goal is to write an efficient algorithm that can find the minimum element in such an array.

## Approach
The approach involves using a modified binary search algorithm to find the minimum element in the rotated sorted array. The algorithm checks the middle element and compares it with the rightmost element to decide which half of the array to search in. This process continues until the minimum element is found.

## Complexity
- Time: O(n) in the worst case when all elements are the same, but O(log n) on average
- Space: O(1) as only a constant amount of space is used

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
                // so we remove the rightmost element
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
- The algorithm handles duplicate elements by removing the rightmost element when the middle element is equal to the rightmost element.
- The time complexity of the algorithm is O(n) in the worst case, but O(log n) on average.