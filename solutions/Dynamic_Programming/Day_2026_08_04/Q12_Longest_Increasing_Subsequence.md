# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of size `n`, find the length of the longest increasing subsequence (LIS). A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The LIS is a subsequence where every element is greater than its previous element. For example, given the array `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]`, and its length is `4`. The constraints are `1 <= n <= 1000` and `0 <= nums[i] <= 10^9`.

## Approach
The algorithm uses dynamic programming to build up a table where each entry represents the length of the LIS ending at that index. The intuition is to compare each element with all previous elements and update the table accordingly. The final result is the maximum value in the table.

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
        if (n == 0) return 0;
        
        // Initialize a table to store the length of LIS ending at each index
        vector<int> dp(n, 1);
        
        // Initialize the maximum length of LIS
        int max_length = 1;
        
        // Fill up the table
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                // If the current element is greater than the previous element, update the table
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            // Update the maximum length of LIS
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
- The dynamic programming approach is used to solve the LIS problem efficiently.
- The time complexity is O(n^2) due to the nested loops, and the space complexity is O(n) for storing the table.
- The algorithm can be further optimized using binary search to achieve a time complexity of O(n log n).