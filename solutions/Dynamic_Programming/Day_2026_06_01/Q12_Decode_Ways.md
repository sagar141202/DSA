# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can represent a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is non-empty and contains only digits from 0 to 9. 1 <= s.length <= 100.

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that point. We iterate over the string, considering each digit and pair of digits to update the array. The base case is when the string is empty or only contains one digit.

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
        // Base case: if the string is empty or starts with 0, there's no way to decode it
        if (s.empty() || s[0] == '0') return 0;
        
        int n = s.length();
        // Initialize an array to store the number of ways to decode the string up to each point
        vector<int> dp(n + 1, 0);
        // There's one way to decode an empty string
        dp[0] = 1;
        // There's one way to decode a string with one digit if it's not 0
        dp[1] = 1;
        
        // Iterate over the string
        for (int i = 2; i <= n; i++) {
            // If the current digit is not 0, we can decode it separately
            if (s[i - 1] != '0') dp[i] += dp[i - 1];
            // If the last two digits are between 10 and 26, we can decode them together
            if (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6')) dp[i] += dp[i - 2];
        }
        
        // The number of ways to decode the entire string is stored in the last element of the array
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
- Dynamic programming can be used to solve problems with overlapping subproblems.
- The problem requires considering each digit and pair of digits to update the array.
- The base case is when the string is empty or starts with 0, in which case there's no way to decode it.