# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done in a way that each digit can be decoded independently, and a pair of digits can also be decoded together if the pair forms a number between 10 and 26. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is guaranteed to be non-empty and contain only digits.

## Approach
The problem can be solved using dynamic programming, where we build up a solution by computing the number of ways to decode the string up to each position. We consider two cases: decoding the current digit independently and decoding the current and previous digits together.

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
        dp[0] = 1; // base case: one way to decode an empty string
        dp[1] = (s[0] != '0') ? 1 : 0; // base case: one way to decode a single digit if it's not zero

        for (int i = 2; i <= n; i++) {
            // if the current digit is not zero, we can decode it independently
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // if the current and previous digits form a number between 10 and 26, we can decode them together
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
- Use dynamic programming to build up a solution by computing the number of ways to decode the string up to each position.
- Consider two cases: decoding the current digit independently and decoding the current and previous digits together.
- Handle edge cases, such as when the input string contains zeros or when the input string is empty.