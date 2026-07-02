# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can be mapped to a letter. However, a pair of digits can only be mapped if the pair forms a number between 10 and 26. For example, "12" can be decoded as "AB" or "L".

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that point. We can then fill up this array by considering each digit or pair of digits and checking if they can be decoded.

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
        int n = s.size();
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            // check if current digit can be decoded
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // check if last two digits can be decoded
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
- The dynamic programming approach helps to avoid redundant calculations and improve efficiency.
- The base cases, such as when the string starts with '0', need to be handled carefully.
- The transition from one state to another in the dynamic programming array is based on the decoding rules.