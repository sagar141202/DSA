# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The function should return the minimum window substring of `s` that contains all characters of `t`. If there are multiple such windows, return the first one. Constraints: `1 <= s.length, t.length <= 10^5`, `s` and `t` consist of English letters.

## Approach
The algorithm uses a sliding window approach with two pointers, `left` and `right`, to traverse the string `s`. It maintains a frequency count of characters in `t` and updates the count as the window moves. The window is expanded to the right until all characters of `t` are included, then it is shrunk from the left until a character of `t` is excluded.

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
        int formed = 0;
        
        unordered_map<char, int> windowCounts;
        int left = 0, right = 0;
        int ans = INT_MAX, start = 0, end = 0;
        
        while (right < s.length()) {
            char c = s[right];
            windowCounts[c]++;
            
            if (tCount.count(c) && windowCounts[c] == tCount[c]) formed++;
            
            while (left <= right && formed == required) {
                c = s[left];
                
                if (right - left + 1 < ans) {
                    ans = right - left + 1;
                    start = left;
                    end = right;
                }
                
                windowCounts[c]--;
                if (tCount.count(c) && windowCounts[c] < tCount[c]) formed--;
                left++;
            }
            right++;
        }
        
        return ans == INT_MAX ? "" : s.substr(start, end - start + 1);
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
- Maintain frequency counts of characters in `t` and the current window to determine when all characters of `t` are included.
- Update the minimum window substring whenever a smaller window is found that contains all characters of `t`.