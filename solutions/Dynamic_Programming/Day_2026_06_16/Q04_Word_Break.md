# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The function should return true if s can be segmented, otherwise return false. The same word in the dictionary may be reused multiple times in the segmentation. The dictionary is not necessarily sorted, and there may be duplicates. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code".

## Approach
The problem can be solved using dynamic programming, where we create a boolean array to store whether each substring can be segmented into dictionary words. We iterate over the string, checking if any substring can be formed using dictionary words. If a substring can be formed, we update the boolean array accordingly.

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
        // Create a set of dictionary words for efficient lookup
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Create a boolean array to store whether each substring can be segmented
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check if any substring can be formed using dictionary words
            for (int j = 0; j < i; j++) {
                if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        // Return whether the entire string can be segmented
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
- Create a boolean array to store whether each substring can be segmented into dictionary words.
- Iterate over the string, checking if any substring can be formed using dictionary words.