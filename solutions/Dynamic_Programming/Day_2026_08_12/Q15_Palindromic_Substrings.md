# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in the string. A palindromic substring is a substring that reads the same backward as forward. The string can contain any ASCII characters and has a length between 1 and 1000. For example, in the string "abc", there are 3 palindromic substrings: "a", "b", and "c". In the string "aaa", there are 6 palindromic substrings: "a", "a", "a", "aa", "aa", and "aaa".

## Approach
The approach to solve this problem is to use dynamic programming to store whether each substring is palindromic or not. We will create a 2D table where each cell [i][j] represents whether the substring from index i to j is palindromic. We will then count the number of palindromic substrings by iterating over the table.

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
                if (dp[i + 1][j - 1] && s[i] == s[j]) {
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
- We use a dynamic programming approach to store whether each substring is palindromic or not.
- The time complexity is O(n^2) due to the nested loops used to fill the dp table.
- The space complexity is O(n^2) for the dp table.