# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window substring in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` with their respective frequencies. For example, if `t = "abc"`, the window must contain at least one `a`, one `b`, and one `c`. The constraints are `1 <= s.length, t.length <= 10^5` and `s` and `t` consist of lowercase English letters.

## Approach
The approach is to use a sliding window technique to find the minimum window that contains all characters of `t`. We maintain two pointers, `left` and `right`, to represent the current window. We also use a hashmap to store the frequency of characters in `t` and another hashmap to store the frequency of characters in the current window.

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
        if (t.length() > s.length()) return "";
        
        // Create a hashmap to store the frequency of characters in t
        unordered_map<char, int> tCount;
        for (char c : t) {
            tCount[c]++;
        }
        
        int required = tCount.size();
        int left = 0, right = 0;
        int formed = 0;
        
        // Create a hashmap to store the frequency of characters in the current window
        unordered_map<char, int> windowCounts;
        int ans = INT_MAX;
        int ansLeft = 0, ansRight = 0;
        
        while (right < s.length()) {
            char c = s[right];
            windowCounts[c]++;
            
            // If the frequency of the current character in the window is equal to the frequency in t,
            // increment the formed count
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formed++;
            }
            
            while (left <= right && formed == required) {
                c = s[left];
                
                // If the length of the current window is less than the minimum length found so far,
                // update the minimum length and the corresponding window
                if (right - left + 1 < ans) {
                    ans = right - left + 1;
                    ansLeft = left;
                    ansRight = right;
                }
                
                // If the frequency of the character at the left of the window is greater than the frequency in t,
                // decrement the formed count
                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }
                
                left++;
            }
            
            right++;
        }
        
        return ans == INT_MAX ? "" : s.substr(ansLeft, ansRight - ansLeft + 1);
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
- Maintain two hashmaps to store the frequency of characters in `t` and the current window.
- Update the minimum length and the corresponding window when a smaller window is found.