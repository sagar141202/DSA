# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The function should return true if the string can be segmented and false otherwise. The same word in the dictionary may be reused multiple times in the segmentation. The input string does not contain any spaces. The dictionary words do not contain any spaces. 1 <= s.length <= 300, 1 <= wordDict.length <= 5000, 1 <= wordDict[i].length <= 20.

## Approach
The problem can be solved using dynamic programming, where a boolean array dp is used to track whether each substring can be segmented into words from the dictionary. The algorithm iterates over the string, checking all possible substrings to see if they match any word in the dictionary. If a match is found, the dp array is updated accordingly.

## Complexity
- Time: O(n^2 * m) where n is the length of the string and m is the average length of words in the dictionary
- Space: O(n) where n is the length of the string

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // Create a set for O(1) lookup time
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        // Create a dp array to track whether each substring can be segmented
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // Check all possible substrings
            for (int j = 0; j < i; j++) {
                // If the substring can be segmented and the remaining part is in the dictionary, update dp
                if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
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
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

## Key Takeaways
- The use of dynamic programming to track the segmentability of substrings.
- The importance of using a set for O(1) lookup time when checking if a word is in the dictionary.
- The need to iterate over all possible substrings to ensure that the solution is correct.