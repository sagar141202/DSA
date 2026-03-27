# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `word1` and `word2`, find the edit distance between them. The strings only contain lowercase letters, and the length of each string is at most 100. For example, the edit distance between "kitten" and "sitting" is 3, because we can change "kitten" to "sitting" by changing the "k" to an "s", changing the "e" to an "i", and appending a "g".

## Approach
We will use dynamic programming to solve this problem, building a 2D table where each cell represents the edit distance between substrings of `word1` and `word2`. The final edit distance will be stored in the bottom-right cell of the table.

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
        
        // Create a 2D table to store edit distances
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        // Initialize the base cases
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        
        // Fill in the rest of the table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
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
- The table is filled in row by row, with each cell representing the edit distance between substrings of the input strings.
- The final edit distance is stored in the bottom-right cell of the table.