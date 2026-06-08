# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. For example, given s = "leetcode" and wordDict = ["leet", "code"], return true because "leetcode" can be segmented into "leet code". However, given s = "applepenapple" and wordDict = ["apple", "pen"], return true because "applepenapple" can be segmented into "apple pen apple". On the other hand, given s = "catsandog" and wordDict = ["cats", "dog", "sand", "and", "cat"], return false because "catsandog" cannot be segmented into words from the dictionary.

## Approach
The algorithm uses dynamic programming to solve the word break problem. It initializes a boolean array dp where dp[i] is true if the string s can be segmented into words from the dictionary up to index i. It then iterates over the string and checks if any word in the dictionary is a prefix of the substring s[j..i]. If it is, it updates dp[i] accordingly.

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
        
        // Initialize a boolean array dp where dp[i] is true if the string s can be segmented into words from the dictionary up to index i
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Iterate over the substring s[j..i]
            for (int j = 0; j < i; j++) {
                // If dp[j] is true and the substring s[j..i] is in the dictionary, update dp[i] accordingly
                if (dp[j] && dict.count(s.substr(j, i - j))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        // Return the result
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
- The word break problem can be solved using dynamic programming.
- The algorithm uses a boolean array dp to keep track of whether the string can be segmented into words from the dictionary up to each index.
- The algorithm iterates over the string and checks if any word in the dictionary is a prefix of the substring s[j..i].