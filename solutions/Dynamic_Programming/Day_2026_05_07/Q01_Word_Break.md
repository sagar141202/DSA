# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. For example, given s = "leetcode" and wordDict = ["leet", "code"], return true because "leetcode" can be segmented into "leet code". However, given s = "applepenapple" and wordDict = ["apple", "pen"], return true because "applepenapple" can be segmented into "apple pen apple". If s cannot be segmented into a sequence of words from wordDict, return false.

## Approach
The algorithm uses dynamic programming to solve the word break problem by checking all possible substrings of the input string against the dictionary words. It maintains a boolean array where each index represents whether the substring up to that point can be segmented into dictionary words. The final result is stored in the last index of the array.

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
        // Create a set for efficient lookup of dictionary words
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Create a boolean array to store whether each substring can be segmented
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;  // The empty string can always be segmented
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check all substrings ending at the current position
            for (int j = 0; j < i; j++) {
                // If the substring from j to i is in the dictionary and the substring before j can be segmented
                if (dict.find(s.substr(j, i - j)) != dict.end() && dp[j]) {
                    dp[i] = true;  // Mark the current substring as segmentable
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
- The dynamic programming approach allows for efficient solution by avoiding redundant computation.
- Using a set for dictionary words enables fast lookup.
- The boolean array dp stores the segmentability status of each substring, making it easy to determine the final result.