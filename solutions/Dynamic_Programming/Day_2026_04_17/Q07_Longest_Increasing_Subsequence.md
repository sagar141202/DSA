# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums`, find the length of the longest increasing subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The problem can be formally defined as finding the maximum length of a subsequence where every element is larger than its previous element. For example, given the array `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]`, so the output should be `4`. The array can contain up to `10^5` elements and each element can range from `0` to `10^9`.

## Approach
The solution utilizes dynamic programming to solve the problem efficiently. It creates an array `dp` where `dp[i]` stores the length of the longest increasing subsequence ending at index `i`. The algorithm iterates through the array, updating `dp[i]` based on the maximum length of the increasing subsequence found so far.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    if (nums.size() == 0) {
        return 0;
    }

    vector<int> dp(nums.size(), 1);
    int max_length = 1;

    for (int i = 1; i < nums.size(); i++) {
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
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4

Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4

Input: nums = [7, 6, 5, 4, 3, 2]
Output: 1
```

## Key Takeaways
- The dynamic programming approach allows for efficient computation of the longest increasing subsequence by avoiding redundant calculations.
- The use of a `dp` array to store intermediate results enables the algorithm to find the optimal solution in O(n^2) time complexity.
- The problem can be solved using a bottom-up dynamic programming approach, which is more efficient than a recursive top-down approach for large inputs.