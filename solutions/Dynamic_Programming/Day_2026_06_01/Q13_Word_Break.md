# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. The function should return true if the string can be segmented, otherwise false. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code".

## Approach
The problem can be solved using dynamic programming by creating a boolean array where each index represents whether the substring up to that point can be segmented into words from the dictionary. We iterate over the string and for each substring, we check if it can be formed using the words in the dictionary.

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
        // Create a set for O(1) lookup
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Create a dp array to store the segmentation status
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true; // empty string can always be segmented
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check all substrings ending at i
            for (int j = 0; j < i; j++) {
                // If the substring can be segmented and the remaining part is in the dictionary
                if (dp[j] && dict.count(s.substr(j, i - j))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[s.size()];
    }
};

## Test Cases
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

## Key Takeaways
- Dynamic programming can be used to solve problems with overlapping subproblems.
- Creating a set for O(1) lookup can improve the efficiency of the solution.
- Breaking down the problem into smaller subproblems and solving them can lead to an efficient solution.