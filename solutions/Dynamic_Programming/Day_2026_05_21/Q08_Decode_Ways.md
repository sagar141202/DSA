# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that the numbers 1-26 correspond to the letters A-Z. For example, "12" can be decoded as "AB" or "L". The string will only contain digits from 0-9 and will be at most 100 characters long.

## Approach
We use dynamic programming to solve this problem by maintaining an array where each element represents the number of ways to decode the string up to that point. We consider each digit and check if it can be decoded separately or together with the previous digit.

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
        // Base case: if the string starts with 0, it cannot be decoded
        if (s[0] == '0') return 0;
        
        int n = s.length();
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // empty string can be decoded in 1 way
        dp[1] = 1; // single digit can be decoded in 1 way
        
        for (int i = 2; i <= n; i++) {
            // If the current digit is not 0, it can be decoded separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // If the last two digits are between 10 and 26, they can be decoded together
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
- Use dynamic programming to break down the problem into smaller subproblems and store the results to avoid redundant computation.
- Consider the base cases and edge cases, such as the string starting with 0 or being empty.
- Use a bottom-up approach to fill up the dp array, starting from the smallest subproblems and building up to the final solution.