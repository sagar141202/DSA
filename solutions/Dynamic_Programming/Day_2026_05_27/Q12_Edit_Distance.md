# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into another. Given two strings `str1` and `str2` with lengths `m` and `n` respectively, find the edit distance between them. The allowed operations are: 
- Insertion: Insert a character into `str1`.
- Deletion: Delete a character from `str1`.
- Substitution: Replace a character in `str1` with a character from `str2`.
The edit distance is also known as the Levenshtein distance.

## Approach
The problem can be solved using dynamic programming by creating a 2D matrix where each cell represents the edit distance between substrings of `str1` and `str2`. The final edit distance is stored in the bottom-right cell of the matrix. The algorithm fills the matrix row by row, using the minimum edit distance from the previous cells to calculate the current cell's value.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDistance(string str1, string str2) {
        int m = str1.size();
        int n = str2.size();
        
        // Create a 2D matrix to store the edit distances
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        // Initialize the base cases
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        
        // Fill the matrix row by row
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // Calculate the cost of substitution
                int cost = (str1[i - 1] == str2[j - 1]) ? 0 : 1;
                
                // Calculate the edit distance for the current cell
                dp[i][j] = min(min(dp[i - 1][j] + 1,      // Deletion
                                    dp[i][j - 1] + 1),      // Insertion
                                dp[i - 1][j - 1] + cost);  // Substitution
            }
        }
        
        // The final edit distance is stored in the bottom-right cell
        return dp[m][n];
    }
};
```

## Test Cases
```
Input: str1 = "kitten", str2 = "sitting"
Output: 3
Input: str1 = "intention", str2 = "execution"
Output: 5
```

## Key Takeaways
- The edit distance problem can be solved using dynamic programming by creating a 2D matrix.
- The matrix is filled row by row, using the minimum edit distance from the previous cells to calculate the current cell's value.
- The final edit distance is stored in the bottom-right cell of the matrix.