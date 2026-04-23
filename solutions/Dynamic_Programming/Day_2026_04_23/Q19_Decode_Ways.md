# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done in a way that each digit or a pair of digits can represent a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is guaranteed to be non-empty and contain only digits from 0 to 9. The function should return the number of ways to decode the given string.

## Approach
The problem can be solved using dynamic programming. We create a DP array where each element represents the number of ways to decode the string up to that index. We iterate over the string and for each character, we check if it can be decoded separately or together with the previous character.

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
        // Base case: if the string starts with 0, it cannot be decoded
        if (s[0] == '0') return 0;
        
        // Initialize the DP array
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // empty string can be decoded in one way
        dp[1] = 1; // single character can be decoded in one way
        
        // Iterate over the string
        for (int i = 2; i <= n; i++) {
            // Check if the current character can be decoded separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // Check if the current character can be decoded together with the previous character
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
- The problem can be solved using dynamic programming by creating a DP array where each element represents the number of ways to decode the string up to that index.
- We need to handle the base case where the string starts with 0, which cannot be decoded.
- We iterate over the string and for each character, we check if it can be decoded separately or together with the previous character.