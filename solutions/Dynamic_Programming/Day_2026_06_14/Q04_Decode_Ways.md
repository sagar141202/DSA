# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can represent a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is guaranteed to be non-empty and only contains digits from 0 to 9. The length of the string is in the range [1, 100]. The input string does not contain any leading zeros.

## Approach
This problem can be solved using dynamic programming, where we build up a solution by considering each possible decode of the input string. We can decode a string of length n by either decoding the last character separately or decoding the last two characters together. The approach involves iterating through the string and at each step, calculating the number of ways to decode the string up to that point.

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
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // empty string can be decoded in one way
        
        // if the first character is not zero, it can be decoded separately
        if (s[0] != '0') {
            dp[1] = 1;
        }
        
        for (int i = 2; i <= n; i++) {
            // if the current character is not zero, it can be decoded separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            
            // if the last two characters form a number between 10 and 26, they can be decoded together
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
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The base cases for the dynamic programming approach should be carefully considered to ensure that the solution is correct.
- The time and space complexity of the solution should be analyzed to ensure that it is efficient.