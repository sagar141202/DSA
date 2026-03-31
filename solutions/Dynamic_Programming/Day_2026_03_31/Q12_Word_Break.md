# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The function should return true if s can be segmented, otherwise return false. The same word in the dictionary may be reused multiple times in the segmentation. The input string does not contain any spaces, and all words in the dictionary are unique. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code".

## Approach
The algorithm uses dynamic programming to solve the problem by checking all possible substrings of the input string against the dictionary words. It maintains a boolean array where each index represents whether the substring up to that point can be segmented into dictionary words. The algorithm iterates through the string and checks all substrings ending at the current position.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool wordBreak(string s, vector<string>& wordDict) {
    // Create a set for O(1) lookup of dictionary words
    unordered_set<string> dict(wordDict.begin(), wordDict.end());
    
    // Initialize a boolean array to track segmentable substrings
    vector<bool> dp(s.size() + 1, false);
    dp[0] = true;  // Empty string can always be segmented
    
    // Iterate through the string
    for (int i = 1; i <= s.size(); i++) {
        // Check all substrings ending at the current position
        for (int j = 0; j < i; j++) {
            // If the substring from j to i is in the dictionary and the substring before j is segmentable
            if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                // Mark the current substring as segmentable
                dp[i] = true;
                break;
            }
        }
    }
    
    // Return whether the entire string can be segmented
    return dp[s.size()];
}

int main() {
    string s = "leetcode";
    vector<string> wordDict = {"leet", "code"};
    cout << wordBreak(s, wordDict) << endl;
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
- Dynamic programming is used to efficiently solve the problem by avoiding redundant computations.
- The use of a set for dictionary words allows for O(1) lookup, improving the overall time complexity.
- The solution has a time complexity of O(n^2) due to the nested loop structure, where n is the length of the input string.