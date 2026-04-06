# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in the string. A palindromic substring is a substring that reads the same backward as forward. For example, "aba" is a palindromic substring, but "abc" is not. The string will contain only lowercase letters and will have a length between 1 and 1000 characters.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell [i][j] represents whether the substring from index i to j is a palindrome or not. We then count the number of palindromic substrings by iterating over this table. The key intuition is to fill the table in a bottom-up manner, starting with substrings of length 1 and 2.

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
- Use dynamic programming to efficiently store and reuse the results of subproblems.
- The dynamic programming table should be filled in a bottom-up manner to avoid redundant computation.
- The base cases for the dynamic programming approach are substrings of length 1 and 2.