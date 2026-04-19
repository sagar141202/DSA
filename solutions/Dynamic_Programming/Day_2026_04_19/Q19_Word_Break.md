# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. The function should return true if the string can be segmented, otherwise return false. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code".

## Approach
The algorithm uses dynamic programming to solve the problem by maintaining a boolean array where each index represents whether the substring up to that point can be segmented into words from the dictionary. The function iterates over the string, checking all possible substrings to see if they match any word in the dictionary.

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
        
        // Create a boolean array to store the segmentation status
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check all possible substrings
            for (int j = 0; j < i; j++) {
                // If the substring matches a word in the dictionary and the previous substring can be segmented
                if (dp[j] && dict.count(s.substr(j, i - j))) {
                    // Mark the current substring as segmentable
                    dp[i] = true;
                    break;
                }
            }
        }
        
        // Return the segmentation status of the entire string
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
- Use dynamic programming to solve the problem by maintaining a boolean array to store the segmentation status.
- Use a set to store the dictionary words for O(1) lookup.
- Iterate over the string and check all possible substrings to see if they match any word in the dictionary.