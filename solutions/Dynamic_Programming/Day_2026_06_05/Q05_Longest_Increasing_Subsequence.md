# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence (LIS). A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The LIS is the longest subsequence that is strictly increasing. For example, given the array `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the LIS is `[2, 3, 7, 101]` and its length is `4`. The constraints are `1 <= n <= 1000` and `0 <= nums[i] <= 10^9`.

## Approach
The approach to solve this problem is to use dynamic programming, where we maintain an array `dp` of length `n` to store the length of the LIS ending at each position. We iterate through the array and for each element, we find the maximum length of the LIS ending at the previous positions that are smaller than the current element. The algorithm has a time complexity of O(n^2) and a space complexity of O(n).

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
        vector<int> dp(n, 1);
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        
        return *max_element(dp.begin(), dp.end());
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
- The dynamic programming approach is used to solve the problem efficiently.
- The time complexity of the solution is O(n^2) due to the nested loops.
- The space complexity is O(n) as we need to store the `dp` array of length `n`.