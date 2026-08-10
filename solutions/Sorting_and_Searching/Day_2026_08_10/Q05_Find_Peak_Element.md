# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The array may contain multiple peak elements, and we need to find any one of them. The input array will always have at least one element and will not be empty. For example, in the array [1, 2, 3, 1], the peak elements are 3. In the array [1, 2, 1, 3, 5, 6, 4], the peak elements are 2, 5, and 6.

## Approach
The algorithm uses a modified binary search to find the peak element. It compares the middle element with its neighbors and moves the search space accordingly. If the middle element is greater than its neighbors, it is a peak element. If the middle element is smaller than the left neighbor, the peak element must be in the left half. If the middle element is smaller than the right neighbor, the peak element must be in the right half.

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
            // If middle element is smaller than the next one, the peak must be on the right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                // If middle element is greater than or equal to the next one, the peak must be on the left side
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
- The algorithm has a logarithmic time complexity because it uses binary search to find the peak element.
- The algorithm has a constant space complexity because it only uses a few variables to store the indices and does not use any additional data structures that scale with the input size.
- The algorithm can be used to find the peak element in any array, not just arrays with a single peak element.