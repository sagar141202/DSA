# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The constraints are: `1 <= s.length, t.length <= 10^5`, and `s` and `t` consist of English letters.

## Approach
The approach involves using a sliding window technique with two pointers, `left` and `right`, to represent the window in `s`. We also use two frequency maps to keep track of the characters in `t` and the current window.

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
        // Base case
        if (s.length() < t.length()) {
            return "";
        }

        // Frequency map for string t
        unordered_map<char, int> tCount;
        for (char c : t) {
            tCount[c]++;
        }

        // Initialize variables
        int required = tCount.size();
        int left = 0;
        int minLen = INT_MAX;
        int minStart = 0;
        int formed = 0;

        // Frequency map for the current window
        unordered_map<char, int> windowCounts;

        // Traverse the string s
        for (int right = 0; right < s.length(); right++) {
            char c = s[right];
            windowCounts[c]++;

            // If the frequency of the current character in the window is equal to the frequency in t,
            // increment the formed count
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formed++;
            }

            // While the window contains all characters of t and the left pointer is not at the start of the window
            while (left <= right && formed == required) {
                // Update the minimum length and start index if the current window is smaller
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minStart = left;
                }

                // Move the left pointer to the right
                char c = s[left];
                windowCounts[c]--;

                // If the frequency of the character at the left pointer in the window is less than the frequency in t,
                // decrement the formed count
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }

                left++;
            }
        }

        // Return the minimum window substring or an empty string if no such window exists
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
- Use a sliding window approach with two pointers to efficiently find the minimum window substring.
- Utilize frequency maps to keep track of the characters in the string `t` and the current window.
- Update the minimum length and start index whenever a smaller window is found that contains all characters of `t`.