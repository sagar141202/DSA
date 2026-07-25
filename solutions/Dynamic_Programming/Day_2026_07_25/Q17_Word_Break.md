# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. The function should return true if the string can be segmented, otherwise return false. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code".

## Approach
The solution uses dynamic programming to build up a table where each entry represents whether the substring up to that point can be segmented into words from the dictionary. The algorithm iterates over the string, checking all possible substrings to see if they match any word in the dictionary.

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
        // Create a set of words for O(1) lookup
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Create a dp table to store segmentation results
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check all substrings ending at i
            for (int j = 0; j < i; j++) {
                // If the substring can be segmented and the remaining part is in the dictionary, update dp[i]
                if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        // Return the segmentation result for the entire string
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
- Use dynamic programming to solve problems that have overlapping subproblems and optimal substructure.
- Use a set or hash table to store the dictionary for efficient lookup.
- Build up the dp table iteratively, using previously computed results to avoid redundant computation.