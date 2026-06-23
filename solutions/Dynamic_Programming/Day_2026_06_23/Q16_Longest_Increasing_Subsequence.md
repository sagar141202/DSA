# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence (LIS) in the array. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The LIS is the longest subsequence that is strictly increasing. For example, given the array `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the LIS is `[2, 3, 7, 101]` and its length is `4`. The constraints are `1 <= n <= 1000` and `0 <= nums[i] <= 10^9`.

## Approach
The algorithm uses dynamic programming to build up a table where each entry `dp[i]` represents the length of the LIS ending at index `i`. The intuition is to compare each element with all previous elements and update `dp[i]` if a longer increasing subsequence is found. The final answer is the maximum value in the `dp` table.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    // Initialize dp table with all ones, since a single element is an increasing subsequence of length 1
    vector<int> dp(n, 1);
    int max_length = 1;
    for (int i = 1; i < n; i++) {
        // Compare current element with all previous elements
        for (int j = 0; j < i; j++) {
            // If current element is greater than previous element, update dp[i] if necessary
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        // Update max_length if a longer increasing subsequence is found
        max_length = max(max_length, dp[i]);
    }
    return max_length;
}

int main() {
    vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << lengthOfLIS(nums) << endl;  // Output: 4
    return 0;
}
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
- The LIS problem can be solved using dynamic programming with a time complexity of O(n^2).
- The `dp` table is used to store the length of the LIS ending at each index.
- The final answer is the maximum value in the `dp` table, which represents the length of the longest increasing subsequence in the array.