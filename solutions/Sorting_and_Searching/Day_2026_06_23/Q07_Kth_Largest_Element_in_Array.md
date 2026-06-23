# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, find the kth largest element in the array. The kth largest element is the element that would be at index `k-1` if the array were sorted in descending order. You may assume that `1 <= k <= nums.size()` and that `nums` contains at least `k` elements. For example, if `nums = [3,2,1,5,6,4]` and `k = 2`, the kth largest element is `5`. If `nums = [1,2,3,4,5]` and `k = 1`, the kth largest element is `5`.

## Approach
The algorithm uses the built-in sort function in C++ to sort the array in descending order. Then it returns the element at index `k-1`. This approach is straightforward but not the most efficient for large inputs. A more efficient approach would be to use a priority queue or the nth_element function.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Sort the array in descending order
        sort(nums.rbegin(), nums.rend());
        // Return the kth largest element
        return nums[k-1];
    }
};
```

## Test Cases
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Input: nums = [1,2,3,4,5], k = 1
Output: 5
```

## Key Takeaways
- The problem can be solved by sorting the array in descending order and returning the element at index `k-1`.
- The time complexity of the solution is O(n log n) due to the sorting operation.
- A more efficient solution can be achieved using a priority queue or the nth_element function, which would reduce the time complexity to O(n log k) or O(n) respectively.