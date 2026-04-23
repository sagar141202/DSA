# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The function should return the minimum window substring of `s` that contains all characters of `t`. If there are multiple such windows, return the first one. Constraints: `1 <= s.length, t.length <= 10^5`, `s` and `t` consist of lowercase English letters.

## Approach
We use a sliding window approach with two pointers to find the minimum window substring. We maintain a frequency count of characters in `t` and a count of characters in the current window that match characters in `t`. When the count of matching characters equals the number of unique characters in `t`, we have found a valid window.

## Complexity
- Time: O(|s| + |t|)
- Space: O(|t|)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (s.length() < t.length()) return "";
        
        unordered_map<char, int> tCount;
        for (char c : t) {
            tCount[c]++;
        }
        
        int required = tCount.size();
        int formed = 0;
        
        unordered_map<char, int> windowCounts;
        int ans = INT_MAX;
        int start = 0;
        string result = "";
        
        for (int end = 0; end < s.length(); end++) {
            char c = s[end];
            windowCounts[c]++;
            
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formed++;
            }
            
            while (formed == required && start <= end) {
                if (end - start + 1 < ans) {
                    ans = end - start + 1;
                    result = s.substr(start, end - start + 1);
                }
                
                char startChar = s[start];
                windowCounts[startChar]--;
                
                if (tCount.find(startChar) != tCount.end() && windowCounts[startChar] < tCount[startChar]) {
                    formed--;
                }
                
                start++;
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Input: s = "a", t = "a"
Output: "a"
Input: s = "aa", t = "aa"
Output: "aa"
```

## Key Takeaways
- Use a sliding window approach to find the minimum window substring that contains all characters of `t`.
- Maintain a frequency count of characters in `t` and a count of characters in the current window that match characters in `t`.
- Return the first minimum window substring found, or an empty string if no such window exists.