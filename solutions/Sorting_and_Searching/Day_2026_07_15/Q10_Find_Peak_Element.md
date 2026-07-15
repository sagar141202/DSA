# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The array may contain multiple peak elements, in that case, return the index of any one of the peak elements. The input array will always have at least one element and the first and last elements are considered to be neighbors of each other (i.e., the array is circular). For example, if the input array is [1, 2, 3, 1], the output should be 2 because 3 is the peak element in this array.

## Approach
We can solve this problem using a modified binary search algorithm. The idea is to compare the middle element with its neighbors and move towards the side that has a larger element. This approach works because a peak element must exist in the array.

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
            // if the middle element is smaller than the next one, the peak must be on the right side
            if (nums[mid] < nums[mid + 1])
                left = mid + 1;
            // otherwise, the peak must be on the left side
            else
                right = mid;
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
- The problem can be solved using a modified binary search algorithm.
- The time complexity of the solution is O(log n) because we are dividing the search space in half at each step.
- The space complexity is O(1) because we are only using a constant amount of space to store the indices and the input array.