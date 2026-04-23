# Find Peak Element

## Problem Statement
The problem requires finding a peak element in an unsorted array. A peak element is an element that is not smaller than its neighbors. For an array, a peak element can be defined as an element a[i] such that a[i] >= a[i-1] and a[i] >= a[i+1] for all valid i. If the element is at the beginning or end of the array, it only needs to be greater than or equal to one neighbor. The input array will always have at least one element and may have duplicate elements. The goal is to find any peak element in the array.

## Approach
The algorithm uses a modified binary search approach to find the peak element efficiently. It compares the middle element with its neighbors and decides which half to continue searching in. This approach ensures a logarithmic time complexity.

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
            // If the middle element is smaller than the next one, 
            // then the peak must be on the right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // Otherwise, the peak must be on the left side
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
Input: nums = [1,2,3,1]
Output: 2
Input: nums = [1,2,1,3,5,6,4]
Output: 5
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm.
- The key to solving this problem efficiently is to compare the middle element with its neighbors and decide which half to continue searching in.
- The solution has a time complexity of O(log n) and a space complexity of O(1), making it efficient for large inputs.