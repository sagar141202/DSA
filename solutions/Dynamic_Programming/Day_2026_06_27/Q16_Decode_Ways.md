# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done in a way that each digit can represent a letter, and two consecutive digits can also represent a letter if the number formed by them is between 10 and 26. For example, "12" can be decoded as "AB" or "L". The string is guaranteed to be non-empty and only contains digits from 0 to 9.

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that index. We can fill up this array by considering each digit and the possibility of combining it with the previous digit. The algorithm iterates over the input string, updating the array based on the current digit and the previous digits.

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
        // Base case: empty string has one way to decode (the empty string itself)
        if (n == 0) return 1;
        
        // Initialize dp array with zeros
        vector<int> dp(n + 1, 0);
        dp[0] = 1;  // one way to decode an empty string
        
        // Fill up dp array
        for (int i = 1; i <= n; i++) {
            // If current digit is not zero, it can be decoded separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // If current and previous digits form a number between 10 and 26, 
            // they can be decoded together
            if (i >= 2 && (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6'))) {
                dp[i] += dp[i - 2];
            }
        }
        
        // The last element of dp array represents the number of ways to decode the entire string
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
- We use dynamic programming to solve this problem efficiently by avoiding redundant computations.
- The dp array is used to store the number of ways to decode the string up to each index.
- We consider each digit and the possibility of combining it with the previous digit to fill up the dp array.