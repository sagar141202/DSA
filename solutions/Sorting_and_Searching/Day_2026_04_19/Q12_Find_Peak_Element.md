# Find Peak Element

## Problem Statement
The problem requires finding a peak element in an array, which is an element that is not smaller than its neighbors. The input array will have at least one element and may have multiple peak elements. The goal is to find any one of the peak elements. For example, given the array [1, 2, 3, 1], the peak element is 3. The array can have duplicate elements and may be unsorted.

## Approach
The algorithm uses a binary search approach to find the peak element. It starts by finding the middle element and comparing it with its neighbors. If the middle element is greater than its neighbors, it is a peak element. If the middle element is smaller than its left neighbor, the peak element must be in the left half. If the middle element is smaller than its right neighbor, the peak element must be in the right half.

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
            // If the middle element is smaller than the next one, the peak must be on the right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // If the middle element is greater than the next one, the peak must be on the left side
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
- The problem can be solved using a binary search approach, reducing the time complexity to O(log n).
- The algorithm works by comparing the middle element with its neighbors and adjusting the search space accordingly.
- The solution does not require any extra space, resulting in a space complexity of O(1).