# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1->A, 2->B) or "L" (12->L). The string is non-empty and contains only digits from 0 to 9.

## Approach
The problem can be solved using dynamic programming, where we build up a solution by considering each digit or pair of digits and counting the number of ways to decode them. We use a bottom-up approach, starting from the first digit and moving forward. The key idea is to consider whether the current digit can be decoded separately or together with the previous digit.

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
        // Create a dp array to store the number of ways to decode the string up to each position
        vector<int> dp(n + 1, 0);
        // Base case: there is one way to decode an empty string
        dp[0] = 1;
        // If the first digit is not zero, there is one way to decode it
        if (s[0] != '0') dp[1] = 1;
        // Iterate over the string from the second digit to the end
        for (int i = 2; i <= n; i++) {
            // If the current digit is not zero, we can decode it separately
            if (s[i - 1] != '0') dp[i] += dp[i - 1];
            // If the last two digits form a number between 10 and 26, we can decode them together
            if (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6')) dp[i] += dp[i - 2];
        }
        // The number of ways to decode the entire string is stored in the last position of the dp array
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
- The problem can be solved using dynamic programming with a time complexity of O(n) and space complexity of O(n).
- The key idea is to consider whether the current digit can be decoded separately or together with the previous digit.
- The solution uses a bottom-up approach, starting from the first digit and moving forward, and stores the number of ways to decode the string up to each position in a dp array.