# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is non-empty and contains only digits from 0 to 9. The function should return the number of ways to decode the string.

## Approach
The problem can be solved using dynamic programming, where we build up a solution by considering each digit or pair of digits and determining the number of ways to decode the string up to that point. We use a bottom-up approach, starting from the beginning of the string and working our way to the end. At each step, we consider whether the current digit can be decoded separately or as part of a pair with the previous digit.

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
        if (n == 0 || s[0] == '0') return 0;
        
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // base case: one way to decode an empty string
        dp[1] = 1; // base case: one way to decode a single digit
        
        for (int i = 2; i <= n; i++) {
            // if the current digit is not zero, we can decode it separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // if the last two digits are between 10 and 26, we can decode them together
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
- The problem can be solved using dynamic programming with a bottom-up approach.
- We need to consider both the case where the current digit is decoded separately and the case where it is decoded as part of a pair with the previous digit.
- The base cases are when the string is empty or contains only one digit.