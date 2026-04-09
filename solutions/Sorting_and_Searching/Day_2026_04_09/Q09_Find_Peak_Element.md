# Find Peak Element

## Problem Statement
The problem requires finding a peak element in an array, where a peak element is an element that is not smaller than its neighbors. The input array will have at least one element and may have multiple peak elements, but we only need to return the index of any one of them. For example, given the input array [1, 2, 3, 1], the output can be 2, which is the index of the peak element 3.

## Approach
We can solve this problem using a binary search approach. The idea is to find the middle element and compare it with its neighbors. If the middle element is greater than its neighbors, it is a peak element. If the middle element is smaller than the left neighbor, the peak element must be in the left half. If the middle element is smaller than the right neighbor, the peak element must be in the right half.

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
            // if mid element is smaller than the next one, peak must be in the right half
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // if mid element is greater than the next one, peak must be in the left half
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
- The binary search approach can be applied to find the peak element in an array.
- The time complexity of this solution is O(log n), which is efficient for large inputs.
- The space complexity is O(1), which means the space required does not change with the size of the input array.