# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The characters in `t` can be repeated in the window. If there are multiple minimum windows, return the first one. Constraints: `1 <= s.length, t.length <= 10^5`, `s` and `t` consist of lowercase English letters.

## Approach
Use a sliding window approach with two pointers to track the minimum window in `s` that contains all characters of `t`. Utilize a hashmap to store the frequency of characters in `t` and another hashmap to store the frequency of characters in the current window.

## Complexity
- Time: O(|s| + |t|)
- Space: O(|s| + |t|)

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
        int l = 0, r = 0;
        int formed = 0;
        
        unordered_map<char, int> windowCounts;
        int ans = INT_MAX;
        string ansStr = "";
        
        while (r < s.length()) {
            char c = s[r];
            windowCounts[c]++;
            
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formed++;
            }
            
            while (l <= r && formed == required) {
                c = s[l];
                if (r - l + 1 < ans) {
                    ans = r - l + 1;
                    ansStr = s.substr(l, r - l + 1);
                }
                
                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }
                
                l++;
            }
            
            r++;
        }
        
        return ansStr;
    }
};

```

## Test Cases
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Input: s = "a", t = "a"
Output: "a"
Input: s = "a", t = "aa"
Output: ""
```

## Key Takeaways
- The sliding window approach can be used to solve this problem efficiently.
- Utilizing hashmaps to store character frequencies is essential for tracking the minimum window.
- The `formed` variable helps track when all characters in `t` are present in the current window.