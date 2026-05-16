# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. The string s will only contain lowercase English letters, and the dictionary words will also only contain lowercase English letters. For example, given s = "leetcode" and wordDict = ["leet", "code"], return true because "leetcode" can be segmented into "leet code". However, given s = "applepenapple" and wordDict = ["apple", "pen"], return true because "applepenapple" can be segmented into "apple pen apple". If the string cannot be segmented, return false.

## Approach
The problem can be solved using dynamic programming by maintaining a boolean array where each index represents whether the substring up to that point can be segmented into dictionary words. The algorithm iterates over the string, checking all possible substrings to see if they match any word in the dictionary.

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
        // Create a set for faster lookup of dictionary words
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Initialize a boolean array to store whether each substring can be segmented
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;  // The empty string can always be segmented
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check all possible substrings
            for (int j = 0; j < i; j++) {
                // If the substring from j to i is in the dictionary and the substring before j can be segmented
                if (dict.find(s.substr(j, i - j)) != dict.end() && dp[j]) {
                    dp[i] = true;  // Then the substring up to i can be segmented
                    break;
                }
            }
        }
        
        return dp[s.size()];  // Return whether the entire string can be segmented
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
- Dynamic programming can be used to solve problems that have overlapping subproblems and optimal substructure.
- The use of a set for dictionary words allows for faster lookup times.
- The boolean array dp is used to store the results of subproblems to avoid redundant computation.