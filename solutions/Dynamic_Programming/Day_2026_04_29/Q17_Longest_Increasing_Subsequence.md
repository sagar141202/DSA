# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence (LIS). A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The LIS is the longest subsequence that is strictly increasing. For example, given the array `[10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]`, so the output should be `4`. The array can contain duplicate elements and can be empty.

## Approach
The problem can be solved using dynamic programming by maintaining an array `dp` where `dp[i]` stores the length of the LIS ending at index `i`. We iterate through the array and for each element, we compare it with all previous elements and update `dp[i]` accordingly. The maximum value in the `dp` array will be the length of the LIS.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    if (nums.empty()) return 0;
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
- The `dp` array is used to store the lengths of the LIS ending at each index, which helps to avoid redundant calculations.
- The time complexity of the solution is O(n^2) due to the nested loops, where n is the length of the input array.