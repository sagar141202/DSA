# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings. A palindromic substring is a substring that reads the same backward as forward. For example, in the string "abc", "a", "b", and "c" are palindromic substrings. In the string "aaa", "a", "aa", "aaa" are palindromic substrings. The input string will only contain lowercase English letters and will have a length between 1 and 1000.

## Approach
The approach involves using dynamic programming to build a 2D table where each cell represents whether a substring is palindromic or not. We start by marking all substrings of length 1 as palindromic and then move to longer lengths. For a substring to be palindromic, its first and last characters must be the same, and the substring in between must also be palindromic.

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
        
        // Mark all substrings of length 1 as palindromic
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
- We use a dynamic programming approach to avoid redundant computation.
- The 2D table `dp` helps us keep track of whether each substring is palindromic or not.
- We start with substrings of length 1 and move to longer lengths, ensuring that we consider all possible substrings.