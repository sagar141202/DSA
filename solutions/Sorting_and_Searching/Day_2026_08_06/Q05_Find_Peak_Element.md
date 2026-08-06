# Find Peak Element

## Problem Statement
The problem requires finding a peak element in an unsorted array. A peak element is an element that is not smaller than its neighbors. For an array of size n, the neighbors of an element at index i are the elements at indices i-1 and i+1, except for the first element (which only has a right neighbor) and the last element (which only has a left neighbor). The input array will always have at least one element and may contain duplicate elements. The goal is to find any peak element in the given array. For example, given the array [1, 2, 3, 1], the peak element is 3.

## Approach
The algorithm uses a binary search approach to find the peak element. It starts by finding the middle element of the array and comparing it with its neighbors. If the middle element is greater than its neighbors, it is a peak element. If the middle element is smaller than its left neighbor, the peak element must be in the left half of the array. If the middle element is smaller than its right neighbor, the peak element must be in the right half of the array.

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
- The binary search approach is used to find the peak element in O(log n) time complexity.
- The algorithm only uses a constant amount of space, making it space-efficient.
- The solution handles edge cases, such as arrays with only one element or arrays with duplicate elements.