# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to return an array where each element at index `i` is the count of smaller numbers after `i` in the array `nums`. The array `nums` contains distinct integers. For example, given the array `nums = [5,2,6,1]`, the output should be `[2,1,1,0]` because for the element at index 0 (5), there are 2 smaller numbers after it (2 and 1), for the element at index 1 (2), there is 1 smaller number after it (1), for the element at index 2 (6), there is 1 smaller number after it (1), and for the element at index 3 (1), there are no smaller numbers after it.

## Approach
The approach to solve this problem is to use a Binary Indexed Tree (BIT) or a modified merge sort algorithm. The idea is to iterate through the array from right to left, and for each element, count the number of smaller elements to its right. This can be achieved by maintaining a sorted array of elements seen so far and using binary search to find the count of smaller elements.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> result(nums.size());
        vector<int> sorted;
        for (int i = nums.size() - 1; i >= 0; --i) {
            // Find the count of smaller elements to the right of the current element
            auto it = lower_bound(sorted.begin(), sorted.end(), nums[i]);
            result[i] = it - sorted.begin();
            // Insert the current element into the sorted array
            sorted.insert(it, nums[i]);
        }
        return result;
    }
};
```

## Test Cases
```
Input: [5,2,6,1]
Output: [2,1,1,0]
Input: [1,2,3,4,5]
Output: [0,0,0,0,0]
```

## Key Takeaways
- Use a Binary Indexed Tree (BIT) or a modified merge sort algorithm to solve this problem efficiently.
- The time complexity of the solution is O(n log n) due to the use of binary search and insertion into a sorted array.
- The space complexity of the solution is O(n) for storing the sorted array of elements seen so far.