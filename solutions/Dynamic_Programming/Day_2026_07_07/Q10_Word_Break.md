# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. For example, given s = "leetcode" and wordDict = ["leet", "code"], return true because "leetcode" can be segmented into "leet code". However, given s = "applepenapple" and wordDict = ["apple", "pen"], return true because "applepenapple" can be segmented into "apple pen apple". If the string cannot be segmented, return false.

## Approach
The algorithm uses dynamic programming to solve the problem by breaking down the string into smaller sub-problems and storing the results in a table. It checks if each sub-string can be segmented into words from the dictionary. The approach iterates over the string, checking all possible segmentations.

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
        // Create a set for faster lookup
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Create a dp table to store the results of sub-problems
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;  // Base case: empty string can be segmented
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check all possible segmentations
            for (int j = 0; j < i; j++) {
                // If the sub-string can be segmented and the remaining part is in the dictionary, update dp[i]
                if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        // Return the result for the entire string
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
- Use dynamic programming to break down the problem into smaller sub-problems and store the results in a table.
- Use a set for faster lookup of words in the dictionary.
- Iterate over the string, checking all possible segmentations, and update the dp table accordingly.