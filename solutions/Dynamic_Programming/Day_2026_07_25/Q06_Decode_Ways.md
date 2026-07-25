# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is non-empty and contains only digits from 0 to 9. The string does not contain any leading zeros.

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that index. The algorithm iterates through the string, considering each digit and pair of digits as potential decodings. The base cases are when the string is empty or only contains one digit.

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
        
        // base case: if the string starts with '0', there is no valid decoding
        if (s[0] != '0') {
            dp[1] = 1;
        }
        
        for (int i = 2; i <= n; i++) {
            // if the current digit is not '0', we can decode it separately
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
- The problem requires considering both individual digits and pairs of digits as potential decodings.
- Dynamic programming is used to efficiently compute the number of ways to decode the string up to each index.
- The base cases and transition rules are crucial in defining the dynamic programming approach.