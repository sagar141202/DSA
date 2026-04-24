# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The input strings only contain lowercase English letters and have a length of at most 100 characters.

## Approach
The algorithm uses sorting to compare the characters in the two strings. If the sorted strings are equal, then `t` is an anagram of `s`. Alternatively, a frequency count array can be used to compare the character frequencies in the two strings.

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
        // If the two strings have different lengths, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Sort the characters in the two strings and compare
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        // Return true if the sorted strings are equal, false otherwise
        return s == t;
    }
};

// Alternatively, using a frequency count array
class Solution {
public:
    bool isAnagram(string s, string t) {
        // If the two strings have different lengths, they cannot be anagrams
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
        
        // Check if all frequencies are zero
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        
        // If all frequencies are zero, the strings are anagrams
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
- Sorting the characters in the two strings and comparing the results can determine if one string is an anagram of the other.
- A frequency count array can also be used to compare the character frequencies in the two strings and determine if they are anagrams.