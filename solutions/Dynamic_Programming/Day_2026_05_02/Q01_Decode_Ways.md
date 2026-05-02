# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits between 10 and 26 (inclusive) can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is non-empty and contains only digits from 0 to 9.

## Approach
The problem can be solved using dynamic programming by building up a solution from smaller sub-problems. We create a DP array where each index represents the number of ways to decode the string up to that point. We then fill up the DP array by considering each digit or pair of digits and the number of ways they can be decoded.

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
        // Create a DP array to store the number of ways to decode the string up to each point
        vector<int> dp(n + 1, 0);
        // Base case: there is one way to decode an empty string
        dp[0] = 1;
        
        // Fill up the DP array
        for (int i = 1; i <= n; i++) {
            // If the current digit is not zero, we can decode it separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // If the last two digits are between 10 and 26, we can decode them together
            if (i >= 2 && (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6'))) {
                dp[i] += dp[i - 2];
            }
        }
        // The number of ways to decode the entire string is stored in the last index of the DP array
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
- The problem can be solved using dynamic programming by building up a solution from smaller sub-problems.
- We need to consider each digit or pair of digits and the number of ways they can be decoded.
- The base case is that there is one way to decode an empty string.