# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The function should return true if s can be segmented and false otherwise. The same word in the dictionary may be reused multiple times in the segmentation. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code". However, given s = "applepenapple" and wordDict = ["apple", "pen"], the function should return true because "applepenapple" can be segmented into "apple pen apple". The function should return false for s = "catsandog" and wordDict = ["cats", "dog", "sand", "and", "cat"] because "catsandog" cannot be segmented into words from the dictionary.

## Approach
The problem can be solved using dynamic programming by creating a boolean array where each index represents whether the substring up to that point can be segmented into words from the dictionary. We iterate over the string and for each substring, we check if it can be formed using words from the dictionary. The algorithm builds up a solution by checking all possible substrings and determining if they can be segmented.

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
        // Create a set for efficient lookups
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Create a boolean array to store the segmentation status of each substring
        vector<bool> dp(s.size() + 1, false);
        
        // The empty string can always be segmented
        dp[0] = true;
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Iterate over all substrings ending at the current position
            for (int j = 0; j < i; j++) {
                // If the substring from j to i can be formed using a word from the dictionary
                // and the substring from 0 to j can be segmented, then the substring from 0 to i can be segmented
                if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        // The result is stored in the last index of the boolean array
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
- The word break problem can be solved using dynamic programming by building up a solution from smaller substrings.
- Using an unordered set for the dictionary provides efficient lookups.
- The problem has a time complexity of O(n^2) due to the nested loops over the string.