# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order, but each character in `t` must appear at least as many times in the window as it appears in `t`. For example, if `t = "abc"` and `s = "abcabc"`, the minimum window is `"abc"`. If `t = "aaa"` and `s = "aa"`, there is no minimum window because the window must contain at least three `'a'` characters.

## Approach
The algorithm uses a sliding window approach with two pointers to track the minimum window. It utilizes a frequency map to keep track of characters in `t` and another map to track characters in the current window. The algorithm expands the window to the right and contracts it from the left when all characters in `t` are found.

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
        if (s.empty() || t.empty() || s.length() < t.length()) {
            return "";
        }

        // Create a frequency map for string t
        unordered_map<char, int> tCount;
        for (char c : t) {
            tCount[c]++;
        }

        // Initialize variables to track the minimum window
        int requiredChars = tCount.size();
        int formedChars = 0;

        // Initialize window boundaries
        int windowCounts = 0;
        int minWindowLength = INT_MAX;
        int minWindowStart = 0;
        int minWindowEnd = 0;

        // Create a frequency map for the current window
        unordered_map<char, int> windowCountsMap;

        // Initialize the window start pointer
        int start = 0;

        // Traverse the string s
        for (int end = 0; end < s.length(); end++) {
            // Add the character at the end pointer to the window
            char rightChar = s[end];
            windowCountsMap[rightChar]++;

            // If the added character is in t and its frequency in the window is equal to its frequency in t,
            // increment the formedChars count
            if (tCount.find(rightChar) != tCount.end() && windowCountsMap[rightChar] == tCount[rightChar]) {
                formedChars++;
            }

            // Try to contract the window as long as the window contains all characters of t
            while (start <= end && formedChars == requiredChars) {
                // Update the minimum window if the current window is smaller
                if (end - start + 1 < minWindowLength) {
                    minWindowLength = end - start + 1;
                    minWindowStart = start;
                    minWindowEnd = end;
                }

                // Remove the character at the start pointer from the window
                char leftChar = s[start];
                windowCountsMap[leftChar]--;

                // If the removed character is in t and its frequency in the window is less than its frequency in t,
                // decrement the formedChars count
                if (tCount.find(leftChar) != tCount.end() && windowCountsMap[leftChar] < tCount[leftChar]) {
                    formedChars--;
                }

                // Move the start pointer to the right
                start++;
            }
        }

        // Return the minimum window substring
        return minWindowLength == INT_MAX ? "" : s.substr(minWindowStart, minWindowLength);
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
- The sliding window approach is useful for finding the minimum window that contains all characters of a given string.
- Using frequency maps can help track the characters in the window and the given string efficiently.
- The algorithm should expand the window to the right and contract it from the left when all characters in the given string are found.