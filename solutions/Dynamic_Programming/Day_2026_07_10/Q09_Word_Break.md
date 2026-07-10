# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. For example, given s = "leetcode" and wordDict = ["leet", "code"], return true because "leetcode" can be segmented into "leet code". However, given s = "applepenapple" and wordDict = ["apple", "pen"], return true because "applepenapple" can be segmented into "apple pen apple". The function should return true if the string can be segmented and false otherwise.

## Approach
The approach to solve this problem is to use dynamic programming, where we create a boolean array dp of size n+1, where n is the length of the string s. We then iterate over the string and for each substring, we check if it is present in the wordDict. If it is, we update the dp array accordingly.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool wordBreak(string s, vector<string>& wordDict) {
    unordered_set<string> dict(wordDict.begin(), wordDict.end());
    int n = s.size();
    vector<bool> dp(n + 1, false);
    dp[0] = true;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}
```

## Test Cases
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

## Key Takeaways
- We use a dynamic programming approach to solve this problem efficiently.
- We create a boolean array dp to store the segmentation status of each substring.
- We use an unordered_set to store the words in the wordDict for efficient lookup.