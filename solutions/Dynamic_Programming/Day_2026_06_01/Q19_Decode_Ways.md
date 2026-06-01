# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is valid if at least one encoding is possible. Constraints: 1 <= s.length <= 100, s contains only digits from 0 to 9.

## Approach
The problem can be solved using dynamic programming by building up a solution from smaller sub-problems. We create a DP array where dp[i] represents the number of ways to decode the string up to index i. We fill up the DP array by considering each digit or pair of digits and checking if they can be decoded.

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
        
        // fill up the DP array
        for (int i = 1; i <= n; i++) {
            // check if the current digit can be decoded
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // check if the last two digits can be decoded
            if (i >= 2 && s[i - 2] != '0' && stoi(s.substr(i - 2, 2)) <= 26) {
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
- Dynamic programming can be used to solve problems that have overlapping sub-problems.
- The DP array can be filled up in a bottom-up manner by considering each sub-problem and building up the solution.
- The time and space complexity of the solution should be analyzed to ensure it is efficient.