# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence (LIS) in the array. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The LIS is the longest subsequence that is strictly increasing. For example, given the array `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]`, so the output should be `4`. The array can contain duplicate elements and can be empty.

## Approach
The algorithm uses dynamic programming to solve the problem. It initializes an array `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. It then iterates over the array, updating `dp[i]` whenever it finds a smaller element that can be appended to the subsequence. The maximum value in `dp` is the length of the longest increasing subsequence.

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
        if (nums.empty()) return 0;
        
        int n = nums.size();
        vector<int> dp(n, 1);
        
        int maxLength = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            maxLength = max(maxLength, dp[i]);
        }
        
        return maxLength;
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
- The `dp` array is used to store the length of the longest increasing subsequence ending at each index.
- The time complexity is O(n^2) due to the nested loops, and the space complexity is O(n) for the `dp` array.