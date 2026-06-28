# Palindromic Substrings

## Problem Statement
Given a string, count the total number of palindromic substrings. A palindromic substring is a substring that reads the same backward as forward. The string will contain only lowercase English letters. The length of the string will be between 1 and 1000 characters.

## Approach
We will use dynamic programming to solve this problem by maintaining a 2D table where each cell represents whether the corresponding substring is palindromic or not. We'll then count all the palindromic substrings.

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
- We initialize a 2D DP table `dp` where `dp[i][j]` represents whether the substring from index `i` to `j` is palindromic or not.
- We start by marking all substrings with one character as palindromes and then move to longer lengths.
- For lengths greater than 2, a substring is palindromic if its first and last characters are the same and the substring in between is also palindromic.