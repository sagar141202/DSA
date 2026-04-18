# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into another. Given two strings `word1` and `word2`, find the edit distance between them. The strings only contain lowercase English letters. The edit distance is calculated using the following rules: 
- Insertion: Insert a character into `word1` to make it more similar to `word2`.
- Deletion: Delete a character from `word1` to make it more similar to `word2`.
- Substitution: Replace a character in `word1` with a character from `word2`.
For example, the edit distance between "kitten" and "sitting" is 3, as we can replace 'k' with 's', replace 'e' with 'i', and append 'g'.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the edit distances between substrings of `word1` and `word2`. The table is filled in a bottom-up manner, and the edit distance between the two strings is stored in the top-right corner of the table. The algorithm iterates over the characters in both strings, considering all possible operations (insertion, deletion, substitution) and choosing the one with the minimum cost.

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
                // If the current characters match, there's no operation needed
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    // Consider all possible operations and choose the one with the minimum cost
                    dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
                }
            }
        }
        
        // The edit distance is stored in the top-right corner of the table
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
- The edit distance problem can be solved using dynamic programming by creating a 2D table to store the edit distances between substrings.
- The algorithm iterates over the characters in both strings, considering all possible operations (insertion, deletion, substitution) and choosing the one with the minimum cost.
- The time complexity of the algorithm is O(m*n), where m and n are the lengths of the input strings.