# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings within it. A palindromic substring is a substring that reads the same backward as forward. The input string will only contain lowercase English letters. The length of the input string will be between 1 and 1000 characters.

## Approach
The approach to solve this problem is to use dynamic programming to build a 2D table where each cell represents whether a substring is palindromic or not. We will then count the total number of palindromic substrings.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        int count = 0;
        
        // All substrings with one character are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            count++;
        }
        
        // Check for substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                count++;
            }
        }
        
        // Check for lengths greater than 2
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                if (s[i] == s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    count++;
                }
            }
        }
        
        return count;
    }
};
```

## Test Cases
```
Input: "abc"
Output: 3
Input: "aaa"
Output: 6
```

## Key Takeaways
- Use dynamic programming to build a 2D table for storing palindromic substrings.
- Start with substrings of length 1 and 2, and then expand to longer lengths.
- Count the total number of palindromic substrings by checking the 2D table.