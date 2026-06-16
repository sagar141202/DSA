# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done in a way that each digit or a pair of digits can represent a character. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is guaranteed to be non-empty and contain only digits from 0 to 9. The function should return the number of ways to decode the given string.

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that point. We can then fill up this array by considering each digit and pairs of digits. The base case is when the string is empty or contains only one digit.

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
        // Create a dp array to store the number of ways to decode the string up to each point
        vector<int> dp(n + 1, 0);
        
        // Base case: there is one way to decode an empty string
        dp[0] = 1;
        
        // If the first digit is not zero, there is one way to decode it
        if (s[0] != '0') {
            dp[1] = 1;
        }
        
        // Fill up the dp array
        for (int i = 2; i <= n; i++) {
            // If the current digit is not zero, we can decode it separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // If the last two digits form a number between 10 and 26, we can decode them together
            if (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6')) {
                dp[i] += dp[i - 2];
            }
        }
        
        // The number of ways to decode the entire string is stored in the last element of the dp array
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
- The problem can be solved using dynamic programming with a time complexity of O(n) and a space complexity of O(n).
- We need to consider each digit and pairs of digits when filling up the dp array.
- The base case is when the string is empty or contains only one digit.