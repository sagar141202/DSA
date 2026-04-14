# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence (LIS) in the array. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The LIS is the longest subsequence that is strictly increasing. For example, given `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]`, so the output should be `4`. The array may contain duplicate elements and may not be sorted.

## Approach
The approach to solve this problem is to use dynamic programming, where we maintain an array `dp` such that `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. We iterate through the array and for each element, we compare it with all previous elements and update `dp[i]` accordingly.

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
        // if the array is empty, return 0
        if (nums.empty()) return 0;
        
        // initialize dp array with 1's
        vector<int> dp(nums.size(), 1);
        
        // initialize max length
        int maxLength = 1;
        
        // iterate through the array
        for (int i = 1; i < nums.size(); i++) {
            // for each element, compare it with all previous elements
            for (int j = 0; j < i; j++) {
                // if current element is greater than previous element, update dp[i]
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            // update max length
            maxLength = max(maxLength, dp[i]);
        }
        
        // return max length
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
- The dynamic programming approach is used to solve this problem efficiently.
- The `dp` array is used to store the length of the longest increasing subsequence ending at each index.
- The time complexity of this solution is O(n^2) due to the nested loops.