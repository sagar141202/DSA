# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done in a way that each digit or a pair of digits can represent a character. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is non-empty and contains only digits from 0 to 9. The string does not contain any leading zeros, and all digits are valid.

## Approach
We can solve this problem using dynamic programming, where each state represents the number of ways to decode the string up to a certain position. We consider two cases: decoding the current digit separately or decoding it together with the previous digit. We update the state based on these cases and finally return the last state.

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
        // base case: empty string
        if (n == 0) return 0;
        
        // initialize dp array
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // one way to decode an empty string
        
        // fill dp array
        for (int i = 1; i <= n; i++) {
            // if current digit is not zero, we can decode it separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // if current and previous digits form a valid number, we can decode them together
            if (i >= 2 && (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6'))) {
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
- Use dynamic programming to break down the problem into smaller sub-problems and store the results in a dp array.
- Consider all possible cases for decoding the string, including decoding the current digit separately or together with the previous digit.
- Update the dp array based on these cases and return the last state as the result.