# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. The function should return true if the string can be segmented, otherwise return false. For example, given s = "leetcode" and wordDict = ["leet", "code"], return true because "leetcode" can be segmented into "leet code".

## Approach
The problem can be solved using dynamic programming, where we build up a table of whether each prefix of the string can be segmented into words from the dictionary. We iterate over the string and for each position, we check all substrings ending at that position to see if they are in the dictionary.

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
        
        // Create a dp table to store whether each prefix can be segmented
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true; // empty string can always be segmented
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check all substrings ending at position i
            for (int j = 0; j < i; j++) {
                // If the substring is in the dictionary and the previous prefix can be segmented
                if (dict.count(s.substr(j, i - j)) && dp[j]) {
                    dp[i] = true; // then the current prefix can be segmented
                    break;
                }
            }
        }
        
        return dp[s.size()]; // return whether the entire string can be segmented
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
- Use dynamic programming to build up a table of whether each prefix of the string can be segmented into words from the dictionary.
- Use a set to store the dictionary words for O(1) lookup.
- Iterate over the string and for each position, check all substrings ending at that position to see if they are in the dictionary.