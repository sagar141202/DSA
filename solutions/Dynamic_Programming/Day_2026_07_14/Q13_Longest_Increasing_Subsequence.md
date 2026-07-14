# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The subsequence should be increasing, meaning that every element is greater than its previous element. For example, given the array `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]`, and its length is `4`. Constraints: `0 <= n <= 10^5`, `0 <= nums[i] <= 10^9`.

## Approach
The algorithm uses dynamic programming to build up a table where each entry represents the length of the longest increasing subsequence ending at that index. The intuition is to compare each element with all previous elements and update the table accordingly. The maximum length of the longest increasing subsequence is then the maximum value in the table.

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
        int max_length = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The longest increasing subsequence problem can be solved using a bottom-up dynamic programming approach.
- The time complexity of the solution can be improved using a binary search approach to find the correct position to insert the current element in the dynamic programming table.