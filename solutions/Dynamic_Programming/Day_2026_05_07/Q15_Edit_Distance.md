# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `word1` and `word2`, find the edit distance between them. The strings only contain lowercase English letters. The length of `word1` is `m` and the length of `word2` is `n`, where `1 <= m, n <= 500`. The allowed operations are: insert a character, delete a character, and replace a character.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the edit distance between substrings of `word1` and `word2`. We fill the table in a bottom-up manner. The edit distance is calculated by considering the minimum cost of insertion, deletion, and substitution.

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
                // Calculate the cost of substitution
                int cost = (word1[i - 1] == word2[j - 1]) ? 0 : 1;
                
                // Calculate the edit distance
                dp[i][j] = min(min(dp[i - 1][j] + 1,      // Deletion
                                    dp[i][j - 1] + 1),      // Insertion
                               dp[i - 1][j - 1] + cost);  // Substitution
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
- The edit distance problem can be solved using dynamic programming by building a 2D table.
- The table is filled in a bottom-up manner by considering the minimum cost of insertion, deletion, and substitution.
- The edit distance is calculated by finding the minimum cost path in the table.