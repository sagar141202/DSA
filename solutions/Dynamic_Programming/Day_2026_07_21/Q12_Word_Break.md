# Word Break

## Problem Statement
Given a non-empty string `s` and a dictionary `wordDict` containing a list of non-empty words, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words. The function should return `true` if `s` can be segmented, otherwise it returns `false`. For example, given `s = "leetcode"` and `wordDict = ["leet", "code"]`, the function should return `true` because `"leetcode"` can be segmented into `"leet code"`. The input string `s` only contains lowercase English letters, and the dictionary `wordDict` contains only unique words.

## Approach
The Word Break problem can be solved using dynamic programming, where we build up a solution by checking if each prefix of the string can be segmented into dictionary words. We use a boolean array `dp` to store whether each prefix can be segmented. The algorithm iterates over the string, checking if any word in the dictionary is a suffix of the current prefix.

## Complexity
- Time: O(n^2 + m) where n is the length of the string `s` and m is the total length of all words in `wordDict`
- Space: O(n) for the `dp` array

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // Create a set for O(1) lookup of words in the dictionary
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Create a dp array to store whether each prefix can be segmented
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true; // Empty string can always be segmented
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check if any word in the dictionary is a suffix of the current prefix
            for (int j = 0; j < i; j++) {
                if (dp[j] && dict.count(s.substr(j, i - j))) {
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
- Use dynamic programming to solve the Word Break problem by checking if each prefix of the string can be segmented into dictionary words.
- Use a boolean array `dp` to store whether each prefix can be segmented.
- Use an unordered set for O(1) lookup of words in the dictionary.