# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done in a way that '10' can be decoded as 'J' and '1' followed by '0' can be decoded as 'A' followed by nothing (since 0 cannot be decoded on its own). For example, "12" can be decoded as "AB" or "L". The string is guaranteed to be a valid encoding, but it may contain leading zeros.

## Approach
We will use dynamic programming to solve this problem, where dp[i] represents the number of ways to decode the string up to index i. We will consider each digit and the possibility of combining it with the previous digit to form a valid encoding.

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
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // base case: one way to decode an empty string
        if (s[0] != '0') dp[1] = 1; // base case: one way to decode a single digit if it's not zero
        
        for (int i = 2; i <= n; i++) {
            // if the current digit is not zero, we can decode it separately
            if (s[i - 1] != '0') dp[i] += dp[i - 1];
            // if the last two digits form a valid encoding (10-26), we can decode them together
            if (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6')) dp[i] += dp[i - 2];
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
- We use dynamic programming to store the number of ways to decode the string up to each index.
- We consider each digit and the possibility of combining it with the previous digit to form a valid encoding.
- The base cases are when the string is empty (one way to decode) or when the string has only one digit (one way to decode if it's not zero).