# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. For example, given s = "leetcode" and wordDict = ["leet", "code"], return true because "leetcode" can be segmented into "leet code". However, given s = "applepenapple" and wordDict = ["apple", "pen"], return true because "applepenapple" can be segmented into "apple pen apple". The constraints are 1 <= s.length <= 300 and 1 <= wordDict.length <= 1000.

## Approach
The algorithm uses dynamic programming to build a table where each entry represents whether the substring up to that point can be segmented into dictionary words. We start by initializing the table with false values, then we iterate over the string and update the table based on whether the current substring can be formed using the dictionary words. The time complexity of this approach is linear with respect to the length of the string.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // Create a set for wordDict to allow O(1) lookup
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Initialize the dp table
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        
        // Fill up the dp table
        for (int i = 1; i <= s.size(); i++) {
            for (int j = 0; j < i; j++) {
                // If the substring from j to i can be formed using the dictionary words
                if (dp[j] && dict.count(s.substr(j, i - j))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        // Return the last entry in the dp table
        return dp[s.size()];
    }
};
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
- Use dynamic programming to solve problems that have overlapping subproblems.
- Use a set to store the dictionary words for O(1) lookup.
- The dp table should be initialized with false values, and the base case should be set to true.