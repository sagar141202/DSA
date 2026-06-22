# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `word1` and `word2`, find the edit distance between them. The edit distance is defined as the minimum number of operations (insertions, deletions, and substitutions) required to change `word1` into `word2`. For example, given `word1 = "kitten"` and `word2 = "sitting"`, the edit distance is 3 (replace 'k' with 's', replace 'e' with 'i', and append 'g').

## Approach
The approach to solve this problem is to use dynamic programming, where we build a 2D table to store the edit distances between substrings of `word1` and `word2`. We fill up the table by considering the minimum edit distance between substrings of `word1` and `word2` and then use this table to find the edit distance between the entire strings. The key idea is to break down the problem into smaller subproblems and store the solutions to these subproblems to avoid redundant computation.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        
        // Create a 2D table to store the edit distances between substrings
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        // Initialize the base cases
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        
        // Fill up the table by considering the minimum edit distance between substrings
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
                }
            }
        }
        
        // The edit distance between the entire strings is stored in the bottom-right corner of the table
        return dp[m][n];
    }
};
```

## Test Cases
```
Input: word1 = "kitten", word2 = "sitting"
Output: 3
Input: word1 = "hello", word2 = "world"
Output: 4
```

## Key Takeaways
- The edit distance problem can be solved using dynamic programming by building a 2D table to store the edit distances between substrings.
- The key idea is to break down the problem into smaller subproblems and store the solutions to these subproblems to avoid redundant computation.
- The time complexity of the solution is O(m*n), where m and n are the lengths of the input strings.