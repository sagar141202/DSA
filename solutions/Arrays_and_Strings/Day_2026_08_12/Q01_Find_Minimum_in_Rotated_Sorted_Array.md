# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a sorted array that has been rotated an unknown number of times. The array was initially sorted in ascending order, but after rotation, the smallest element is now at some unknown position. The task is to write an efficient algorithm to find this minimum element. The array can contain duplicate elements and the rotation can be to the left or right. For example, given the array [4, 5, 6, 7, 0, 1, 2], the minimum element is 0. If the array is [3, 3, 1, 3], the minimum element is 1.

## Approach
The algorithm will use a modified binary search approach to find the minimum element in the rotated sorted array. It will compare the middle element with the rightmost element to determine which half of the array the minimum element is in. This process will be repeated until the minimum element is found.

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
        
        // if the array is not rotated, return the first element
        if (nums[left] < nums[right]) {
            return nums[left];
        }
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            // if the middle element is greater than the rightmost element, 
            // the minimum element must be in the right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // if the middle element is less than the rightmost element, 
            // the minimum element must be in the left half
            else if (nums[mid] < nums[right]) {
                right = mid;
            } 
            // if the middle element is equal to the rightmost element, 
            // we can't be sure which half the minimum element is in, 
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
Input: [1, 2, 3, 4, 5]
Output: 1
```

## Key Takeaways
- The problem can be solved using a modified binary search approach.
- The algorithm has a time complexity of O(log n) on average, but can be O(n) in the worst case when all elements are the same.
- The algorithm uses a constant amount of space, making it efficient for large inputs.