# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The substring should be a contiguous sequence of characters within the string. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Another example is the string "bbbbb", where the longest substring without repeating characters is "b" with a length of 1. The string `s` consists of English letters and has a length between 0 and 5 * 10^4.

## Approach
The algorithm uses a sliding window approach with two pointers to track the current substring. It also utilizes an unordered set to store unique characters within the current window. The intuition is to expand the window to the right when a new character is encountered and shrink the window from the left when a repeating character is found.

## Complexity
- Time: O(n)
- Space: O(min(n, m))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Initialize an unordered set to store unique characters
        unordered_set<char> charSet;
        
        // Initialize two pointers for the sliding window
        int left = 0;
        
        // Initialize the maximum length of substring
        int maxLength = 0;
        
        // Iterate over the string
        for (int right = 0; right < s.length(); right++) {
            // While the current character is in the set, remove the leftmost character
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]);
                left++;
            }
            
            // Add the current character to the set
            charSet.insert(s[right]);
            
            // Update the maximum length
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};

int main() {
    Solution solution;
    string s = "abcabcbb";
    cout << "Length of longest substring: " << solution.lengthOfLongestSubstring(s) << endl;
    return 0;
}
```

## Test Cases
```
Input: "abcabcbb"
Output: 3
Input: "bbbbb"
Output: 1
Input: "pwwkew"
Output: 3
```

## Key Takeaways
- Use a sliding window approach to efficiently track the current substring.
- Utilize an unordered set to store unique characters within the current window.
- The time complexity is O(n) because each character is visited at most twice (once by the right pointer and once by the left pointer).