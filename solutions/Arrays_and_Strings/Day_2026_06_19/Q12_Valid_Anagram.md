# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings `s` and `t` consist of lowercase English letters, and the length of both strings is between 1 and 100.

## Approach
The approach is to sort both strings and compare them. If the sorted strings are equal, then the original strings are anagrams. Alternatively, we can use a frequency count array to compare the frequency of each character in both strings.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // If the lengths of the strings are not equal, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Sort both strings and compare them
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        // If the sorted strings are equal, the original strings are anagrams
        return s == t;
    }
    
    // Alternative solution using frequency count array
    bool isAnagramAlt(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
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
Input: s = "listen", t = "silent"
Output: true

Input: s = "hello", t = "world"
Output: false
```

## Key Takeaways
- An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
- We can use sorting or frequency count arrays to determine if two strings are anagrams.
- The time complexity of the sorting approach is O(n log n), while the frequency count approach has a time complexity of O(n).