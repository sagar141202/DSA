# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The function should return true if s can be segmented and false otherwise. The same word in the dictionary may be reused multiple times in the segmentation. The dictionary does not contain duplicates and all words are lowercase. 1 <= s.length <= 300, 1 <= wordDict.length <= 5000, 1 <= wordDict[i].length <= 20.

## Approach
The problem can be solved using dynamic programming by maintaining a boolean array where each index represents whether the substring up to that index can be segmented into words from the dictionary. We iterate over the string and for each substring, we check if it can be formed using words from the dictionary.

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
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        
        // Initialize a boolean array to store whether each substring can be segmented
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;  // Empty string can always be segmented
        
        // Iterate over the string
        for (int i = 1; i <= s.size(); i++) {
            // For each substring, check if it can be formed using words from the dictionary
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.find(s.substr(j, i - j)) != wordSet.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
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
- The problem can be solved using dynamic programming by maintaining a boolean array to store whether each substring can be segmented into words from the dictionary.
- The time complexity of the solution is O(n^2) due to the nested loop structure.
- The space complexity of the solution is O(n) for storing the boolean array and the set of words.