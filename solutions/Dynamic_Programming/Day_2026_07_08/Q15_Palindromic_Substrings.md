# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in it. A palindromic substring is a substring that reads the same backward as forward. For example, in the string "abc", there are 3 palindromic substrings: "a", "b", and "c". In the string "aaa", there are 6 palindromic substrings: "a", "a", "a", "aa", "aa", and "aaa". The input string will contain only lowercase English letters and will have a length between 1 and 1000.

## Approach
We will use dynamic programming to solve this problem, creating a 2D table to store whether each substring is palindromic or not. The algorithm will iterate over the string, checking for palindromes of different lengths. We will start with substrings of length 1 and then move to longer lengths.

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
        int n = s.length();
        int count = 0;
        // Create a 2D table to store whether each substring is palindromic or not
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        
        // All substrings of length 1 are palindromes
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
- Use dynamic programming to efficiently store and reuse results for subproblems.
- Initialize a 2D table to store whether each substring is palindromic or not.
- Start with substrings of length 1 and then move to longer lengths, checking for palindromes at each step.