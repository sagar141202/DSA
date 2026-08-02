# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is guaranteed to be non-empty and contain only digits.

## Approach
We can solve this problem using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that point. We iterate through the string, considering each digit and pair of digits separately. The algorithm builds up the solution by adding the number of ways to decode the current substring to the total count.

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
        
        // base case: if the first digit is not zero, there is one way to decode it
        if (s[0] != '0') {
            dp[1] = 1;
        }
        
        for (int i = 2; i <= n; i++) {
            // if the current digit is not zero, we can decode it separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // if the last two digits form a number between 10 and 26, we can decode them together
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The base case is crucial in dynamic programming, and it should be handled carefully.
- The transition from one state to another should be well-defined and consistent.