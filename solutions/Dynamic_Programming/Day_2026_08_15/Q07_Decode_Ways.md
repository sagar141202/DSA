# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can represent a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). However, not all digits or pairs of digits can represent a letter, such as "06" or "27", as there is no letter corresponding to 0 or 27 in the given mapping. The string is guaranteed to only contain digits from 0 to 9.

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that point. The algorithm iterates through the string, considering each digit and pair of digits, and updates the array accordingly. The final result is stored in the last element of the array.

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
        
        // create dp array
        vector<int> dp(n + 1, 0);
        dp[0] = 1; // one way to decode empty string
        
        // fill dp array
        for (int i = 1; i <= n; i++) {
            // check if current digit can be decoded
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // check if last two digits can be decoded
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
- Use dynamic programming to break down the problem into smaller sub-problems and store the results in an array.
- Consider each digit and pair of digits separately to determine the number of ways to decode the string.
- Handle edge cases, such as an empty string or a string containing only zeros.