# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is a 1-based index mapping, meaning '1' maps to 'A', '2' maps to 'B', etc. For example, "12" can be decoded as "AB" (1 2) or "L" (12). The string is non-empty and contains only digits from 0-9. The string does not contain leading zeros unless the only character is "0".

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that point. We can build up this array by considering the last one or two digits of the string and determining how many ways they can be decoded.

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
        // Base case: if the string starts with '0', it cannot be decoded
        if (s[0] == '0') return 0;
        
        // Initialize an array to store the number of ways to decode the string up to each point
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // there is one way to decode an empty string (i.e., do nothing)
        dp[1] = 1; // there is one way to decode a string of length 1 (i.e., decode the single digit)
        
        // Fill in the rest of the array
        for (int i = 2; i <= n; i++) {
            // If the current digit is not '0', we can decode it separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // If the last two digits form a valid number (i.e., between 10 and 26), we can decode them together
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
- Dynamic programming can be used to solve problems that have overlapping subproblems, such as this one.
- The key to solving this problem is to maintain an array where each element represents the number of ways to decode the string up to that point.
- The final answer can be obtained by looking up the last element of the array.