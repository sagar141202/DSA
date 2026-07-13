# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings `s` and `t` consist of lowercase English letters, and the length of both strings is between 1 and 10^4.

## Approach
The algorithm uses a frequency count approach to compare the characters in both strings. It counts the frequency of each character in the first string and then subtracts the frequency of each character in the second string. If all counts are zero at the end, the strings are anagrams.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // If the strings are not of the same length, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Create a frequency count array
        int count[26] = {0};
        
        // Count the frequency of each character in the first string
        for (char c : s) {
            count[c - 'a']++;
        }
        
        // Subtract the frequency of each character in the second string
        for (char c : t) {
            count[c - 'a']--;
        }
        
        // If all counts are zero, the strings are anagrams
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        
        return true;
    }
};
```

## Test Cases
```
Input: s = "anagram", t = "nagaram"
Output: true
Input: s = "rat", t = "car"
Output: false
```

## Key Takeaways
- Use a frequency count approach to compare the characters in both strings.
- The time complexity is O(n), where n is the length of the strings.
- The space complexity is O(1), as we only use a fixed-size array to store the frequency counts.