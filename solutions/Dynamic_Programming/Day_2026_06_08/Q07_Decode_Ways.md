# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is guaranteed to be non-empty and contain only digits.

## Approach
The problem can be solved using dynamic programming by maintaining a DP array where each element represents the number of ways to decode the string up to that index. We can then fill up the DP array by considering each digit or pair of digits and checking if it's a valid mapping.

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
        // Base case: if the string starts with 0, it's not decodable
        if (s[0] == '0') return 0;
        
        // Initialize the DP array
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // empty string has 1 way to decode
        dp[1] = 1; // single digit string has 1 way to decode
        
        // Fill up the DP array
        for (int i = 2; i <= n; i++) {
            // Check if the current digit is non-zero
            if (s[i-1] != '0') {
                dp[i] += dp[i-1];
            }
            // Check if the current and previous digits form a valid mapping
            if (s[i-2] == '1' || (s[i-2] == '2' && s[i-1] <= '6')) {
                dp[i] += dp[i-2];
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
- The problem can be solved using dynamic programming by maintaining a DP array where each element represents the number of ways to decode the string up to that index.
- We need to consider each digit or pair of digits and check if it's a valid mapping to fill up the DP array.
- The base case is when the string starts with 0, in which case it's not decodable.