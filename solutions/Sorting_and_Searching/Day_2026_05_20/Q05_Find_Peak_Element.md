# Find Peak Element

## Problem Statement
The problem requires finding a peak element in an array, where a peak element is an element that is greater than its neighbors. The array can be unsorted, and there can be multiple peak elements. However, it is guaranteed that at least one peak element exists. The problem can be solved using a binary search approach. The constraints are: the array will have at least one element, and the array will have a length of at most 10^4 elements. For example, given the array [1, 2, 3, 1], the output can be 2 (the index of the peak element 3).

## Approach
The algorithm uses a binary search approach to find the peak element. If the middle element is greater than its neighbors, it is a peak element. Otherwise, the algorithm checks if the left neighbor is greater than the middle element. If it is, the peak element must be in the left half; otherwise, it must be in the right half.

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
            if (nums[mid] > nums[mid + 1])
                right = mid;
            else
                left = mid + 1;
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
- The problem can be solved using a binary search approach with a time complexity of O(log n).
- The algorithm uses a two-pointer approach to narrow down the search range.
- The solution does not require any extra space, making it space-efficient with a space complexity of O(1).