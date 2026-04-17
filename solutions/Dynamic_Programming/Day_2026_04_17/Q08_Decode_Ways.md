# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is guaranteed to be non-empty and contain only digits.

## Approach
We can solve this problem using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that point. We consider each digit or pair of digits and update the array accordingly. The base case is when the string is empty or contains only one digit.

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
        dp[0] = 1; // empty string
        dp[1] = 1; // single digit
        
        for (int i = 2; i <= n; i++) {
            // check single digit
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // check pair of digits
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
- Dynamic programming is used to break down the problem into smaller sub-problems and store their solutions to avoid redundant computation.
- The base case is crucial in dynamic programming, and in this case, it's when the string is empty or contains only one digit.
- The transition from one state to another is based on the current digit or pair of digits, and we update the dp array accordingly.