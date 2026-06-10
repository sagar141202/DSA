# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order but has been rotated an unknown number of times. The array contains distinct integers. For example, given the array [3, 4, 5, 1, 2], the minimum element is 1. The array can be rotated any number of times, and the minimum element can be anywhere in the array. The constraints are that the array will have at least one element and at most 10^4 elements, and each element will be between 1 and 10^4.

## Approach
We can use a modified binary search algorithm to find the minimum element in the rotated sorted array. The algorithm works by dividing the array into two halves and checking which half contains the minimum element. This process is repeated until the minimum element is found. The key intuition is that the minimum element will be the first element in the unrotated part of the array.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMin(vector<int>& nums) {
    int left = 0;
    int right = nums.size() - 1;
    
    // if the array is not rotated, return the first element
    if (nums[left] < nums[right]) {
        return nums[left];
    }
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        // if the middle element is greater than the right element, the minimum element must be in the right half
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } 
        // if the middle element is less than or equal to the right element, the minimum element must be in the left half
        else {
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
Input: [1]
Output: 1
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm.
- The key intuition is to find the first element in the unrotated part of the array, which will be the minimum element.
- The time complexity is O(log n) and the space complexity is O(1), making it efficient for large inputs.