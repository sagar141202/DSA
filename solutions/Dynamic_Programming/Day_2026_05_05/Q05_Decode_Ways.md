# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done in a way that each digit or a pair of digits can represent a character. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is non-empty and contains only digits from 0 to 9. The length of the string is up to 100 characters.

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that point. We iterate over the string, considering each digit and each pair of digits to update the array. The final result will be the last element in the array.

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
        int n = s.length();
        if (n == 0 || s[0] == '0') return 0;
        
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            // Check if the current digit can be decoded
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // Check if the last two digits can be decoded
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
- The problem can be solved using dynamic programming by maintaining an array to store the number of ways to decode the string up to each point.
- We need to consider each digit and each pair of digits to update the array.
- The final result will be the last element in the array, representing the total number of ways to decode the entire string.