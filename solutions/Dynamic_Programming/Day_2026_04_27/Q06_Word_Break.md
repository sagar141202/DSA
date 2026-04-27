# Word Break

## Problem Statement
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation. The function should return true if s can be segmented, otherwise return false. For example, given s = "leetcode" and wordDict = ["leet", "code"], the function should return true because "leetcode" can be segmented into "leet code". However, given s = "applepenapple" and wordDict = ["apple", "pen"], the function should return true because "applepenapple" can be segmented into "apple pen apple". On the other hand, given s = "catsandog" and wordDict = ["cats", "dog", "sand", "and", "cat"], the function should return false.

## Approach
The algorithm uses dynamic programming to solve the problem by maintaining a boolean array dp where dp[i] is true if the substring from index 0 to i can be segmented into words from the dictionary. The algorithm iterates over the string and checks if any substring ending at the current index can be formed from the dictionary words.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool wordBreak(string s, vector<string>& wordDict) {
    // Create a set of words for O(1) lookup
    unordered_set<string> dict(wordDict.begin(), wordDict.end());
    
    // Create a dp array to store the segmentation status of each substring
    vector<bool> dp(s.size() + 1, false);
    dp[0] = true;
    
    // Iterate over the string
    for (int i = 1; i <= s.size(); i++) {
        // Check if any substring ending at the current index can be formed from the dictionary words
        for (int j = 0; j < i; j++) {
            if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                dp[i] = true;
                break;
            }
        }
    }
    
    // Return the segmentation status of the entire string
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
- The word break problem can be solved using dynamic programming with a time complexity of O(n^2) and a space complexity of O(n).
- The algorithm uses a boolean array dp to store the segmentation status of each substring.
- The algorithm iterates over the string and checks if any substring ending at the current index can be formed from the dictionary words.