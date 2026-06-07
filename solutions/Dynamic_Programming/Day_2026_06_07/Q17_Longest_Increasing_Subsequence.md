# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of size `n`, find the length of the longest increasing subsequence (LIS). A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The LIS is the longest subsequence that is strictly increasing. For example, given the array `nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]`, the LIS is `[10, 22, 33, 50, 60, 80]` and its length is `6`. The constraints are `1 <= n <= 10^5` and `0 <= nums[i] <= 10^9`.

## Approach
The algorithm uses dynamic programming to build up a table where each entry represents the length of the LIS ending at that index. The intuition is to compare each element with all previous elements and update the table accordingly. The final answer is the maximum value in the table.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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

int main() {
    vector<int> nums = {10, 22, 9, 33, 21, 50, 41, 60, 80};
    cout << lengthOfLIS(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: 6
Input: [1, 2, 3, 4, 5]
Output: 5
Input: [5, 4, 3, 2, 1]
Output: 1
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems and optimal substructure.
- The time complexity of the algorithm can be improved to O(n log n) using a binary search approach.
- The space complexity can be reduced to O(1) if only the maximum length is required, not the actual subsequence.