# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window should contain all characters of `t` with their respective frequencies. For example, if `t = "abc"`, the window in `s` should contain at least one `a`, one `b`, and one `c`. The constraints are: `1 <= s.length, t.length <= 10^5` and `s` and `t` consist of lowercase English letters.

## Approach
We will use a sliding window approach to solve this problem. We will maintain two pointers, `left` and `right`, to represent the window in `s`. We will also maintain a frequency map of characters in `t` and a frequency map of characters in the current window.

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
        // Base case: If string `t` is longer than string `s`, return an empty string
        if (t.length() > s.length()) {
            return "";
        }

        // Create a frequency map of characters in string `t`
        unordered_map<char, int> tCount;
        for (char c : t) {
            tCount[c]++;
        }

        // Initialize variables to keep track of the minimum window
        int requiredChars = tCount.size();
        int formedChars = 0;
        int windowSize = INT_MAX;
        int left = 0;
        int minWindowLeft = 0;
        int minWindowRight = 0;

        // Create a frequency map of characters in the current window
        unordered_map<char, int> windowCounts;

        // Expand the window to the right
        for (int right = 0; right < s.length(); right++) {
            char c = s[right];
            windowCounts[c]++;

            // If the current character is in `t` and its frequency in the window is equal to its frequency in `t`, increment `formedChars`
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formedChars++;
            }

            // While the window contains all characters of `t` and the left pointer is not at the beginning of the window
            while (left <= right && formedChars == requiredChars) {
                // Update the minimum window size and its boundaries
                if (right - left + 1 < windowSize) {
                    windowSize = right - left + 1;
                    minWindowLeft = left;
                    minWindowRight = right;
                }

                // Shrink the window from the left
                char c = s[left];
                windowCounts[c]--;

                // If the current character is in `t` and its frequency in the window is less than its frequency in `t`, decrement `formedChars`
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formedChars--;
                }

                // Move the left pointer to the right
                left++;
            }
        }

        // Return the minimum window substring or an empty string if no such window exists
        return windowSize == INT_MAX ? "" : s.substr(minWindowLeft, minWindowRight - minWindowLeft + 1);
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

Input: s = "bba", t = "ab"
Output: "ba"
```

## Key Takeaways
- The sliding window approach can be used to solve problems that involve finding a subarray or substring with certain properties.
- Using frequency maps can help keep track of the characters in the window and the target string.
- The `formedChars` variable is used to keep track of the number of characters in the window that match the characters in the target string.