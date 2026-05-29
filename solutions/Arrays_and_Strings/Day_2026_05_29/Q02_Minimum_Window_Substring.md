# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The constraints are: `1 <= s.length, t.length <= 10^5`, and `s` and `t` consist of lowercase English letters.

## Approach
This problem can be solved using the sliding window technique with the help of two frequency maps to track the characters in `s` and `t`. We maintain a window in `s` and try to minimize it while ensuring it contains all characters of `t`. The algorithm uses two pointers to represent the window.

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
        for (char c : t) tCount[c]++;
        
        int required = tCount.size();
        unordered_map<char, int> windowCounts;
        int formed = 0;
        
        int windowStart = 0, minLength = INT_MAX, minWindow = "";
        
        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            char rightChar = s[windowEnd];
            windowCounts[rightChar]++;
            
            if (tCount.find(rightChar) != tCount.end() && windowCounts[rightChar] == tCount[rightChar]) {
                formed++;
            }
            
            while (windowStart <= windowEnd && formed == required) {
                char leftChar = s[windowStart];
                
                if (windowEnd - windowStart + 1 < minLength) {
                    minLength = windowEnd - windowStart + 1;
                    minWindow = s.substr(windowStart, windowEnd - windowStart + 1);
                }
                
                windowCounts[leftChar]--;
                if (tCount.find(leftChar) != tCount.end() && windowCounts[leftChar] < tCount[leftChar]) {
                    formed--;
                }
                
                windowStart++;
            }
        }
        
        return minWindow;
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
- Use the sliding window technique to solve string problems involving substrings.
- Utilize frequency maps (unordered_map in C++) to efficiently track character counts.
- Maintain a window with two pointers and adjust it based on the conditions of the problem.