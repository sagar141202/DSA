# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in the string. A palindromic substring is a substring that reads the same backward as forward. For example, in the string "abc", there are 3 palindromic substrings: "a", "b", and "c". In the string "aaa", there are 6 palindromic substrings: "a", "a", "a", "aa", "aa", and "aaa". The input string will only contain lowercase English letters and will have a length between 1 and 1000.

## Approach
We can use dynamic programming to solve this problem by maintaining a 2D table where each cell represents whether the corresponding substring is palindromic or not. We will fill up the table in a bottom-up manner, starting from substrings of length 1 and going up to substrings of the maximum length.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
```

## Test Cases
```
Input: "abc"
Output: 3
Input: "aaa"
Output: 6
```

## Key Takeaways
- We used a dynamic programming approach to store and reuse the results of subproblems.
- The time complexity is O(n^2) because we are filling up a 2D table of size n x n.
- The space complexity is also O(n^2) because of the 2D table used to store the dynamic programming state.