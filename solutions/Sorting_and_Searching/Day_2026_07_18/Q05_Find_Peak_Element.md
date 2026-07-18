# Find Peak Element

## Problem Statement
The problem requires finding a peak element in an array, where a peak element is an element that is not smaller than its neighbors. The array can be rotated, and there can be duplicate elements. The goal is to find any peak element in the array. For example, given the array `[1, 2, 3, 1]`, the peak element is `3`. The array can be of size up to `10^5` elements, and all elements are integers between `1` and `10^9`.

## Approach
We can solve this problem using a modified binary search algorithm. The idea is to compare the middle element with its neighbors and move towards the side that has a larger element. This approach ensures that we can find a peak element in logarithmic time complexity.

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
            // if mid element is smaller than the next one, then peak must be on the right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // if mid element is larger than the next one, then peak must be on the left side
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
Output: 5
```

## Key Takeaways
- The modified binary search approach is used to solve the problem efficiently.
- The time complexity of the solution is O(log n), making it suitable for large inputs.
- The space complexity is O(1), as only a constant amount of space is used.