# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. The function should return true if the string can be segmented, otherwise return false. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code".

## Approach
The problem can be solved using dynamic programming by maintaining a boolean array where each index represents whether the substring up to that point can be segmented. We iterate through the string and for each position, we check all substrings ending at that position to see if they can be formed from the dictionary words.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool wordBreak(string s, vector<string>& wordDict) {
    // Create a set of words for faster lookup
    unordered_set<string> dict(wordDict.begin(), wordDict.end());
    
    // Initialize a boolean array to store whether each substring can be segmented
    vector<bool> dp(s.size() + 1, false);
    dp[0] = true;  // Empty string can always be segmented
    
    // Iterate through the string
    for (int i = 1; i <= s.size(); i++) {
        // Check all substrings ending at the current position
        for (int j = 0; j < i; j++) {
            // If the substring can be segmented and the remaining part is in the dictionary, update dp[i]
            if (dp[j] && dict.count(s.substr(j, i - j))) {
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
- The dynamic programming approach allows for efficient computation of whether each substring can be segmented.
- Using an unordered set for the dictionary provides fast lookup times.
- The solution has a time complexity of O(n^2) due to the nested loop structure, where n is the length of the input string.