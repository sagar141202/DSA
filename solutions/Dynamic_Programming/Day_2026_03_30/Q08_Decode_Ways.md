# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can represent a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is non-empty and contains only digits from 0 to 9. The string does not contain any leading zeros unless the string itself is "0".

## Approach
This problem can be solved using dynamic programming, where we build up a solution by considering each digit or pair of digits and determining the number of ways to decode the string up to that point. We use a DP array to store the number of ways to decode the string up to each position. The algorithm iterates through the string, considering each digit and updating the DP array accordingly.

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
        
        // base case: if the string starts with '0', there is no way to decode it
        if (s[0] == '0') {
            dp[1] = 0;
        } else {
            dp[1] = 1;
        }
        
        for (int i = 2; i <= n; i++) {
            // if the current digit is not '0', we can decode it separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            
            // if the last two digits form a valid number (10-26), we can decode them together
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
- The problem can be solved using dynamic programming by considering each digit or pair of digits and updating the DP array accordingly.
- The base case is when the string starts with '0', in which case there is no way to decode it.
- The time complexity is O(n), where n is the length of the input string, and the space complexity is also O(n) due to the DP array.