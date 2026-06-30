# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `word1` and `word2`, find the edit distance between them. The allowed operations are: 
- Insertion: Insert a character into `word1`.
- Deletion: Delete a character from `word1`.
- Substitution: Replace a character in `word1` with a character from `word2`.
For example, given `word1 = "kitten"` and `word2 = "sitting"`, the edit distance is 3 (replace 'k' with 's', replace 'e' with 'i', append 'g').

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the edit distance between substrings of `word1` and `word2`. The edit distance for the current cell is determined by considering the minimum cost of insertion, deletion, and substitution operations.

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
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        // Initialize the base cases
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        
        // Fill the dp table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]));
                }
            }
        }
        
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
- The edit distance problem can be solved using dynamic programming with a time complexity of O(m*n), where m and n are the lengths of the input strings.
- The space complexity is O(m*n) due to the 2D dp table used to store the edit distances between substrings.
- The problem has numerous applications in data comparison, plagiarism detection, and machine learning.