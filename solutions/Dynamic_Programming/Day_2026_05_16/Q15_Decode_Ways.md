# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done in a way that each digit or a pair of digits can represent a letter. For example, "12" can be decoded as "AB" or "L". The string is non-empty and contains only digits from 0 to 9. The function should return the number of ways to decode the given string.

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that index. We can decode a string of length i if the last digit is non-zero or if the last two digits form a number between 10 and 26.

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
        if (s[0] == '0') return 0;
        
        int n = s.length();
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            // Check if the current character can be decoded separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // Check if the current and previous characters can be decoded together
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
- Use dynamic programming to solve problems that have overlapping subproblems.
- Initialize the base cases carefully to avoid incorrect results.
- Consider all possible decoding scenarios for each character or pair of characters.