# Longest Increasing Subsequence

## Problem Statement
Given a sequence of integers, find the length of the longest increasing subsequence. An increasing subsequence is a sequence of numbers where every number is greater than the previous number. The subsequence can be non-contiguous. For example, in the sequence [10, 22, 9, 33, 21, 50, 41, 60, 80], the longest increasing subsequence is [10, 22, 33, 50, 60, 80] with a length of 6. The sequence can contain duplicate numbers and can be of any length up to 10^5.

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the length of the longest increasing subsequence ending at that index. The algorithm iterates over the array, updating the lengths based on whether the current element can extend any previous increasing subsequences.

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
    int maxLength = 1;

    for (int i = 1; i < nums.size(); i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        maxLength = max(maxLength, dp[i]);
    }

    return maxLength;
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
- Dynamic programming is used to solve the problem efficiently by avoiding redundant computations.
- The solution has a time complexity of O(n^2) due to the nested loop structure, where n is the length of the input sequence.
- The space complexity is O(n) for storing the dynamic programming array.