# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The function should return the minimum window substring of `s` that contains all characters of `t`. If there are multiple such windows, return the first one. For example, given `s = "ADOBECODEBANC"` and `t = "ABC"`, the minimum window is `"BANC"`.

## Approach
The algorithm uses a sliding window approach with two pointers to track the minimum window in `s` that contains all characters of `t`. It maintains a frequency count of characters in `t` and updates it as the window moves. The window expands to the right until all characters of `t` are included, and then contracts from the left until a character of `t` is excluded.

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
        // Base case: if string t is longer than string s
        if (t.size() > s.size()) return "";

        // Create a frequency map for string t
        unordered_map<char, int> tCount;
        for (char c : t) tCount[c]++;

        // Initialize variables
        int required = tCount.size();
        int left = 0, right = 0;
        int formed = 0;

        // Create a frequency map for the current window
        unordered_map<char, int> windowCounts;

        // Initialize the minimum window
        int minLen = INT_MAX;
        int minStart = 0;

        // Expand the window to the right
        while (right < s.size()) {
            char c = s[right];
            windowCounts[c]++;

            // If the character is in tCount and its frequency in the window is equal to its frequency in tCount
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formed++;
            }

            // While the window contains all characters of t and the left pointer is not at the beginning of the window
            while (left <= right && formed == required) {
                c = s[left];

                // Update the minimum window if the current window is smaller
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minStart = left;
                }

                // Contract the window from the left
                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }

                left++;
            }

            right++;
        }

        // Return the minimum window substring
        return minLen == INT_MAX ? "" : s.substr(minStart, minLen);
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
- Use a sliding window approach with two pointers to track the minimum window in `s` that contains all characters of `t`.
- Maintain a frequency count of characters in `t` and update it as the window moves.
- The time complexity is O(|s| + |t|) due to the single pass through both strings.