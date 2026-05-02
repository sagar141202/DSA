# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The input array will always have a peak element. If there are multiple peak elements, any of them can be returned as the result. The array can be unsorted and may contain duplicate elements. For example, in the array [1, 2, 3, 1], the peak elements are 2 and 3.

## Approach
The approach to solve this problem is to use a modified binary search algorithm. We start by checking the middle element of the array. If the middle element is greater than its neighbors, it is a peak element. If the middle element is smaller than the left neighbor, we repeat the process on the left half of the array. If the middle element is smaller than the right neighbor, we repeat the process on the right half of the array.

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
            // If the middle element is smaller than the next element, 
            // the peak must be on the right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // If the middle element is greater than the next element, 
            // the peak must be on the left side
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
- The modified binary search algorithm is used to find the peak element in the array.
- The time complexity of this solution is O(log n), where n is the number of elements in the array.
- The space complexity of this solution is O(1), as it only uses a constant amount of space.