# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The function should return true if s can be segmented and false otherwise. The same word in the dictionary may be reused multiple times in the segmentation. The input string s will only contain lowercase English letters, and the dictionary words will also only contain lowercase English letters.

## Approach
The problem can be solved using dynamic programming, where we build a table to store whether each prefix of the string can be segmented into words from the dictionary. We start by initializing a boolean array dp of size s.length() + 1, where dp[i] is true if the substring s[0..i) can be segmented.

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
        
        // Initialize dp array
        vector<bool> dp(s.length() + 1, false);
        dp[0] = true;
        
        // Fill dp array
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.find(s.substr(j, i - j)) != wordSet.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[s.length()];
    }
};

int main() {
    Solution solution;
    string s = "leetcode";
    vector<string> wordDict = {"leet", "code"};
    cout << solution.wordBreak(s, wordDict) << endl;
    return 0;
}
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
- Use dynamic programming to solve the word break problem efficiently.
- Create a set of words for efficient lookup.
- Initialize a boolean array dp to store whether each prefix of the string can be segmented into words from the dictionary.