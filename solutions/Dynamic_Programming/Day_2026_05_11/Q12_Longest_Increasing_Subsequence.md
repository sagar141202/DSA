# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, given the array `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]`, which has a length of `4`. The constraints are `1 <= n <= 1000` and `0 <= nums[i] <= 10^4`.

## Approach
The algorithm uses dynamic programming to solve the problem. It initializes a DP array `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. Then, it iterates over the array and updates `dp[i]` by comparing the current element with all previous elements.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        // Initialize DP array with all elements as 1
        vector<int> dp(n, 1);
        
        int max_length = 1;
        // Iterate over the array
        for (int i = 1; i < n; i++) {
            // Compare the current element with all previous elements
            for (int j = 0; j < i; j++) {
                // If the current element is greater than the previous element, update DP
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            // Update the maximum length
            max_length = max(max_length, dp[i]);
        }
        return max_length;
    }
};
```

## Test Cases
```
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4
Input: nums = [7, 6, 5, 4, 3, 2]
Output: 1
```

## Key Takeaways
- Dynamic programming is used to solve the problem efficiently.
- The DP array `dp` is used to store the length of the longest increasing subsequence ending at each index.
- The time complexity is O(n^2) due to the nested loops, and the space complexity is O(n) for the DP array.