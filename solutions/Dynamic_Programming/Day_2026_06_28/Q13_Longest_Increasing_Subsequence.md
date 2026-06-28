# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums`, find the length of the longest increasing subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, given the array `[10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]`, so the output should be `4`. The array can contain up to `1000` elements and each element is between `0` and `10^9`. The goal is to find the most efficient solution to solve this problem.

## Approach
The algorithm uses dynamic programming to solve the problem by maintaining an array `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. We iterate through the array and for each element, we compare it with all previous elements and update `dp[i]` accordingly. The maximum value in `dp` will be the length of the longest increasing subsequence.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    // If the input array is empty, return 0
    if (nums.empty()) {
        return 0;
    }

    // Initialize the dp array with 1s, since a single element is always an increasing subsequence
    vector<int> dp(nums.size(), 1);

    // Initialize the maximum length of increasing subsequence
    int maxLength = 1;

    // Iterate through the array
    for (int i = 1; i < nums.size(); i++) {
        // For each element, compare it with all previous elements
        for (int j = 0; j < i; j++) {
            // If the current element is greater than the previous element, update dp[i]
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }

        // Update the maximum length
        maxLength = max(maxLength, dp[i]);
    }

    // Return the maximum length of increasing subsequence
    return maxLength;
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
- The dynamic programming approach is used to solve the problem efficiently.
- The `dp` array is used to store the length of the longest increasing subsequence ending at each index.
- The maximum value in `dp` represents the length of the longest increasing subsequence in the entire array.