# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The array may contain multiple peak elements, and we need to find any one of them. The constraints are: the array will have at least one element, and the first and last elements are considered to have only one neighbor.

## Approach
We can use a modified binary search algorithm to find a peak element. The idea is to compare the middle element with its neighbors and move towards the side that has a larger element. This approach ensures that we will always find a peak element if one exists.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            // if mid element is smaller than the next one, move to the right half
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // otherwise, move to the left half
            else {
                right = mid;
            }
        }
        return left;
    }
};
```

## Test Cases
```
Input: nums = [1,2,3,1]
Output: 2
Input: nums = [1,2,1,3,5,6,4]
Output: 5
```

## Key Takeaways
- The problem can be solved using a modified binary search approach.
- The time complexity is reduced to O(log n) due to the binary search.
- The space complexity is O(1) as no extra space is used.