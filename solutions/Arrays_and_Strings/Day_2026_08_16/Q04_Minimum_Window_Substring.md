# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The input strings `s` and `t` contain only lowercase English letters. The length of `s` is between 1 and 10^5, and the length of `t` is between 1 and 100.

## Approach
The algorithm uses a sliding window approach to find the minimum window in `s` that contains all characters of `t`. It maintains a frequency count of characters in `t` and updates the count as the window moves. The minimum window is updated whenever a smaller window is found that contains all characters of `t`.

## Complexity
- Time: O(|s| + |t|)
- Space: O(|t|)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string minWindow(string s, string t) {
    if (t.size() > s.size()) return "";
    
    unordered_map<char, int> tCount;
    for (char c : t) tCount[c]++;
    
    int required = tCount.size();
    int left = 0, right = 0;
    int formed = 0;
    
    unordered_map<char, int> windowCounts;
    int ans = INT_MAX;
    string ansStr = "";
    
    while (right < s.size()) {
        char c = s[right];
        windowCounts[c]++;
        
        if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) formed++;
        
        while (left <= right && formed == required) {
            c = s[left];
            
            if (right - left + 1 < ans) {
                ans = right - left + 1;
                ansStr = s.substr(left, right - left + 1);
            }
            
            windowCounts[c]--;
            if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) formed--;
            
            left++;
        }
        
        right++;
    }
    
    return ansStr;
}
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
- Use a sliding window approach to find the minimum window in `s` that contains all characters of `t`.
- Maintain a frequency count of characters in `t` and update the count as the window moves.
- Update the minimum window whenever a smaller window is found that contains all characters of `t`.