# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `str1` and `str2`, find the edit distance between them. The strings only contain lowercase English letters. The length of `str1` is `m` and the length of `str2` is `n`, where `1 <= m, n <= 100`. For example, the edit distance between "kitten" and "sitting" is 3 (replace 'k' with 's', replace 'e' with 'i', append 'g').

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell represents the edit distance between substrings of `str1` and `str2`. The final edit distance is stored in the bottom-right cell of the table. The edit distance is calculated by considering the minimum cost of inserting, deleting, or substituting a character.

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
    
    // Create a table to store the results of subproblems
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
            // If the current characters match, there's no operation needed
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                // Otherwise, consider the minimum cost of inserting, deleting, or substituting
                dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]));
            }
        }
    }
    
    // The edit distance is stored in the bottom-right cell of the table
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
- The edit distance problem can be solved using dynamic programming by building a 2D table to store the results of subproblems.
- The time complexity of the solution is O(m*n), where m and n are the lengths of the input strings.
- The space complexity of the solution is O(m*n) due to the extra space required for the 2D table.