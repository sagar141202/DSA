# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done in a way that each digit or a pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is non-empty and contains only digits from 0 to 9. The string does not contain any leading zeros.

## Approach
We use dynamic programming to solve this problem by maintaining an array where each element represents the number of ways to decode the string up to that point. We iterate over the string and for each digit, we check if it can be decoded independently or together with the previous digit.

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
        dp[0] = 1;
        
        // If the first digit is not zero, it can be decoded
        if (s[0] != '0') {
            dp[1] = 1;
        }
        
        for (int i = 2; i <= n; i++) {
            // Check if the current digit can be decoded independently
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            
            // Check if the current and previous digits can be decoded together
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
- We use dynamic programming to break down the problem into smaller sub-problems and store the results in an array to avoid redundant calculations.
- We handle the base cases where the first digit is zero or the string is empty.
- We iterate over the string and for each digit, we check if it can be decoded independently or together with the previous digit, and update the dp array accordingly.