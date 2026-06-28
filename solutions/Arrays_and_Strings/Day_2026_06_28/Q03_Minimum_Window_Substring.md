# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If no such window exists, return an empty string. The window must contain all characters of `t` in any order. The constraints are: `1 <= s.length, t.length <= 10^5`, and `s` and `t` consist of lowercase English letters.

## Approach
The algorithm uses a sliding window approach with two pointers to traverse the string `s`. It maintains a frequency count of characters in `t` and updates the window boundaries based on the count. The minimum window is updated whenever a smaller window is found that contains all characters of `t`.

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
        for (char c : t) tCount[c]++;
        
        int required = tCount.size();
        int left = 0, right = 0;
        int formed = 0;
        
        unordered_map<char, int> windowCounts;
        int minLen = INT_MAX;
        int minStart = 0, minEnd = 0;
        
        while (right < s.length()) {
            char c = s[right];
            windowCounts[c]++;
            
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formed++;
            }
            
            while (left <= right && formed == required) {
                c = s[left];
                
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minStart = left;
                    minEnd = right;
                }
                
                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }
                
                left++;
            }
            
            right++;
        }
        
        return minLen == INT_MAX ? "" : s.substr(minStart, minEnd - minStart + 1);
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
- Use a sliding window approach to efficiently scan the string `s`.
- Maintain a frequency count of characters in `t` to track the required characters.
- Update the window boundaries based on the formed characters to find the minimum window.