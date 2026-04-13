# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done in a way that each digit or a pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is non-empty and contains only digits from 0 to 9. The function should return the number of ways to decode the string.

## Approach
The problem can be solved using dynamic programming, where each state represents the number of ways to decode the string up to a certain position. The algorithm iterates through the string, considering each digit and pair of digits as potential mappings to letters. The base cases are when the string is empty or only contains one digit.

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
        // Base case: empty string
        if (n == 0) return 0;
        
        // Initialize dp array
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // One way to decode an empty string
        
        // Fill dp array
        for (int i = 1; i <= n; i++) {
            // Check if current digit can be decoded
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // Check if last two digits can be decoded
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
- Use dynamic programming to break down the problem into smaller sub-problems.
- Initialize a dp array to store the number of ways to decode the string up to each position.
- Fill the dp array by considering each digit and pair of digits as potential mappings to letters.
- Handle base cases and edge cases, such as an empty string or a string containing only zeros.