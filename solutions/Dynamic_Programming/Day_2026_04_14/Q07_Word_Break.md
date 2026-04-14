# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. The function should return true if the string can be segmented, otherwise return false. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code".

## Approach
The problem can be solved using dynamic programming by creating a boolean array where each index represents whether the substring up to that point can be segmented into words from the dictionary. The algorithm iterates over the string, checking all possible substrings to see if they match any word in the dictionary.

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
        dp[0] = true;  // Empty string can always be segmented
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check all possible substrings
            for (int j = 0; j < i; j++) {
                // If the substring can be segmented and the remaining part is in the dictionary, update dp[i]
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
- Use dynamic programming to store the segmentation status of substrings to avoid redundant computation.
- Utilize a set data structure for efficient lookup of words in the dictionary.
- Initialize the dynamic programming array with a base case (empty string can always be segmented) and build up the solution iteratively.