# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is guaranteed to be non-empty and contain only digits from 0 to 9. The length of the string will be in the range [1, 100]. The string does not contain any leading zeros unless the string itself is "0", in which case there is only one way to decode it.

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that point. The number of ways to decode the string up to a certain point depends on whether the current digit can be decoded separately or together with the previous digit.

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
            // check if the current digit can be decoded separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            
            // check if the current digit can be decoded together with the previous digit
            int num = stoi(s.substr(i - 2, 2));
            if (num >= 10 && num <= 26) {
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
- The dynamic programming approach allows us to break down the problem into smaller subproblems and store the results of each subproblem to avoid redundant computation.
- The base cases for the dynamic programming approach are when the string is empty or contains only one digit.
- The transition function for the dynamic programming approach depends on whether the current digit can be decoded separately or together with the previous digit.