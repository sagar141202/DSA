# Longest Increasing Subsequence

## Problem Statement
Given an array of integers, find the length of the longest increasing subsequence (LIS). A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, given the array `[10, 22, 9, 33, 21, 50, 41, 60, 80]`, the longest increasing subsequence is `[10, 22, 33, 50, 60, 80]`. The constraints are: `1 <= arr.length <= 1000` and `0 <= arr[i] <= 1000`.

## Approach
The algorithm uses dynamic programming to solve the problem by maintaining an array `dp` where `dp[i]` stores the length of the longest increasing subsequence ending at index `i`. The intuition is to iterate over the array and for each element, compare it with all previous elements to find the maximum length of the increasing subsequence.

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
    vector<int> nums = {10, 22, 9, 33, 21, 50, 41, 60, 80};
    cout << "Length of LIS: " << lengthOfLIS(nums) << endl;
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
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The `dp` array is used to store the lengths of the longest increasing subsequences ending at each index.
- The time complexity is O(n^2) due to the nested loops, and the space complexity is O(n) for storing the `dp` array.