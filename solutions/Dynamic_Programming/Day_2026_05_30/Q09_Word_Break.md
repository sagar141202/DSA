# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. The function should return true if s can be segmented, otherwise return false. For example, given s = "leetcode" and wordDict = ["leet", "code"], return true because "leetcode" can be segmented into "leet code". However, given s = "applepenapple" and wordDict = ["apple", "pen"], return true because "applepenapple" can be segmented into "apple pen apple". On the other hand, given s = "catsandog" and wordDict = ["cats", "dog", "sand", "and", "cat"], return false.

## Approach
The solution uses dynamic programming to solve the problem by checking all possible substrings of the input string and determining if they can be segmented into dictionary words. The algorithm iterates over the string, and for each substring, it checks if the substring can be segmented by looking up the remaining part of the substring in the dictionary. If the remaining part can be segmented, then the current substring can also be segmented.

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
        
        // Create a dp array to store the segmentation status of each substring
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check all substrings ending at i
            for (int j = 0; j < i; j++) {
                // If the substring from j to i is in the dictionary and the substring from 0 to j can be segmented
                if (dict.find(s.substr(j, i - j)) != dict.end() && dp[j]) {
                    // Then the substring from 0 to i can be segmented
                    dp[i] = true;
                    break;
                }
            }
        }
        
        // Return the segmentation status of the entire string
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
- Use dynamic programming to solve the problem by checking all possible substrings of the input string.
- Create a set for O(1) lookup of dictionary words.
- Use a dp array to store the segmentation status of each substring.