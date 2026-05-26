# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can be mapped to a character, and the string should be decoded in a way that each character is mapped to a valid digit or pair of digits. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is guaranteed to only contain digits from 0 to 9.

## Approach
The problem can be solved using dynamic programming, where we build up a solution by considering each digit or pair of digits as a possible decode. We maintain an array where each element represents the number of ways to decode the string up to that point. We iterate through the string, considering each digit and pair of digits, and update the array accordingly.

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
- The problem can be solved using dynamic programming by maintaining an array to store the number of ways to decode the string up to each point.
- The time complexity is O(n), where n is the length of the input string, because we only need to iterate through the string once.
- The space complexity is O(n) because we need to store the array of size n + 1.