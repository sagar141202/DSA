# Find Peak Element

## Problem Statement
The problem requires finding a peak element in an array, where a peak element is an element that is not smaller than its neighbors. The array can contain duplicate elements and may not be sorted. The problem has the following constraints: the input array will have at least one element, and the first and last elements are considered to have only one neighbor. For example, given the array [1, 2, 3, 1], the peak element is 3. If there are multiple peak elements, the problem requires finding any one of them.

## Approach
The algorithm uses a modified binary search approach to find the peak element. It starts by comparing the middle element with its neighbors and moves towards the side that has a larger element. This process continues until the peak element is found.

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
- The space complexity is O(1), as the solution only uses a constant amount of space to store the indices.