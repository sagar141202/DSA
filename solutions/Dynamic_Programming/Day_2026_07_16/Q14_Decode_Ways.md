# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done in a way that each digit can be decoded independently, but a digit '0' cannot be decoded on its own. For example, the string "12" can be decoded as "AB" or "L". However, "10" can only be decoded as "J" because "0" cannot be decoded independently.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller subproblems. We create a DP array where each index represents the number of ways to decode the string up to that point. The number of ways to decode a string at a given index depends on whether the current digit can be decoded independently or with the previous digit.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        // Base case: if the string is empty or starts with '0', there is no way to decode it
        if (n == 0 || s[0] == '0') return 0;
        
        // Initialize the DP array
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // There is one way to decode an empty string
        dp[1] = 1; // There is one way to decode a string of length 1
        
        // Fill up the DP array
        for (int i = 2; i <= n; i++) {
            // If the current digit can be decoded independently
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // If the current digit can be decoded with the previous digit
            if (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6')) {
                dp[i] += dp[i - 2];
            }
        }
        
        return dp[n];
    }
};
```

## Test Cases
```
Input: "12"
Output: 2
Input: "226"
Output: 3
Input: "0"
Output: 0
```

## Key Takeaways
- The problem can be broken down into smaller subproblems using dynamic programming.
- The number of ways to decode a string at a given index depends on whether the current digit can be decoded independently or with the previous digit.
- The base case for the dynamic programming approach is when the string is empty or starts with '0', in which case there is no way to decode it.