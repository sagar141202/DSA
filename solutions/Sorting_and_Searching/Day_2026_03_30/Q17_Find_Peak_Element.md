# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The array may contain multiple peak elements, in that case, return the index of any one of the peak elements. The input array will always have at least one element and may contain duplicates. For example, given the array [1, 2, 3, 1], the output could be 2 (since 3 is a peak element), and given the array [1, 2, 1, 3, 5, 6, 4], the output could be either 1 or 5.

## Approach
The approach is to use a modified binary search algorithm to find the peak element in the array. The idea is to compare the middle element with its neighbors and move towards the side that has a larger element. This ensures that we are always moving towards a peak element.

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
            // If the middle element is smaller than the next element, 
            // then the peak element must be in the right half
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // If the middle element is larger than the next element, 
            // then the peak element must be in the left half
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
Input: [1, 2, 3, 1]
Output: 2
Input: [1, 2, 1, 3, 5, 6, 4]
Output: 5
```

## Key Takeaways
- The binary search approach can be used to find the peak element in an array.
- The time complexity of the solution is O(log n) because we are dividing the search space in half at each step.
- The space complexity of the solution is O(1) because we are only using a constant amount of space to store the indices and the middle element.