# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element, which is an element that is not smaller than its neighbors. The array may contain multiple peak elements, and the solution should return the index of any one of them. The input array will always contain at least one element, and the first and last elements are considered to have only one neighbor. For example, given the array [1, 2, 3, 1], the peak elements are 3, and the solution should return 2, which is the index of 3.

## Approach
The algorithm uses a modified binary search approach to find the peak element in the array. It starts by checking the middle element, and if it's greater than its neighbors, it returns the index of the middle element. Otherwise, it moves to the half of the array where the peak element is more likely to be.

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
            // if mid element is smaller than the next one, peak must be on the right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
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
- The problem can be solved using a modified binary search approach.
- The time complexity of the solution is O(log n), making it efficient for large inputs.
- The space complexity is O(1), as the solution only uses a constant amount of space.