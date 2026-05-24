# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The problem has a constraint that the input array will have at least one element and at most 1000 elements, with each element being an integer between 0 and 1000. For example, for the input `[10, 9, 2, 5, 3, 7, 101, 18]`, the output will be `4` because the longest increasing subsequence is `[2, 3, 7, 101]`.

## Approach
The algorithm uses dynamic programming to build up a table where each entry represents the length of the longest increasing subsequence ending at that index. The intuition is to compare each element with all previous elements and update the table accordingly. The maximum value in the table will be the length of the longest increasing subsequence.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    // If the input array is empty, return 0
    if (nums.empty()) return 0;
    
    // Initialize a table to store the length of the longest increasing subsequence ending at each index
    vector<int> dp(nums.size(), 1);
    
    // Iterate over the array
    for (int i = 1; i < nums.size(); i++) {
        // For each element, compare it with all previous elements
        for (int j = 0; j < i; j++) {
            // If the current element is greater than the previous element, update the table
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    
    // The length of the longest increasing subsequence is the maximum value in the table
    return *max_element(dp.begin(), dp.end());
}
```

## Test Cases
```
Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Input: [0, 1, 0, 3, 2, 3]
Output: 4
Input: [7, 6, 5, 4, 3, 2]
Output: 1
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The table `dp` is used to store the length of the longest increasing subsequence ending at each index, which helps to avoid redundant computation.
- The maximum value in the table `dp` will be the length of the longest increasing subsequence.