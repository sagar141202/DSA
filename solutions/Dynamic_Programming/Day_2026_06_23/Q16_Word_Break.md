# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The function should return true if s can be segmented and false otherwise. The same word in the dictionary may be reused multiple times in the segmentation. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code".

## Approach
The problem can be solved using dynamic programming by maintaining a boolean array where each index represents whether the substring up to that point can be segmented into words from the dictionary. We iterate over the string and for each position, we check all substrings ending at that position to see if they are in the dictionary.

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
        // Create a set for O(1) lookup of words in the dictionary
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Create a boolean array to store whether each substring can be segmented
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;  // Empty string can always be segmented
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // For each position, check all substrings ending at that position
            for (int j = 0; j < i; j++) {
                // If the substring from j to i is in the dictionary and the substring before j can be segmented
                if (dict.find(s.substr(j, i - j)) != dict.end() && dp[j]) {
                    // Then the substring up to i can be segmented
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
- Dynamic programming can be used to solve problems that have overlapping subproblems, such as the word break problem.
- Using a set for the dictionary allows for O(1) lookup of words.
- The boolean array dp is used to store whether each substring can be segmented, and is updated based on whether the current substring is in the dictionary and the previous substring can be segmented.