# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or a pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is non-empty and contains only digits from 0 to 9. The function should return the number of ways to decode the given string.

## Approach
The problem can be solved using dynamic programming, where we build up a solution by considering each digit or pair of digits. We use a DP array to store the number of ways to decode the string up to each position. The algorithm iterates through the string, updating the DP array based on whether the current digit or the last two digits can be decoded.

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
        // Base case: empty string has 1 way to decode (no decoding)
        if (n == 0) return 1;
        
        // Initialize DP array with 0s
        vector<int> dp(n + 1, 0);
        // Base case: 1 way to decode a string of length 1 if it's not 0
        dp[0] = 1;
        if (s[0] != '0') dp[1] = 1;
        
        // Fill up the DP array
        for (int i = 2; i <= n; i++) {
            // If the current digit is not 0, we can decode it separately
            if (s[i - 1] != '0') dp[i] += dp[i - 1];
            // If the last two digits are between 10 and 26, we can decode them together
            if (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6')) dp[i] += dp[i - 2];
        }
        
        // The answer is stored in the last position of the DP array
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
- The problem can be solved using dynamic programming by considering each digit or pair of digits.
- The DP array is used to store the number of ways to decode the string up to each position.
- The base cases are when the string is empty (1 way to decode) or when the string starts with a non-zero digit (1 way to decode the first digit).