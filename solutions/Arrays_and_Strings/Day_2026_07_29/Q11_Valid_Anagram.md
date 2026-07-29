# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The input strings may contain any ASCII characters, and the function should be case-sensitive. For example, given `s = "listen"` and `t = "silent"`, the function should return `true`, while given `s = "hello"` and `t = "world"`, the function should return `false`.

## Approach
The approach to solve this problem is to use a frequency counting technique, where we count the frequency of each character in both strings and compare the resulting frequency counts. If the frequency counts are equal, then `t` is an anagram of `s`. We can use an unordered map to store the frequency counts.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // If the two strings have different lengths, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Create an unordered map to store the frequency counts
        unordered_map<char, int> count;
        
        // Count the frequency of each character in the first string
        for (char c : s) {
            count[c]++;
        }
        
        // Subtract the frequency of each character in the second string
        for (char c : t) {
            count[c]--;
            // If the frequency count is negative, the strings are not anagrams
            if (count[c] < 0) {
                return false;
            }
        }
        
        // If we have not returned false by now, the strings are anagrams
        return true;
    }
};
```

## Test Cases
```
Input: s = "listen", t = "silent"
Output: true
Input: s = "hello", t = "world"
Output: false
```

## Key Takeaways
- Use a frequency counting technique to compare the characters in the two strings.
- Use an unordered map to store the frequency counts for efficient lookup and update.
- Check for the lengths of the strings before comparing the frequency counts.