# Find Peak Element

## Problem Statement
The problem requires finding a peak element in an array, which is an element that is not smaller than its neighbors. Given an array of integers, find an element such that the element is greater than or equal to its neighbors. If there are multiple peak elements, any one of them can be returned. The array can contain duplicate elements and may not be sorted. For example, in the array [1, 2, 3, 1], the peak element is 3. In the array [1, 2, 1, 3, 5, 6, 4], the peak elements are 2 and 6.

## Approach
We can use a binary search approach to find the peak element in the array. The idea is to compare the middle element with its neighbors and move towards the side that has a larger element. This approach works because the peak element must exist in the array, and by comparing the middle element with its neighbors, we can effectively reduce the search space by half in each iteration.

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
            // if mid element is smaller than the next one, 
            // then the peak must be in the right half
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // otherwise, the peak must be in the left half
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
Input: nums = [1, 2, 3, 1]
Output: 2
Input: nums = [1, 2, 1, 3, 5, 6, 4]
Output: 1 or 5
```

## Key Takeaways
- The peak element must exist in the array, so we can use a binary search approach to find it.
- By comparing the middle element with its neighbors, we can effectively reduce the search space by half in each iteration.
- The time complexity of the solution is O(log n), where n is the number of elements in the array.