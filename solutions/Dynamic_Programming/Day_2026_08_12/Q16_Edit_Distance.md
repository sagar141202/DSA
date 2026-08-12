# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `word1` and `word2`, find the edit distance between them. The constraints are: `1 <= word1.length, word2.length <= 500`, and the strings only contain lowercase English letters. For example, the edit distance between "kitten" and "sitting" is 3 (replace 'k' with 's', replace 'e' with 'i', append 'g').

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell represents the edit distance between substrings of `word1` and `word2`. The intuition is to fill the table in a bottom-up manner by considering the minimum cost of insertion, deletion, or substitution at each step.

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
        int m = word1.size(), n = word2.size();
        // Create a 2D table to store the edit distances
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        // Initialize the base cases
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        
        // Fill the table in a bottom-up manner
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // Check if the current characters match
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    // Consider the minimum cost of insertion, deletion, or substitution
                    dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
                }
            }
        }
        
        // The edit distance is stored in the bottom-right cell
        return dp[m][n];
    }
};
```

## Test Cases
```
Input: word1 = "kitten", word2 = "sitting"
Output: 3
Input: word1 = "intention", word2 = "execution"
Output: 5
```

## Key Takeaways
- The edit distance problem can be solved using dynamic programming with a 2D table.
- The table is filled in a bottom-up manner by considering the minimum cost of insertion, deletion, or substitution at each step.
- The edit distance is stored in the bottom-right cell of the table.