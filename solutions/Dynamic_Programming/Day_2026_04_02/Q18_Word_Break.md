# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. The function should return true if s can be segmented, otherwise return false. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code". 

## Approach
The problem can be solved using dynamic programming by creating a boolean array where each index represents whether the substring up to that point can be segmented into words from the dictionary. We initialize the first element of the array to true and then iterate over the string, checking all substrings that end at the current position to see if they can be formed from the dictionary.

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
        // Create a set of words for efficient lookup
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Create a boolean array to store whether each substring can be segmented
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check all substrings that end at the current position
            for (int j = 0; j < i; j++) {
                // If the substring from j to i can be formed from the dictionary and the substring before j can be segmented, update dp[i]
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
- The problem can be solved using dynamic programming by storing whether each substring can be segmented into words from the dictionary.
- We use a set to store the dictionary words for efficient lookup.
- The time complexity is O(n^2) due to the nested loops, where n is the length of the input string.