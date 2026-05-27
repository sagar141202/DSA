# Word Break

## Problem Statement
Given a non-empty string `s` and a dictionary `wordDict` containing a list of non-empty words, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. Constraints: `1 <= s.length <= 300`, `1 <= wordDict.length <= 1000`, `1 <= wordDict[i].length <= 20`, `s` and `wordDict[i]` consist of lowercase English letters. Example: `s = "leetcode", wordDict = ["leet","code"]`, Output: `true`.

## Approach
This problem can be solved using Dynamic Programming by creating a boolean array `dp` where `dp[i]` is `true` if the string `s[0...i]` can be segmented into words from the dictionary. We iterate over the string and for each position, we check all substrings ending at that position to see if they are in the dictionary.

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
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        for (int i = 1; i <= s.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.size()];
    }
};

int main() {
    Solution solution;
    string s = "leetcode";
    vector<string> wordDict = {"leet", "code"};
    cout << boolalpha << solution.wordBreak(s, wordDict) << endl;
    return 0;
}
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
- Use dynamic programming to solve problems that have overlapping subproblems.
- The `dp` array can be used to store the results of subproblems to avoid redundant computation.
- The `unordered_set` data structure can be used to store the dictionary words for efficient lookup.