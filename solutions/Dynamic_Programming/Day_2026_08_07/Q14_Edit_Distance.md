# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into another. Given two strings `str1` and `str2` with lengths `m` and `n` respectively, find the edit distance between them. The allowed operations are: 
- Insertion: Insert a character into `str1`.
- Deletion: Delete a character from `str1`.
- Substitution: Replace a character in `str1` with a character from `str2`.
For example, the edit distance between "kitten" and "sitting" is 3 (substitute 'k' with 's', substitute 'e' with 'i', append 'g').

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the edit distances between substrings of `str1` and `str2`. The edit distance is calculated by considering the minimum cost of insertion, deletion, and substitution at each step.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int editDistance(string str1, string str2) {
    int m = str1.length();
    int n = str2.length();

    // Create a 2D table to store the edit distances
    int dp[m + 1][n + 1];

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
            // If the current characters match, no operation is needed
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                // Otherwise, consider the minimum cost of insertion, deletion, and substitution
                dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
            }
        }
    }

    // The edit distance is stored in the bottom-right corner of the table
    return dp[m][n];
}

int main() {
    string str1 = "kitten";
    string str2 = "sitting";
    cout << "Edit Distance: " << editDistance(str1, str2) << endl;
    return 0;
}
```

## Test Cases
```
Input: str1 = "kitten", str2 = "sitting"
Output: 3
Input: str1 = "hello", str2 = "world"
Output: 4
```

## Key Takeaways
- The edit distance problem can be solved using dynamic programming by creating a 2D table to store the edit distances between substrings.
- The time complexity of the solution is O(m*n), where m and n are the lengths of the input strings.
- The space complexity of the solution is O(m*n), which is used to store the 2D table.