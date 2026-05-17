# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The array may contain multiple peak elements, in that case, return the index of any one of the peak element. The input array will always have at least one element and the answer will always exist.

## Approach
We will use a modified binary search algorithm to find the peak element in the array. The idea is to compare the middle element with its neighbors and move towards the side that has a larger element. This approach ensures that we will always find a peak element.

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
            } else {
                // if mid element is larger than the next one, then peak must be on the left side
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
- The modified binary search algorithm is used to find the peak element in the array.
- The time complexity of this solution is O(log n) which makes it efficient for large inputs.
- The space complexity is O(1) as we only use a constant amount of space to store the indices.