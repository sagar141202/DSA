# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. The function should return true if the string can be segmented, otherwise return false. The input string does not contain any spaces, and the dictionary words do not contain any spaces. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code".

## Approach
The Word Break problem can be solved using dynamic programming, where we create a boolean array to track whether each substring can be segmented into dictionary words. We then fill up this array by checking all possible substrings. The algorithm iterates over the string, checking for each position if any word in the dictionary matches the substring ending at that position.

## Complexity
- Time: O(n^2 + m) where n is the length of the string and m is the total length of all words in the dictionary
- Space: O(n) where n is the length of the string

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool wordBreak(string s, vector<string>& wordDict) {
    // Create a set of words for efficient lookup
    unordered_set<string> dict(wordDict.begin(), wordDict.end());
    
    // Create a boolean array to track whether each substring can be segmented
    vector<bool> dp(s.size() + 1, false);
    dp[0] = true;
    
    // Fill up the dp array
    for (int i = 1; i <= s.size(); i++) {
        for (int j = 0; j < i; j++) {
            // Check if the substring can be segmented
            if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                dp[i] = true;
                break;
            }
        }
    }
    
    // Return the result for the entire string
    return dp[s.size()];
}

int main() {
    string s = "leetcode";
    vector<string> wordDict = {"leet", "code"};
    cout << boolalpha << wordBreak(s, wordDict) << endl;
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
- The Word Break problem can be efficiently solved using dynamic programming.
- Creating a set of dictionary words allows for efficient lookup.
- The dynamic programming approach avoids redundant computation by storing the results of subproblems in the dp array.