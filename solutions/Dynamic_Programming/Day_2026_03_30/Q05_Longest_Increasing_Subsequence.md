# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, given the array `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]` and its length is `4`. The constraints are `1 <= n <= 1000` and `0 <= nums[i] <= 10^9`.

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

int main() {
    vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << lengthOfLIS(nums) << endl;
    return 0;
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
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The time complexity can be improved to O(n log n) using a binary search approach.
- The space complexity can be improved to O(1) if we only need to find the length of the longest increasing subsequence and not the subsequence itself.