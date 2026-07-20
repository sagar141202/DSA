# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `str1` and `str2`, find the edit distance between them. The strings only contain lowercase English letters. The length of `str1` is `m` and the length of `str2` is `n`, where `1 <= m, n <= 1000`.

## Approach
The edit distance problem can be solved using dynamic programming by creating a 2D table to store the edit distances between substrings of `str1` and `str2`. We fill the table in a bottom-up manner, considering all possible operations (insertion, deletion, substitution) at each step. The final edit distance is stored in the last cell of the table.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int editDistance(string str1, string str2, int m, int n) {
    // Create a 2D table to store the edit distances
    int dp[m + 1][n + 1];

    // Initialize the base cases
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0)
                dp[i][j] = j;  // Edit distance is j if str1 is empty
            else if (j == 0)
                dp[i][j] = i;  // Edit distance is i if str2 is empty
            else if (str1[i - 1] == str2[j - 1])
                dp[i][j] = dp[i - 1][j - 1];  // No operation needed if characters match
            else
                dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
        }
    }

    return dp[m][n];
}

int main() {
    string str1 = "kitten";
    string str2 = "sitting";
    int m = str1.length();
    int n = str2.length();

    cout << "Edit Distance: " << editDistance(str1, str2, m, n);

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
- The edit distance problem has an optimal substructure, making it suitable for dynamic programming.
- The time complexity of the solution is O(m*n), where m and n are the lengths of the input strings.
- The space complexity of the solution is also O(m*n) due to the 2D table used to store the edit distances.